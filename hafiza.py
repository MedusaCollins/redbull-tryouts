import pyautogui
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
screenshot_region = (738, 177, 1201 - 738, 252 - 177)

lauda = (1128,665)
yuksek = (1128,665)
alcak = (1128,665)
hizli = (1128,665)
yavas = (1128,665)
redbull = (1128,665)
pit = (1128,665)
tespit = (1128,665)
drs = (1128,665)


yavas = (784, 480)
pit = (1127, 652)
yuksek = (811, 477)
hizli = (834, 548)
drs = (1121, 623)

harita_kareler = {
    #Lauda viraji
    "LAUDA ViRAJI": (lauda, "Lauda Virajına tıklandı!"),

    #Pistteki en yüksek nokta
    "PISTTEKi YUKSEK NOKTA": (yuksek, "Pistteki Yüksek Nokta tıklandı!"),
    "PISTTEKI EN YUKSEK NOK TA": (yuksek, "Pistteki Yüksek Nokta tıklandı!"),
    "STTEKi YUKSEK NOKT#": (yuksek, "Pistteki Yüksek Nokta tıklandı!"),
    "STTEKi EN YUKSEK NOKTS": (yuksek, "Pistteki Yüksek Nokta tıklandı!"),

    #Pistteki en alçak nokta
    "PISTTEKI EN ALCAK NOKTA": (alcak, "Pistteki En alçak tıklandı!"),
    "PiSTTEKi ALCGAK NOK'TA": (alcak, "Pistteki en alçak tıklandı!"),
    "PiISTTEKi ALCAK NOK'TA": (alcak, "Pistteki en alçak tıklandı!"),
    "PiSTTEKi ALCGAK NOKTA": (alcak, "Pistteki en alçak tıklandı!"),
    "PiISTTEKi ALCGAK NOKTA": (alcak, "Pistteki en alçak tıklandı!"),
    "iSTTEKi ALCGAK NOKTA": (alcak, "Pistteki en alçak tıklandı!"),
    "iSTTEKi EN ALGAK NOKTA": (alcak, "Pistteki en alçak tıklandı!"),

    #En Hızlı Viraj
    "EN HIZLI VIRAJ": (hizli, "EN HIZLI VIRAJ tıklandı!"),
    "EN HIZLI ViRAJ": (hizli, "EN HIZLI VIRAJ tıklandı!"),

    #En Yavaş Viraj
    "EN YAVAS VIRAJ": (yavas, "Yavaş viraj tıklandı!"), 
    "YAVAS ViRAJ": (yavas, "Yavaş viraj tıklandı!"), 
    "EN YAVAS ViIRAJ": (yavas, "Yavaş viraj tıklandı!"), 

    #Redbull Ana Tribünü
    "RED BULL ANA TRIBUNU": (redbull, "RED BULL ANA TRIBUNU tıklandı!"),

    #Pit Girişi
    "PIT airigi": (pit, "PIT girişi tıklandı!"),
    "PIT amigi": (pit, "PIT girişi tıklandı!"),
    "PIT GiRisi": (pit, "PIT girişi tıklandı!"),
    "PIT GiRiSi": (pit, "PIT girişi tıklandı!"),

    #Hız Tespiti
    "HIiZ TESPITi": (tespit, "HIiZ TESPITi tıklandı!"), 
    "HIZ TESPITi": (tespit, "HIiZ TESPITi tıklandı!"),

    #Drs Başlangıç Noktası #1
    "DRS BASLANGIC NOKTASI #1": (drs, "DRS BASLANGIC NOKTASI #1 tıklandı!"),
    "2S BASLANGIC NOKTAS!I #:": (drs, "DRS BASLANGIC NOKTASI #1 tıklandı!"),
    "2S BASLANGIC NOKTASI #:": (drs, "DRS BASLANGIC NOKTASI #1 tıklandı!")
}

while True:
    screenshot = pyautogui.screenshot(region=screenshot_region)
    detected_texts = pytesseract.image_to_string(screenshot).strip().splitlines()

    for detected_text in detected_texts:
        if detected_text in harita_kareler:
            (x, y), message = harita_kareler[detected_text]
            if x != 0 and y != 0:
                pyautogui.moveTo(x, y)
                pyautogui.click()
            print(message)
            detected_texts.remove(detected_text)

    if detected_texts:
        print("Algılanan metinler:", detected_texts)
    else:
        print("Yazı bulunmuyor.")
    time.sleep(0.01)
