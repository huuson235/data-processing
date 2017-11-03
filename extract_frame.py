import cv2

cap = cv2.VideoCapture('sperms.mp4')
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
ret = True
i = 5

while ret:
    ret, frame = cap.read()
    if i % 5 == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = clahe.apply(frame)
        frame = cv2.medianBlur(frame, 5)
        name = str(10000 + i)
        name = name[1:]
        cv2.imwrite('frames/' + name +'.jpg', frame)
    i += 1
print i
