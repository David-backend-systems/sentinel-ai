import cv2
import time
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
prev_time = time.time()
model = YOLO("yolov8n.pt")

while True:
    current_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    
    fps = 1.0 / (current_time - prev_time + 0.001)
    prev_time = current_time
    
    result = model.track(frame, persist=True)
    people_count = 0
    if result[0].boxes.id is not None:
        classes = result[0].boxes.cls.cpu().numpy()
        people_count = sum(1 for c in classes if model.names[int(c)] == "person")
    annotated = result[0].plot()
    
    cv2.putText(annotated, f"FPS: {fps:.1f}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    
    cv2.imshow("Sentinel AI", annotated)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()