import cv2, pyautogui
import mediapipe as mp
import pyautogui


x1 = y1 = x2 = y2 = x3 = y3 = y4 = x4 = 0
screenWidth, screenHeight = (2560, 1440)

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:

    _, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    cv2.imshow("Mouse control", image)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)


                if id == 8:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(0,255,255), thickness=3)
                    x1 = x
                    y1 = y


                if id == 4:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(0,0,255), thickness=3)
                    x2 = x
                    y2 = y

                if id == 12:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(0,0,255), thickness=3)
                    x3 = x
                    y3 = y

                if id == 10:
                    x4 = x
                    y4 = y

        # d = √ (x2 - x1)² + (y2 - y1)²            
        dist = ((x2-x1) ** 2 + (y2 - y1) ** 2) ** (0.5) // 4
        click = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** (0.5) // 4
        #cv2.line(image, (x1,y1), (x2,y2),(0,255,0), 5)
        if dist >= 65.0:
            dist = 65.0
        pyautogui.moveTo(x1 * 4, y1 * 3)
        if click < 10:
            pyautogui.click()

        # if dist > 30:
        #     pyautogui.press("volumeup")

        # else:
        #     pyautogui.press("volumedown")
    
    
    
    cv2.imshow("Mouse control", image)
    key = cv2.waitKey(10)
    if key == 13:
        break

webcam.release()
cv2.destroyAllWindows()