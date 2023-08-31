from PIL import ImageGrab
import numpy as np
import cv2
import time
from pynput import keyboard
import pyautogui

# Kare koordinatları (sol üst x, sol üst y, sağ alt x, sağ alt y)
square_coords = (870, 100, 1050, 120)

# İzlemek istediğiniz bölgenin koordinatları (sol üst x, sol üst y, sağ alt x, sağ alt y)
watch_region = (870, 100, 1050, 120)

# Önceki ekran görüntüsü
previous_image = None

# Q tuşuna basılı olduğunu kontrol eden değişken
q_key_pressed = False

def on_key_press(key):
    global q_key_pressed
    try:
        if key.char == 'q':
            if not q_key_pressed:
                q_key_pressed = True
                print("Q tuşuna basıldı! q_key_pressed:", q_key_pressed)
    except AttributeError:
        pass

def on_key_release(key):
    global q_key_pressed
    try:
        if key.char == 'q':
            if q_key_pressed:
                q_key_pressed = False
                print("Q tuşu bırakıldı! q_key_pressed:", q_key_pressed)
    except AttributeError:
        pass

def check_for_changes():
    global previous_image
    
    # Belirlediğiniz bölgeden ekran görüntüsü al
    screenshot = ImageGrab.grab(bbox=watch_region)
    
    # Ekran görüntüsünü NumPy dizisine dönüştür
    current_image = np.array(screenshot)
    
    # İlk döngüde önceki ekran görüntüsü yoksa, şu anki ekran görüntüsünü kaydet
    if previous_image is None:
        previous_image = current_image
        return
    
    # Önceki ve şu anki ekran görüntülerini karşılaştır
    difference = np.sum(current_image != previous_image)
    
    # Eğer fark varsa ve q tuşu basılı değilse, sol fare tuşuna bas
    if difference > 0 and not q_key_pressed:
        # Burada yapmak istediğiniz işlemi gerçekleştirin
        pyautogui.click(button="left")
        print("Değişiklik tespit edildi!")
    
    # Şu anki ekran görüntüsünü önceki ekran görüntüsü olarak kaydet
    previous_image = current_image

def main():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        while True:
            # Q tuşuna basılıysa, bekleme süresi boyunca algılamayı atla
            if q_key_pressed:
                time.sleep(1)
                continue

            check_for_changes()
            
    
    listener.join()

if __name__ == "__main__":
    main()
