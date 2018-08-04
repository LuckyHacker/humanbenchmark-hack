import time
import pyautogui
from datetime import datetime
from gi.repository import Gdk


target_time_ms = 100
wait_time_reduce_ms = 30

green_match = b"\x1f\xe4U"
blue_match = b"St\xd5"


def pixel_at(pos):
    x, y = pos
    w = Gdk.get_default_root_window()
    pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
    return pb.get_pixels()


def click_loop():
    while 1:
        begin = datetime.now().microsecond
        mouse_position = pyautogui.position()
        pixel = pixel_at(mouse_position)

        #print(pixel) # Uncomment if need to tweak match colors

        if pixel == green_match:
            end = (datetime.now().microsecond - begin) / 1000
            time_to_wait_ms = target_time_ms - end - wait_time_reduce_ms
            time.sleep(time_to_wait_ms / 1000)
            pyautogui.click()

        if pixel == blue_match:
            pyautogui.click()


if __name__ == "__main__":
    click_loop()
