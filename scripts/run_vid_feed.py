import torch
import cv2
import time

# Set paths to your dataset.yaml and model weights (replace these with actual paths)
dataset_yaml = r"C:\Users\PRATYUSH\Desktop\waste seg\yolo\dataset.yaml"
model_weights = r"C:\Users\PRATYUSH\Desktop\waste seg\yolov5l.pt"

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_weights)  # Load custom model

# Initialize the video capture (0 for webcam or provide video file path)
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide a video file path

# Check if the video feed is opened correctly
if not cap.isOpened():
    print("Error: Could not open video feed.")
    exit()

# Start measuring time for FPS calculation
prev_time = time.time()

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference (detection) on the current frame
    results = model(frame)  # Run the model on the current frame
    
    # Render the results (boxes, labels, and confidences)
    results.render()  # This adds the boxes to the frame

    # Display the frame with detections
    cv2.imshow("YOLOv5 Detection", frame)

    # Calculate FPS (frames per second)
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Print FPS on the frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
