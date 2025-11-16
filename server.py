import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from flask import Flask, render_template, Response, request, jsonify
from fer import FER
import cv2
import sqlite3
import numpy as np
import random
# server.py (top)
import sys, traceback
try:
    from fer import FER
    print("Imported FER OK. fer.__version__:", getattr(__import__("fer"), "__version__", "unknown"))
except Exception as e:
    print("ERROR importing FER:", repr(e), file=sys.stderr, flush=True)
    traceback.print_exc()
    # exit so Gunicorn log contains the trace (optional)
    sys.exit(1)

from flask import Flask



app = Flask(__name__)
detector = FER()

def get_recommendations(emotion):
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT r.recommendation, c.name 
        FROM recommendations r 
        JOIN categories c ON r.category_id = c.id 
        WHERE r.emotion = ?
    ''', (emotion,))
    
    recommendations = cursor.fetchall()
    conn.close()

    if not recommendations:
        print(f"No recommendations found for emotion: {emotion}")
        return []


    categorized_recommendations = {'movie': [], 'place': [], 'song': [], 'food': [], 'activity': []}
    for recommendation, category in recommendations:
        if category in categorized_recommendations:
            categorized_recommendations[category].append(recommendation)


    selected_recommendations = []
    for category in categorized_recommendations:
        if categorized_recommendations[category]:
            selected_recommendations.append((random.choice(categorized_recommendations[category]), category))


    while len(selected_recommendations) < 5:
        for category in categorized_recommendations:
            if categorized_recommendations[category] and len(selected_recommendations) < 5:
                recommendation = random.choice(categorized_recommendations[category])
                if recommendation not in [rec[0] for rec in selected_recommendations]:
                    selected_recommendations.append((recommendation, category))

    return selected_recommendations



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def generate_frames():
        cap = cv2.VideoCapture(0)
        while True:
            success, frame = cap.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        cap.release()

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    in_memory_file = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)

    emotion, score = detector.top_emotion(image)
    print(f"Detected emotion: {emotion}") 
    recommendations = get_recommendations(emotion)

    return jsonify({'emotion': emotion, 'recommendations': recommendations})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)