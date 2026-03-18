from upload_image import upload_image
from detect_cars import detect_cars
from draw_cars import draw_cars

image_path = upload_image()
car_boxes = detect_cars(image_path)
print("Number of cars detected:", len(car_boxes))
draw_cars(image_path, car_boxes)
