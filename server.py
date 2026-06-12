import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from fer import FER
import cv2
import sqlite3
import numpy as np
import random
import sys, traceback

try:
    from fer import FER
    detector = FER()
    print("FER loaded successfully")
except Exception as e:
    print(f"ERROR loading FER: {repr(e)}", file=sys.stderr, flush=True)
    traceback.print_exc()
    detector = None

app = Flask(__name__)
CORS(app)

def get_recommendations(emotion):
    try:
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
    except Exception as e:
        print(f"Database error: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for Render"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/process_image', methods=['POST'])
def process_image():
    if not detector:
        return jsonify({'error': 'FER not initialized'}), 500
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    try:
        file = request.files['image']
        in_memory_file = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)

        if image is None:
            return jsonify({'error': 'Invalid image'}), 400

        emotion, score = detector.top_emotion(image)
        print(f"Detected emotion: {emotion}") 
        recommendations = get_recommendations(emotion)

        return jsonify({'emotion': emotion, 'score': float(score), 'recommendations': recommendations})
    except Exception as e:
        print(f"Processing error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
