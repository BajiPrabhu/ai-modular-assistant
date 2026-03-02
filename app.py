from flask import Flask, render_template, request, jsonify
from modules.voice.text_to_speech import speak
from modules.voice.speech_to_text import listen

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak_route():
    data = request.json
    text = data.get("text")
    speak(text)
    return jsonify({"status": "spoken", "text": text})

@app.route("/listen", methods=["GET"])
def listen_route():
    text = listen()
    return jsonify({"recognized_text": text})

if __name__ == "__main__":
    app.run(debug=False)