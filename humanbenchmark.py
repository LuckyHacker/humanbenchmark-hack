import pyautogui
from ctypes import windll
import time

sniper_number = 0.080   # Tweak this according to your PC speed
trigger_color = 7002955

if __name__ == "__main__":
    gdi = windll.LoadLibrary("c:\\Windows\\system32\\gdi32.dll")

    while 1:
        begin = time.time()
        width, height = pyautogui.position()
        pixel = int(gdi.GetPixel(windll.user32.GetDC(0), width, height))
        # uncomment if need to change color:
        #print(pixel)
        if pixel == trigger_color:
            while time.time() - begin < sniper_number:
                pass
            pyautogui.click()
