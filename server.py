from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")

    # If given text is empty 
    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400
    
    response = emotion_detector(text_to_analyze)
    
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # If there is no dominant emotion 
    if dominant_emotion is None:
        return "Invalid text! Please try again.", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
