import cv2 as cv

def captureVideo():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("cannot open camera")
        return

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
