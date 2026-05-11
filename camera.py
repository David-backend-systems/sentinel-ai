import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
prev_time = time.time()

while True:
    
    current_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    fps = 1.0 / (current_time - prev_time + 0.001)
    prev_time = current_time
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.putText(frame, "640x480", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.imshow("Sentinel", frame)
    if cv2.waitKey(30) & 0xFF == ord ('q'):
        break

cap.release()
cv2.destroyAllWindows()