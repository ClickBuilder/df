import os
import json
import time
import datetime
import requests
import schedule
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# === Конфиг ===
CLIENT_ID = 'd7qjv3b1wqn5ekuwugniqpgmgh8i4o'
CLIENT_SECRET = 'hmwywm45op4cz46yirhwoqsuezzhop'
USERNAME = 'tijoe'
DATA_FILE = 'watch_log.json'
GRAPH_FILE = 'watch_graph.png'
FIREFOX_PROFILE_DIR = '/home/wex/.mozilla/firefox/eujkloxz.default'  # твой профиль

# === Получить OAuth токен ===
def get_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    resp = requests.post(url, params=params)
    resp.raise_for_status()
    return resp.json()['access_token']

# === Проверка стрима через Twitch API ===
def is_stream_live(token):
    url = f'https://api.twitch.tv/helix/streams?user_login={USERNAME}'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    print(f"[DEBUG] Twitch API response: {data}")
    return len(data['data']) > 0

# === Логирование ===
def log_watch(session_time):
    entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'duration_min': session_time
    }

    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    data.append(entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# === Построение графика ===
def generate_graph():
    if not os.path.exists(DATA_FILE):
        print("[!] Нет данных для построения графика.")
        return

    with open(DATA_FILE) as f:
        data = json.load(f)

    times = [datetime.datetime.fromisoformat(e['timestamp']) for e in data]
    durations = [e['duration_min'] for e in data]

    plt.figure(figsize=(10, 5))
    plt.plot(times, durations, label='Minutes Watched')
    plt.xlabel('Time')
    plt.ylabel('Minutes Watched')
    plt.title('Twitch Watch Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(GRAPH_FILE)
    print(f'[+] График сохранён: {GRAPH_FILE}')

# === Главный демон ===
def run_watcher():
    print("[*] Демон запущен... проверка каждые 5 минут")
    session_minutes = 0

    def check():
        nonlocal session_minutes
        token = get_access_token()
        if is_stream_live(token):
            session_minutes += 5
            print(f"[+] Стрим активен: +5 минут (сессия: {session_minutes} мин)")
            log_watch(5)
        else:
            if session_minutes > 0:
                print(f"[-] Стрим завершён. Итоговая сессия: {session_minutes} минут.")
                session_minutes = 0
            else:
                print("[ ] Стрим не в эфире.")

    schedule.every(5).minutes.do(check)
    check()  # первая проверка сразу

    while True:
        schedule.run_pending()
        time.sleep(60)

# === Точка входа ===
if __name__ == '__main__':
    if not os.path.exists(FIREFOX_PROFILE_DIR):
        print(f"[!] Путь профиля Firefox не найден: {FIREFOX_PROFILE_DIR}")
        exit(1)

    try:
        run_watcher()
    except KeyboardInterrupt:
        print("\n[!] Остановлено пользователем.")
        generate_graph()

