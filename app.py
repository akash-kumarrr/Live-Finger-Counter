from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
from main import process_frame

app = Flask(__name__)

# Initialize MediaPipe Hands globally
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def generate_frames():
    """Generates frames from the webcam to be streamed."""
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to grab frame")
            break
        else:
            # Process the frame using the logic from main.py
            processed_frame = process_frame(frame, hands, mp_drawing, mp_hands.HAND_CONNECTIONS)
            
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()
            
            # Yield the frame in the format required for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
    print("Webcam released.")

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # To make it accessible on your local network, use host='0.0.0.0'
    # For development, you can just run it on the default localhost.
    app.run(host='0.0.0.0', debug=True)