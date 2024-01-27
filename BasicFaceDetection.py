import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
face_cascade = mp.solutions.face_detection
face_reco = face_cascade.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
    
    verify, frame = webcam.read()
    frame = cv2.flip(frame,1)
    if not verify:
        break

    face_list = face_reco.process(frame)

    if face_list.detections:
        for face in face_list.detections:
            draw.draw_detection(frame, face)
    
    cv2.imshow("Face Reco", frame)
    
    if cv2.waitKey(5) == 27:
        break
webcam.release()