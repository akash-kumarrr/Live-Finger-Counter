# Live Finger Counter

A Python application that uses OpenCV and Google's MediaPipe library to detect hands in a webcam feed and count the number of extended fingers in real-time. The project includes both a standalone desktop application and a web version powered by Flask that streams the output to a browser.

 

---

## Features

- **Real-time Hand Detection**: Utilizes MediaPipe Hands to accurately detect 21 keypoints on the hand.
- **Finger Counting**: Implements logic to determine if each finger is extended or closed.
- **Desktop App**: A simple, standalone version that runs locally using `new.py`.
- **Web Application**: A Flask server (`app.py`) that streams the processed video feed to any web browser on your local network.
- **Cross-platform**: Runs on any operating system where Python and OpenCV are supported.

## Tech Stack

- **Python**
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand landmark detection.
- **Flask**: For the web application and video streaming.

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Live-Finger-Counter.git
    cd Live-Finger-Counter
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

You can run either the standalone desktop version or the web application.

### 1. Standalone Desktop App

To run the local version that opens a window on your desktop:
```bash
python new.py
```
Press `q` to quit.

### 2. Web Application

To stream the feed to a web browser:
```bash
python app.py
```
Then, open a web browser and navigate to `http://127.0.0.1:5000`. You can also access it from other devices on the same network using your computer's local IP address (e.g., `http://192.168.1.10:5000`).

---

## Project Structure

- `app.py`: The Flask web server for streaming video.
- `main.py`: Contains the core finger counting and frame processing logic.
- `new.py`: A standalone script for running the application on the desktop.
- `templates/index.html`: The HTML page for the web interface.
- `requirements.txt`: A list of Python dependencies for the project.
