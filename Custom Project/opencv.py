import cv2
import mediapipe as mp
import numpy as np

# Inisialisasi
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

canvas = np.zeros((480, 640, 3), dtype=np.uint8)
cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0

def is_fist(landmarks):
    # Mengecek apakah semua jari kecuali ibu jari ditekuk (telunjuk, tengah, manis, kelingking)
    # Tip jari: 8, 12, 16, 20
    # MCP jari: 5, 9, 13, 17
    tips = [8, 12, 16, 20]
    mcps = [5, 9, 13, 17]
    for tip, mcp in zip(tips, mcps):
        if landmarks[tip].y < landmarks[mcp].y:
            return False  # Jika satu saja terbuka, bukan kepalan
    return True

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm_list = handLms.landmark
            fist = is_fist(lm_list)

            # Ambil koordinat ujung jari telunjuk (landmark 8)
            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)

            if not fist:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y
                cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 255, 255), 4)
                prev_x, prev_y = x, y
            else:
                prev_x, prev_y = 0, 0  # Reset jika mengepal

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    else:
        prev_x, prev_y = 0, 0

    combined = cv2.add(frame, canvas)
    cv2.imshow("Air Writing", combined)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)

cap.release()
cv2.destroyAllWindows()
