from PIL import ImageGrab
import numpy as np
import cv2
import time
from pynput import keyboard
import pyautogui

# İzlemek istediğiniz bölgenin koordinatları (sol üst x, sol üst y, sağ alt x, sağ alt y)
watch_region = (870, 100, 1050, 120)
threshold = 100  # Algılama hassasiyeti için eşik değeri

# Önceki ekran görüntüleri
previous_images = [None, None, None]

# Q tuşuna basılı olduğunu kontrol eden değişken
q_key_pressed = False
flag_clicked = False

# Kaydedilen konumlar
saved_positions = []

def on_key_press(key):
    global q_key_pressed, saved_positions
    try:
        if key.char == 'q':
            if not q_key_pressed:
                q_key_pressed = True
                print("Q tuşuna basıldı! q_key_pressed:", q_key_pressed)
        elif key.char == 'z':
            if not q_key_pressed:
                saved_positions.append(pyautogui.position())
                print(f"Konum kaydedildi: {pyautogui.position()}")
        elif key.char == 'x':
            if not q_key_pressed:
                print("Tıklamalar başlıyor...")
                time.sleep(2)  # İstediğiniz bekleme süresi
                for position in saved_positions:
                    pyautogui.click(position)
                    print(f"Tıklandı: {position}")
                print("Tıklamalar tamamlandı.")
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
    global previous_images, flag_clicked
    
    screenshot = ImageGrab.grab(bbox=watch_region)
    current_image = np.array(screenshot)
    
    if previous_images[0] is not None:
        differences = [np.sum(current_image != prev_image) for prev_image in previous_images]
        
        # Eğer son 3 ekran görüntüsü arasında fark varsa, değişiklik algıla
        if any(diff > threshold for diff in differences) and not flag_clicked:
            # Tıklama işlemini gerçekleştir
            pyautogui.click(322, 17)
            pyautogui.click(137, 12)
            print("Değişiklik tespit edildi!")
            flag_clicked = True
    
    previous_images.pop(0)
    previous_images.append(current_image)

def main():
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        while True:
            # Q tuşuna basılıysa, bekleme süresxi boyunca algılamayı atla
            if q_key_pressed:
                time.sleep(1)
                continue

            check_for_changes()
            
    
    listener.join()

if __name__ == "__main__":
    main()
