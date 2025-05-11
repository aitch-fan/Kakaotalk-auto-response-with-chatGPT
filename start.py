import pyautogui
import mouse
import time
import clipboard
from datetime import datetime

c = 0
infomsg = 0
k = True
x1, y1 = (1280,896) #카톡 적는곳
x2, y2 = (1311, 825) #카톡 메시지 있는곳
x3, y3 = (523, 633) #gpt메시지 적는곳
x4, y4 = (515, 334) #gpt메시지 복사하는곳
msg = " "
lastmsg = " "

while k :
    if(input("건너뛰시겠습니까? yes or no :")== 'yes') :
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        break
    if(c==0) : #카톡메시지입력창
        if(infomsg == 0) :
            print("where to write text on kakaotalk?")
            infomsg = 1
        if(mouse.is_pressed("left")) :
            x1, y1 = mouse.get_position()
            print("카톡 메시지 적을곳은 ",x1,y1)
            infomsg = 0
            c = 1
            time.sleep(1)
    if (c == 1): #친구메시지위치
        if (infomsg == 0):
            print("locate your friends msg on kakaotalk.")
            infomsg = 1
        if (mouse.is_pressed("left")):
            x2, y2 = mouse.get_position()
            print("친구 메시지 위치는",x2, y2)
            infomsg = 0
            c = 2
            time.sleep(1)
    if(c==2) :
        if (infomsg == 0):
            print("where to write text on GPT?")
            infomsg = 1
        if (mouse.is_pressed("left")):
            x3, y3 = mouse.get_position()
            infomsg = 0
            c = 3
            time.sleep(1)
    if(c==3) :
        if (infomsg == 0):
            print("where is copy button on GPT?")
            infomsg = 1
        if (mouse.is_pressed("left")):
            x4, y4 = mouse.get_position()
            k = False

print(x1,y1,x2,y2,x3,y3,x4,y4)
print(f"카카오톡 자동응답봇 실행, 시간은 {datetime.now()}")

#매개변수:보낼 메시지
def sendmsg(t) :
    pyautogui.click(x1,y1)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('backspace')
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
#친구의 메시지를 클립보드에 복사해줌
def copymsg() :
    print("copymsg실행")
    time.sleep(0.3)
    pyautogui.rightClick(x2, y2)
    time.sleep(0.3)
    pyautogui.leftClick(1401, 842)
#당장 떠있는 상대의 말을 반환
def returncopymsg() :
    print("returncopymsg실행")
    time.sleep(0.3)
    pyautogui.rightClick(x2,y2)
    time.sleep(0.3)
    pyautogui.leftClick(int(x2)+30, int(y2)+20)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','c')
    if (len(clipboard.paste()) > 100) :
        pyautogui.click()
        return lastmsg
    else : return clipboard.paste()
#매개변수 없음
def gpt() :
    print("gpt실행")
    pyautogui.click(x3,y3)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(6)
    pyautogui.click(x4,y4)
    time.sleep(0.5)

def checkdiff() :
    if(lastmsg == returncopymsg()) : return False
    else : return True


while True:
    time.sleep(1)
    if(checkdiff()) :
        copymsg()
        lastmsg = clipboard.paste()
        gpt()
        sendmsg(clipboard.paste())
        print(f"{clipboard.paste()}를 전송합니다 {datetime.now()}")