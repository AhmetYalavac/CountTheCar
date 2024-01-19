#import libraries of python opencv
import cv2

# capture video/ video path
cap = cv2.VideoCapture('cars.mp4')


#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('cars.xml')

car_count = 0
#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()

    #convert video into gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect cars in the video
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #to draw a rectangle in each cars 
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        crop_img = frame[y:y + h, x:x + w]
        if x>50 and x<75:
            car_count += 1
        cv2.putText(frame, f'Car {car_count}', (15,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.line(img=frame, pt1=(0, 50), pt2=(frame.shape[1], 50), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
        cv2.line(img=frame, pt1=(0, 65), pt2=(frame.shape[1], 65), color=(255, 0, 0), thickness=5, lineType=8,
                 shift=0)
        cv2.line(img=frame, pt1=(x, int(y+h/2)), pt2=(x+w, int(y+h/2)), color=(0, 0, 255), thickness=5, lineType=8,
                 shift=0)
    cv2.imshow('video', frame)
     #press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

print(car_count)
#release the video-capture object
cap.release()
#close all the frames
cv2.destroyAllWindows() 