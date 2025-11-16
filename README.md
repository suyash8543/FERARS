FERARS – Facial Expression Recognition & Recommendation System

A Real-Time Emotion Detection & Smart Recommendation Tool

FERARS is a Python-based real-time facial expression recognition system that uses OpenCV, FER, and Flask to detect human emotions through a webcam feed.
Based on the detected emotion, the system provides personalized recommendations such as songs, quotes, activities, or motivational messages.

🚀 Features
🎭 Emotion Detection

Detects emotions like Happy, Sad, Angry, Neutral, Disgust, Surprise, Fear

Uses the FER library for deep-learning-based recognition

Real-time webcam feed processing using OpenCV

🤝 Recommendation System

Provides emotion-based recommendations such as:

Music playlists

Motivational quotes

Activities

Self-care recommendations

Uses custom logic + SQLite database support (optional)

🌐 Web Interface

Built using Flask

Streams live camera feed to frontend

Simple and clean UI (HTML, CSS, JS)

🗄️ Database Support

Uses SQLite3 for storing user interactions / logs (optional)

🛠️ Tech Stack
Backend

Python

Flask

FER

OpenCV

NumPy

SQLite3

Frontend

HTML5

CSS3

JavaScript

📁 Project Structure
FERARS/
│── backend/
│   └── app.py
│── frontend/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── login.html
│   ├── css/
│   └── js/
│── database/
│   └── ferars.db
│── models/
│── static/
│── templates/
│── .gitignore
│── README.md

⚙️ How It Works

The webcam feed is captured using OpenCV

The image frames are passed to FER() detector

The model returns emotion scores

FERARS selects the highest-probability emotion

The system returns personalized recommendations (JSON / HTML)

The frontend displays results in real time

📦 Installation
1. Clone the Repository
git clone https://github.com/yourusername/Ferars.git
cd Ferars

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows

3. Install Dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, here are the main libraries:

pip install opencv-python flask fer numpy

▶️ Run the Application
python app.py


Then open the app in your browser:
👉 http://127.0.0.1:5000

🧠 Emotion Labels Detected

FERARS supports these emotions:

Emotion	Description
Happy	Positive mood, smiling
Sad	Low mood, frowning
Angry	Frustrated, irritated
Neutral	No strong expression
Surprise	Shock / astonishment
Disgust	Disapproval
Fear	Anxiety / fear
💡 Future Enhancements

Integrate Machine Learning model (CNN) for emotion recognition

Implement user accounts and analytics

Add voice-based recommendations

Convert app into a mobile application

Add stress level detection using facial indicators

🙌 Contributing

Contributions are welcome!
If you want to improve FERARS, feel free to submit a pull request or open an issue.

📜 License

This project is licensed under the MIT License.

👨‍💻 Developed By

Suyash Tripathi ,Tanmay Vaishth , Sujal Aggrawal , Vikash Verma
FERARS – AI-based Facial Emotion Recognition & Recommendation System