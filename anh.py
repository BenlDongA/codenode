import mediapipe as med
import cv2

# Initialize mediapipe hands and drawing utilities
ph_hand = med.solutions.hands
ve_khung = med.solutions.drawing_utils
hand = ph_hand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    kq = hand.process(frame_rgb)

    if kq.multi_hand_landmarks:
        for idx, moc_tay in enumerate(kq.multi_hand_landmarks):
            dem = 0
            my_hand = []
            my_handx = []

            ph = kq.multi_handedness[idx].classification[0].label
            if ph == 'Right':

                for id, lm in enumerate(moc_tay.landmark):
                    h, w, c = frame.shape
                    tx, ty = int(lm.x * w), int(lm.y * h)
                    my_hand.append(ty)
                    my_handx.append(tx)

                if my_hand[8] < my_hand[6]:
                    dem += 1
                if my_hand[12] < my_hand[10]:
                    dem += 1
                if my_hand[16] < my_hand[14]:
                    dem += 1
                if my_hand[20] < my_hand[18]:
                    dem += 1
                if my_handx[4] < my_handx[3]:
                    dem += 1

                # Determine the color for the landmarks based on the count (dem)
                color = (0, 0, 255)  # Default color (Red)

                if dem == 0:
                    color = (255, 0, 0)  # Blue
                elif dem == 1:
                    color = (0, 255, 255)  # Yellow
                elif dem == 2:
                    color = (0, 0, 255)  # Red
                elif dem == 3:
                    color = (255, 255, 0)  # Cyan
                elif dem == 4:
                    color = (0, 255, 0)  # Green
                elif dem == 5:
                    color = (0, 128, 0)  # Dark Green

                # Print the label to the terminal
                print(f"Số ngón tay: {dem}")

                # Define the drawing specifications with the chosen color
                landmark_spec = ve_khung.DrawingSpec(color=color, thickness=5)

                # Draw landmarks with the specified color
                ve_khung.draw_landmarks(frame, moc_tay, ph_hand.HAND_CONNECTIONS,
                                        landmark_spec, landmark_spec)

                # Draw the text with the specified color
                cv2.putText(frame, f"{dem}", (150, 150), cv2.FONT_HERSHEY_COMPLEX, 3, color, 2)

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
