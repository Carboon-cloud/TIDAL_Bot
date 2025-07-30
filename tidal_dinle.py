import pyautogui
import pyperclip
import time
import random
import os

TIDAL_EXE = r"C:\Users\Administrator\AppData\Local\TIDAL\TIDAL.exe"

EMAIL = {1: "comsir@ccqu.top",
         2: "43l5mln222@xkxkud.com",
         3: "womexo9659@ofacer.com"}

PASSWORD = "4rfv3edc"

def get_random_playlist(): 
    return random.choice(PLAYLISTS)

def open_tidal():
    os.startfile(TIDAL_EXE) 
    time.sleep(10)

    
# --- Playlistler --- #

def play_gas_station_vibes():
    playlist = "Gas Station Vibes"
    print(f">>> Playlist aranıyor: {playlist}")
    pyautogui.click(800, 80, duration=1)
    pyautogui.write(playlist)
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.click(400, 80, duration=1)
    time.sleep(3)
    pyautogui.click(600, 125, duration=1)  
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(400, 300, duration=2)
    time.sleep(2)
    pyautogui.click(600, 430, duration=2)

    
def play_deep_chill():
    playlist = "Deep Chill 24/7"
    print(f">>> Playlist aranıyor: {playlist}")
    pyautogui.click(800, 80, duration=1)
    pyautogui.write(playlist)
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.click(400, 80, duration=1)
    time.sleep(3)
    pyautogui.click(700, 125, duration=1)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(400, 300, duration=2)
    time.sleep(2)
    pyautogui.click(600, 430, duration=2)


def play_slow_mood_radio():
    playlist = "Slow Mood Radio"
    print(f">>> Playlist aranıyor: {playlist}")
    pyautogui.click(800, 80, duration=1)
    pyautogui.write(playlist)
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.click(400, 80, duration=1)
    time.sleep(3)
    pyautogui.click(700, 125, duration=1)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(400, 300, duration=2)
    time.sleep(2)
    pyautogui.click(600, 430, duration=2)

    
def play_deep_echo_room():
    playlist = "Deep Echo Room"
    print(f">>> Playlist aranıyor: {playlist}")
    pyautogui.click(800, 80, duration=1)
    pyautogui.write(playlist)
    time.sleep(4)
    pyautogui.press("enter")
    pyautogui.click(400, 80, duration=1)
    time.sleep(3)
    pyautogui.click(700, 125, duration=1)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(400, 300, duration=2)
    time.sleep(2)
    pyautogui.click(600, 430, duration=2)

    
# --- Diğer Fonksiyonlar ---

def search_and_play_playlist():
    playlist = get_random_playlist()
    print(f">>> Playlist aranıyor: {playlist}")
    if playlist in PLAYLIST_ACTIONS:
        PLAYLIST_ACTIONS[playlist]()
    else:
        print(f"Playlist '{playlist}' için bir aksiyon tanımlanmamış.")
        
def music_like(duration_minutes=2):
    pyautogui.click(1015, 600, duration=1)
    time.sleep(2)

    elapsed = 0 
    like_interval = 10
    special_click_interval = 60  # 1 dakika

    next_special_click = special_click_interval
    y_positions = [600, 550, 500, 450, 400, 360, 310, 260]

    while elapsed < duration_minutes * 60:
        pyautogui.click(950, random.choice(y_positions), duration=1)
        time.sleep(like_interval)
        elapsed += like_interval

        if elapsed >= next_special_click:
            print(f"{elapsed // 60} dakika geçti, özel tıklama yapılıyor...")
            pyautogui.click(1015, 600, duration=1)
            next_special_click += special_click_interval

        print(f"Beğenme süresi: {elapsed // 60} dk {elapsed % 60} sn")

        
def listen_playlist_for(hours):
    seconds = hours * 60 * 60
    print(f">>> Dinlenme süresi belirlendi: {hours} saat")

    elapsed = 0
    shuffle_interval = 3600  # 1 saat
    special_click_interval = 1800
    next_shuffle_time = shuffle_interval
    next_special_click = special_click_interval

    y_positions = [590, 540, 450, 490, 400, 350, 300, 250]

    while elapsed < seconds:
        pyautogui.click(950, random.choice(y_positions), duration=1)
        time.sleep(10)
        elapsed += 10

        if elapsed >= next_shuffle_time:
            print(f">>> {elapsed // 3600}. saat: Shuffle butonuna tıklanıyor.")
            pyautogui.click(600, 430, duration=1)
            next_shuffle_time += shuffle_interval
                 
        if elapsed >= next_special_click:
            pyautogui.click(750, 150, duration=1)
            next_special_click += special_click_interval

        print(f"   Geçen süre: {elapsed // 3600} saat {elapsed // 60 % 60} dakika {elapsed % 60} saniye")


        
def logout_user():
    pyautogui.click(100, 120, duration=1)
    time.sleep(4)
    pyautogui.click(200, 60, duration=1)
    time.sleep(2)
    pyautogui.click(250, 300, duration=1)  # Logout butonu
    time.sleep(10)
    
def login_user(email):
    pyautogui.click(950, 85, duration=1)
    time.sleep(20)
    pyautogui.click(455, 350, duration=1)
    pyperclip.copy(email)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)
    pyautogui.click(455, 420, duration=1)
    time.sleep(2)
    pyautogui.write(PASSWORD, interval=0.1)
    time.sleep(5)
    pyautogui.click(455, 500, duration=1)
    time.sleep(5)
    
        
PLAYLIST_ACTIONS = {
    "Gas Station Vibes": play_gas_station_vibes,
    "Deep Chill 24/7": play_deep_chill,
    "Slow Mood Radio": play_slow_mood_radio,
    "Deep Echo Room": play_deep_echo_room
}

PLAYLISTS = list(PLAYLIST_ACTIONS.keys())

def run_multi_user_rotation():
    while True:
        user_list = list(EMAIL.values())
        random.shuffle(user_list)

        for user in user_list:
            print(f">>> Kullanıcı: {user} ile oturum açılıyor...")
            open_tidal()
            login_user(user)
            search_and_play_playlist()
            music_like()
            listen_playlist_for(random.randint(5, 8)) 
            logout_user()

        
if __name__ == "__main__":
    run_multi_user_rotation()
    print("Program sonlandı.")

        
