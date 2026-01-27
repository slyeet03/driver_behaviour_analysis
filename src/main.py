import cv2 as cv
from utils import config

def captureVideo():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("cannot open camera")
        return
    
    cap.set(cv.CAP_PROP_FPS, config.FPS)
    
    actual_fps = cap.get(cv.CAP_PROP_FPS)
    print(f"Desired FPS: {config.FPS}, Actual FPS set by camera: {actual_fps}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("can't receive frame")
            break

        cv.imshow("live feed", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


captureVideo()
