import cv2
import mediapipe as mp

# Landmark IDs for the tips of the fingers
TIP_IDS = [4, 8, 12, 16, 20]

def count_fingers(hand_landmarks):
    """Counts the number of extended fingers based on hand landmarks."""
    fingers_up = 0
    landmarks = hand_landmarks.landmark

    # Thumb: Check if the tip is to the left/right of the joint below it.
    # This logic is for a right hand when the image is flipped.
    if landmarks[TIP_IDS[0]].x < landmarks[TIP_IDS[0] - 1].x:
        fingers_up += 1

    # Other 4 fingers: Check if the tip is higher (lower y-coordinate) than the joint two positions below it.
    for i in range(1, 5):
        if landmarks[TIP_IDS[i]].y < landmarks[TIP_IDS[i] - 2].y:
            fingers_up += 1
            
    return fingers_up

def process_frame(img, hands_detector, drawing_utils, hands_connections):
    """Processes a single frame to detect and count fingers."""
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(img, hand_landmarks, hands_connections)

            # Count fingers and display the count
            finger_count = count_fingers(hand_landmarks)
            cv2.putText(img, f'Fingers: {finger_count}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    return img
