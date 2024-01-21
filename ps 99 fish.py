import time  
import threading  
from pynput.mouse import Button, Controller  
  
from pynput.keyboard import Listener, KeyCode  
from pynput.keyboard import Controller as kc
  
  
delayTime = 0.001  
buttonDirection = Button.left  
startStopButton = KeyCode(char='k')  
terminateButton = KeyCode(char='l')  
  
class ClickTheMouse(threading.Thread):  
    def __init__(self, delayTime, buttonDirection):  
        super(ClickTheMouse, self).__init__()  
        self.delayTime = delayTime  
        self.buttonDirection = buttonDirection  
        self.running = False  
        self.program_running = True  
        self.key = kc()
        self.timeCount = 0
  
    def startMouseclick(self):  
        self.running = True  
  
    def stopMouseClick(self):  
        self.running = False  
  
    def exitScript(self):  
        self.stopMouseClick()  
        self.program_running = False  
          
    def run(self):  
        while self.program_running:  
            while self.running:  
                if self.timeCount < 3:
                    pass
                elif self.timeCount < 8:
                    mouse.click(self.buttonDirection)
                else:
                    self.timeCount = 0
                self.timeCount +=0.1
                time.sleep(0.1)
            time.sleep(0.5)  
  
mouse = Controller()  
clickThread = ClickTheMouse(delayTime, buttonDirection)  
clickThread.start()  
  
def on_press(key):
    if key == startStopButton:  
        if clickThread.running:  
            clickThread.stopMouseClick()  
        else:  
            clickThread.startMouseclick()  
    elif key == terminateButton:  
        clickThread.exitScript()  
        listener.stop()  
  
  
with Listener(on_press=on_press) as listener:  
    listener.join()  