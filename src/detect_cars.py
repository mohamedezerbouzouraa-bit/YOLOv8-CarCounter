from ultralytics import YOLO
def detect_cars(image_path, model_path="yolov8n.pt"):
    model = YOLO(model_path)
    results = model(image_path)
    car_boxes = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            if class_name == "car":
                car_boxes.append(list(map(int, box.xyxy[0])))
    return car_boxes
