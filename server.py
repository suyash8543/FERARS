import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import cv2
import sqlite3
import numpy as np
import random
import sys
import traceback

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

        cursor.execute("""
            SELECT r.recommendation, c.name
            FROM recommendations r
            JOIN categories c ON r.category_id = c.id
            WHERE r.emotion = ?
        """, (emotion,))

        recommendations = cursor.fetchall()
        conn.close()

        if not recommendations:
            return []

        categorized_recommendations = {
            'movie': [],
            'place': [],
            'song': [],
            'food': [],
            'activity': []
        }

        for recommendation, category in recommendations:
            if category in categorized_recommendations:
                categorized_recommendations[category].append(recommendation)

        selected_recommendations = []

        for category in categorized_recommendations:
            if categorized_recommendations[category]:
                selected_recommendations.append(
                    (
                        random.choice(categorized_recommendations[category]),
                        category
                    )
                )

        return selected_recommendations[:5]

    except Exception as e:
        print(f"Database error: {e}")
        return []


# ======================
# PAGE ROUTES
# ======================

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/capture')
def capture():
    return render_template('capture.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


# ======================
# API ROUTES
# ======================

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route('/process_image', methods=['POST'])
def process_image():

    if detector is None:
        return jsonify({
            "error": "FER detector not initialized"
        }), 500

    if 'image' not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    try:
        file = request.files['image']

        image_bytes = np.frombuffer(
            file.read(),
            np.uint8
        )

        image = cv2.imdecode(
            image_bytes,
            cv2.IMREAD_COLOR
        )

        if image is None:
            return jsonify({
                "error": "Invalid image"
            }), 400

        emotion, score = detector.top_emotion(image)

        if emotion is None:
            return jsonify({
                "emotion": "neutral",
                "score": 0,
                "recommendations": []
            })

        recommendations = get_recommendations(emotion)

        return jsonify({
            "emotion": emotion,
            "score": float(score),
            "recommendations": recommendations
        })

    except Exception as e:
        print(f"Processing error: {e}")
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )