import cv2
import mediapipe as mp
import pyautogui
import time
import webbrowser

def playFlappyBirdGame():

  cap = cv2.VideoCapture(0)
  cap.set(3, 780)
  cap.set(4, 520)
  cap.set(15, 0.1)

  url = 'https://flappybird.io/'
  webbrowser.open(url)

  pyautogui.hotkey("winleft", "down")

  mpHands = mp.solutions.hands
  hands = mpHands.Hands()                              
  mpDraw = mp.solutions.drawing_utils

  pTime = 0
  cTime = 0

  guideBar = 0
  doneGuide = False

  while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    height, width, idShape = img.shape

    divideScreenHeight = height//2
    divideScreenWidth = (width-(width//3))-(20*(width//3))//100

    if guideBar <= 80:
      cv2.putText(img, 
              f"Press Q to Exit...", 
              (divideScreenWidth-((divideScreenWidth//2)+( (20*divideScreenWidth//2)//100 ) ), divideScreenHeight+ ((divideScreenHeight//4)*3) ), 
              cv2.FONT_HERSHEY_PLAIN, 
              2,
              (255, 255, 255), 
              2) 
    else:
      doneGuide = True

    guideBar += 1

    cv2.line(img,
             (divideScreenWidth,divideScreenHeight),
             (width,divideScreenHeight),
             (255,255,255),
             2)

    if results.multi_hand_landmarks:
      
      for handLms in results.multi_hand_landmarks:
        
        for id, lm in enumerate(handLms.landmark):
          
          h, w, c = img.shape
          cx, cy = int(lm.x * w), int(lm.y * h)
          mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

          if id == 8 and cy < divideScreenHeight:
            if cx > divideScreenWidth:          
              cv2.putText(img, 
              			  f"Jump!", 
              			  (cx,cy), 
              			  cv2.FONT_HERSHEY_PLAIN, 
              			  2,
                      (64, 225, 128), 
                      2) 
              
              # print("Finger Coordinate = ", cy , " Trigger Axis : ", cx)
              pyautogui.press('space')
              pass

            else:
              pass

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, 
    			  f"FPS : {str(int(fps))}", 
    			  (10, 50), 
    			  cv2.FONT_HERSHEY_PLAIN, 
    			  2,
            (255, 0, 255), 
            1)

    cv2.putText(img, 
            f"Developed by Hanz", 
            (10, 90), 
            cv2.FONT_HERSHEY_PLAIN, 
            2,
            (255, 0, 255), 
            1)

    if doneGuide:
      cv2.putText(img, 
              f"github.com/mfarhanz1", 
              (10, height-50), 
              cv2.FONT_HERSHEY_PLAIN, 
              2,
              (255, 0, 255), 
              1)

    cv2.imshow("Hanz Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      pyautogui.hotkey("winleft","shift","m")
      break

  cap.release()
  cv2.destroyAllWindows()