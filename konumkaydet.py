import keyboard
import pyautogui
import pytesseract
from PIL import Image
import re

pyautogui.FAILSAFE = False
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract yolunu düzenleyin

# Kare koordinatları
x1, y1, x2, y2 = 697, 194, 1225, 226

# Metin varyasyonları için sözlük
text_variations = {
    "lauda": ["LAUDA ViRAJI"],
    "yuksek": ["PISTTEKi EN YUKSEK NOKTA", "PISTTEKi YUKSEK NOKTA", "PISTTEKI EN YUKSEK NOK TA", "STTEKi YUKSEK NOKT#", "Pistteki Yüksek Nokta"],
    "alcak": ["PISTTEKi EN ALGAK NOKTA", "PISTTEKI EN ALCAK NOKTA", "PiSTTEKi ALCGAK NOK'TA", "PiISTTEKi ALCAK NOK'TA", "PiSTTEKi ALCGAK NOKTA", "PiISTTEKi ALCGAK NOKTA", "iSTTEKi ALCGAK NOKTA"],
    "hizli": ["EN HIZLI VIRAJ", "EN HIZLI ViIRAJ"],
    "yavas": ["EN YAVAS VIRAJ", "YAVAS ViRAJ"],
    "redbull": ["RED BULL ANA TRIBUNU"],
    "pit": ["pit girişi", "pit girisi", "pit", "pits", "pitstop", "PIT GiRisi", "PIT amigi", "PIT airigi"],
    "tespit": ["HIiZ TESPITi", "HIZ TESPITi"],
    "drs": ["DRS BASLANGIC NOKTASI #1", "2S BASLANGIC NOKTAS!I #:", "DRS BASLANGIC NOK'TASI #2", "DRS BASLANGIC NOK'TASI #12"]
}

recorded_positions = {}
is_recording = False

def format_point(point):
    return f"{point[0]}, {point[1]}"

def record_mouse_position():
    global recorded_positions, is_recording
    if is_recording:
        return

    is_recording = True
    position = pyautogui.position()
    
    # Kare içerisindeki resmi yakala ve metni algıla
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    text = pytesseract.image_to_string(screenshot)
    
    if text.strip():
        for keyword, variations in text_variations.items():
            for variation in variations:
                if re.search(rf'\b{re.escape(variation)}\b', text, re.IGNORECASE):
                    text = keyword
                    recorded_positions[text] = (position[0], position[1])
                    break
        
    print("Mouse konumu kaydedildi:", position)
    print("Algılanan metin:", text)
    is_recording = False

def write_positions_to_console():
    print("\nKaydedilen metinler:")
    for text, position in recorded_positions.items():
        print(f'{text} = {position}')

keyboard.on_press_key("z", lambda event: record_mouse_position())
keyboard.on_press_key("x", lambda event: write_positions_to_console())

print("Z tuşuna basarak konumu kaydeder. X tuşuna basarak metinleri konsola yazdırır.")
print("Çıkmak için Esc tuşuna basın.")

while True:
    if keyboard.is_pressed("esc"):
        break

print("Program sonlandırıldı.")
