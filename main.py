import cv2
from guidance import guidance

cap = cv2.VideoCapture("http://192.168.42.129:4747/mjpegfeed")

while True:
    success, video = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    x_axis = int(cap.get(3)/2)
    y_axis = int(cap.get(4)/2)
    x, y = guidance("red", video, 135, 135, width, height)
    a = cv2.line(video, (x_axis, 0), (x_axis, height), (255, 0, 0), 1)
    a = cv2.line(video, (0, y_axis), (width, y_axis), (255, 0, 0), 1)
    a = cv2.circle(video, (x_axis, y_axis), 20, (0, 0, 255))
    print("x:", x)
    print("y:", y)
    cv2.imshow("window", video)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
