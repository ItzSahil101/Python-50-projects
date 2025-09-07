import cv2

index = -1
for i in range(5):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        index = i
        cap.release()
        break

face = cv2.VideoCapture(index, cv2.CAP_DSHOW)
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, video = face.read()
    if not ret:
        break

    col = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(col, 1.1, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Video_Live", video)

    if cv2.waitKey(10) & 0xFF == ord("a"):
        break

face.release()
cv2.destroyAllWindows()
