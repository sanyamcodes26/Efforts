import cv2


def read_img():
    img = cv2.imread("14_OpenCV_1.jpg", 1)
    print(type(img))
    print(img)
    print(img.shape)
    print("*" * 10)

    img = cv2.imread("14_OpenCV_1.jpg", 0)
    print(type(img))
    print(img)
    print(img.shape)


def display_img():
    img = cv2.imread("14_OpenCV_1.jpg", 1)
    cv2.imshow("Image", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def resize_image():
    # shrink as well as enlarge
    img = cv2.imread("14_OpenCV_1.jpg", 1)
    res_img = cv2.resize(img, (100, 50))
    cv2.imshow("Res_Image", res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    res_img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
    cv2.imshow("Res_Image", res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def face_detection():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread("14_OpenCV_1.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    print(type(faces))
    print(faces)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    resized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    cv2.imshow("Gray", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def video_capture_1():
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    print(check)
    print(frame)
    # time.sleep(3)
    cv2.imshow("Capturing", frame)
    cv2.waitKey(0)
    video.release()
    cv2.destroyAllWindows()


def video_capture_2():
    video = cv2.VideoCapture(0)
    a = 1
    while True:
        a += 1
        check, frame = video.read()
        print("#" * 20)
        print(check)
        print(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing", gray)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    print(a)
    video.release()
    cv2.destroyAllWindows()


def video_face():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)
    a = 1
    while True:
        a += 1
        check, frame = video.read()
        print("#" * 20)
        print("Check : ", check)
        print("FRAME : ")
        print(frame)

        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
        print("FACE : ")
        print(faces)

        for x, y, w, h in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        resized = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
        cv2.imshow("Capturing", resized)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    print(a)
    video.release()
    cv2.destroyAllWindows()


def motion_detection():
    import pandas as pd
    from datetime import datetime

    first_frame = None

    status_list = [None, None]
    times = []
    df = pd.DataFrame(columns=["Start", "End"])

    video = cv2.VideoCapture(0)
    while True:
        check, frame = video.read()

        status = 0

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if first_frame is None:
            first_frame = gray
            continue
        delta_frame = cv2.absdiff(first_frame, gray)
        thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
        major = cv2.__version__.split('.')[0]
        if major == '3':
            ret, contours, hierarchy = cv2.findContours(thresh_delta.copy(),
                                                        cv2.RETR_EXTERNAL,
                                                        cv2.CHAIN_APPROX_SIMPLE)
        else:
            contours, hierarchy = cv2.findContours(thresh_delta.copy(),
                                                   cv2.RETR_EXTERNAL,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 1000:
                continue

            status = 1

            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now().time())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now().time())

        cv2.imshow("Frame", frame)
        cv2.imshow("Capturing", gray)
        cv2.imshow("Delta", delta_frame)
        cv2.imshow("Thresh", thresh_delta)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    print(status_list)
    print(times)
    for i in range(0, len(times), 2):
        df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)
    df.to_csv("14_OpenCV.csv")

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # read_img()
    # display_img()
    # resize_image()
    # face_detection()
    # video_capture_1()
    # video_capture_2()
    # video_face()
    motion_detection()
