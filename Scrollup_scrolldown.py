import cv2

import time

import pyautogui

import mediapipe as mp

from mediapipe.tasks import python

from mediapipe.tasks.python import vision

MODEL_PATH = "hand_landmarker.task"

SCROLL_SPEED = 300

SCROLL_DELAY = 1

CAM_WIDTH = 640

CAM_HEIGHT = 480
BaseOptions = python.BaseOptions

options = vision.HandLandmarkerOptions(

base_options=BaseOptions(model_asset_path=MODEL_PATH),

running_mode=vision.RunningMode.VIDEO,

num_hands=1,

min_hand_detection_confidence=0.7,

min_hand_presence_confidence=0.7,

min_tracking_confidence=0.7

)

landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

last_scroll = 0

p_time = 0

start_time = time.time()

print("Gesture Scroll Control Active")

print("Open palm = Scroll Up")

print("Fist = Scroll Down")

print("Press q to Exit")

connections = [

(0,1),(1,2),(2,3),(3,4),

(0,5),(5,6),(6,7),(7,8),

(5,9),(9,10),(10,11),(11,12),

(9,13),(13,14),(14,15),(15,16),

(13,17),(17,18),(18,19),(19,20),

(0,17)

]
def draw_hand(frame, landmarks, w, h):

    points = []

    for lm in landmarks:

        x = int(lm.x * w)

        y = int(lm.y * h)

        points.append((x, y))

        cv2.circle(frame, (x, y), 5, (0,255,0), -1)

    for a, b in connections:

        cv2.line(frame, points[a], points[b], (255,0,0), 2)
    
def detect_gesture(landmarks, handedness):

    fingers = []

    tips = [8, 12, 16, 20]

    # Fingers

    for tip in tips:

        if landmarks[tip].y < landmarks[tip - 2].y:

                fingers.append(1)

    # Thumb

    thumb_tip = landmarks[4]

    thumb_ip = landmarks[3]

    if (

    handedness == "Right" and thumb_tip.x > thumb_ip.x

    ) or (

    handedness == "Left" and thumb_tip.x < thumb_ip.x

    ):

        fingers.append(1)

    if sum(fingers) == 5:

        return "scroll_up"

    elif len(fingers) == 0:

        return "scroll_down"

    return "none"
while True:

    success, frame = cap.read()

    if not success:

        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(

    image_format=mp.ImageFormat.SRGB,

    data=rgb_frame

    )

    timestamp_ms = int((time.time() - start_time) * 1000)

    result = landmarker.detect_for_video(

    mp_image,

    timestamp_ms

    )

    gesture = "none"

    handedness = "Unknown"

    h, w, c = frame.shape

    if result.hand_landmarks:

        for i, hand_landmarks in enumerate(result.hand_landmarks):

            handedness = result.handedness[i][0].category_name

            gesture = detect_gesture(

            hand_landmarks,

            handedness

            )

            draw_hand(frame, hand_landmarks, w, h)

            if (time.time() - last_scroll) > SCROLL_DELAY:

                if gesture == "scroll_up":

                    pyautogui.scroll(SCROLL_SPEED)

            elif gesture == "scroll_down":

                pyautogui.scroll(-SCROLL_SPEED)

                last_scroll = time.time()

    # FPS

    c_time = time.time()

    fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0

    p_time = c_time

    cv2.putText(

    frame,

    f"FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}",

    (10, 30),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.7,

    (255, 0, 0),

    2

    )

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
cap.release()
cv2.destroyAllWindows()