import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import sqlite3

# URL страницы
url = "https://meteo.ua/31/jitomir"

# Делаем GET-запрос
response = requests.get(url)

# Проверяем статус код ответа
if response.status_code == 200:
    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем div с классом page-header-info__title
    weather_div = soup.find('div', class_='page-header-info__title')

    if weather_div:
        # Получаем текст из div
        weather_info = weather_div.get_text(strip=True)
        print(f"{weather_info}")

        # Используем регулярное выражение для извлечения температуры
        temperature_match = re.search(r'-?\d+ °C', weather_info)
        if temperature_match:
            temperature = temperature_match.group(0)
            print(f"Температура: {temperature}")
        else:
            print("Не удалось найти информацию о температуре.")
            temperature = None

        # Получаем текущую дату и время
        current_date = datetime.now().strftime("%Y-%m-%d")  # Текущая дата
        current_time = datetime.now().strftime("%H:%M:%S")  # Текущее время

        print(f"Текущая дата: {current_date}")
        print(f"Текущее время: {current_time}")

        # Подключаемся к базе данных SQLite
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()

        # Проверяем существование таблицы и её структуру
        cursor.execute("PRAGMA table_info(weather);")
        columns = cursor.fetchall()
        expected_columns = {"id", "temperature", "date", "time"}
        existing_columns = {col[1] for col in columns}

        # Удаляем таблицу, если структура не совпадает
        if existing_columns != expected_columns:
            cursor.execute("DROP TABLE IF EXISTS weather;")
            conn.commit()
            existing_columns = set()

        # Создаем таблицу, если она еще не существует
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

        # Вставляем данные в таблицу
        cursor.execute('''
            INSERT INTO weather (temperature, date, time)
            VALUES (?, ?, ?)
        ''', (temperature, current_date, current_time))

        # Сохраняем изменения
        conn.commit()

        # Извлекаем все данные из таблицы и выводим их
        cursor.execute('SELECT * FROM weather')
        rows = cursor.fetchall()
        print("\nДанные из таблицы:")
        for row in rows:
            print(row)

        # Закрываем соединение с базой данных
        conn.close()

        print("")
    else:
        print("Не удалось найти информацию о погоде.")
else:
    print(f"Не удалось получить страницу. Статус код: {response.status_code}")
