import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import sqlite3

# URL
url = "https://meteo.ua/31/jitomir"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    weather_div = soup.find('div', class_='page-header-info__title')

    if weather_div:
        #div
        weather_info = weather_div.get_text(strip=True)
        print(f"{weather_info}")

        temperature_match = re.search(r'-?\d+ °C', weather_info)
        if temperature_match:
            temperature = temperature_match.group(0)
            print(f"Температура: {temperature}")
        else:
            print("Не удалось найти информацию о температуре.")
            temperature = None

        # Получаем текущую дату и время
        current_date = datetime.now().strftime("%Y-%m-%d")  #дата
        current_time = datetime.now().strftime("%H:%M:%S")  #время
        print(f"Текущая дата: {current_date}")
        print(f"Текущее время: {current_time}")


        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()


        cursor.execute("PRAGMA table_info(weather);")
        columns = cursor.fetchall()
        expected_columns = {"id", "temperature", "date", "time"}
        existing_columns = {col[1] for col in columns}


        if existing_columns != expected_columns:
            cursor.execute("DROP TABLE IF EXISTS weather;")
            conn.commit()
            existing_columns = set()

        # Создаем таблицу
        if not existing_columns:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature TEXT,
                    date TEXT,
                    time TEXT
                )
            ''')
            conn.commit()


        cursor.execute('''
            INSERT INTO weather (temperature, date, time)
            VALUES (?, ?, ?)
        ''', (temperature, current_date, current_time))

        # Сохраняем изменения
        conn.commit()


        cursor.execute('SELECT * FROM weather')
        rows = cursor.fetchall()
        print("\nДанные из таблицы:")
        for row in rows:
            print(row)

        conn.close()

        print("")
    else:
        print("Не удалось найти информацию о погоде.")
else:
    print(f"Не удалось получить страницу. Статус код: {response.status_code}")
