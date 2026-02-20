import cv2
import mediapipe as mp
import math
import numpy as np
import screen_brightness_control as sbc
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load MediaPipe model
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

print("Brightness Control Started")
print("Pinch thumb and index to adjust brightness")
print("Press 'q' to quit\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    result = landmarker.detect(mp_image)

    if result.hand_landmarks:
        hand_landmarks = result.hand_landmarks[0]

        thumb = hand_landmarks[4]
        index = hand_landmarks[8]

        x1, y1 = int(thumb.x * w), int(thumb.y * h)
        x2, y2 = int(index.x * w), int(index.y * h)

        cv2.circle(frame, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (0, 255, 0), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)

        # Distance calculation
        distance = math.hypot(x2 - x1, y2 - y1)

        # Map distance to brightness (adjust 30–250 if needed)
        brightness = np.interp(distance, [30, 250], [0, 100])

        sbc.set_brightness(int(brightness))

        cv2.putText(frame, f'Brightness: {int(brightness)}%',
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 255, 0),
                    3)

    cv2.imshow("Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()