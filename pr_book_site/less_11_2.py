#ПЕРЕХОД НА СЛЕДУЮЩИЮ СТРАНИЦУ ЦЕРЕЗ a d в eng розкладке
#ПЕРЕХОД НА СЛЕДУЮЩИЮ СТРАНИЦУ ЦЕРЕЗ a d в eng розкладке
#ПЕРЕХОД НА СЛЕДУЮЩИЮ СТРАНИЦУ ЦЕРЕЗ a d в eng розкладке
#ПЕРЕХОД НА СЛЕДУЮЩИЮ СТРАНИЦУ ЦЕРЕЗ a d в eng розкладке


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


folder = 'downloaded_images'

# Создаем папку, если она не существует
if not os.path.exists(folder):
    os.makedirs(folder)



def get_books(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    books = soup.find_all('article', class_='product_pod')

    img_paths = []
    book_info = []
    for book in books:
        #название книги
        title = book.find('h3').find('a')['title']
        # ценa
        price = book.find('p', class_='price_color').text

        img_tag = book.find('img')
        img_url = img_tag.get('src')
        img_url = urljoin(base_url, img_url)  # Преобразуем в абсолютный путь
        img_name = os.path.basename(img_url)
        img_data = requests.get(img_url).content

        img_path = os.path.join(folder, img_name)
        with open(img_path, 'wb') as f:
            f.write(img_data)
        img_paths.append(img_path)
        book_info.append((title, price))

    return img_paths, book_info


#удаления фото
def delete_images(img_paths):
    for img_path in img_paths:
        if os.path.exists(img_path):
            os.remove(img_path)



current_page = 1
img_paths = []
book_info = []


root = Tk()
root.title("Скачанные книги и изображения")

# Основной контейнер для всех элементов
main_frame = Frame(root)
main_frame.pack(padx=10, pady=10)



def show_images():
    # Очистка старых изображений
    for widget in main_frame.winfo_children():
        widget.destroy()


    row = 0
    column = 0
    for i in range(len(img_paths)):
        img = Image.open(img_paths[i])
        img = img.resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)

        # Создаем виджет Label для изображения
        image_label = Label(main_frame, image=img_tk)
        image_label.grid(row=row, column=column, padx=5, pady=5)
        image_label.image = img_tk

        # Создаем метку для названия книги
        title_label = Label(main_frame, text=book_info[i][0], font=('Arial', 10), wraplength=150)
        title_label.grid(row=row + 1, column=column, padx=5, pady=5)


        price_label = Label(main_frame, text=book_info[i][1], font=('Arial', 10))
        price_label.grid(row=row + 2, column=column, padx=5, pady=5)


        column += 1
        if column >= 3:
            column = 0
            row += 3
def next_page(event=None):
    global current_page, img_paths, book_info
    current_page += 1
    delete_images(img_paths)
    img_paths, book_info = get_books(current_page)
    show_images()


def prev_page(event=None):
    global current_page, img_paths, book_info
    if current_page > 1:
        current_page -= 1
        delete_images(img_paths)
        img_paths, book_info = get_books(current_page)
        show_images()

button_prev = Button(root, text="Предыдущая страница", command=prev_page)
button_prev.pack(side="left", padx=10, pady=10)
button_next = Button(root, text="Следующая страница", command=next_page)
button_next.pack(side="right", padx=10, pady=10)
img_paths, book_info = get_books(current_page)
show_images()
root.bind('a', prev_page)  #на предыдущую страницу
root.bind('d', next_page)  #следующую страницу
root.bind('ф', prev_page)  #предыдущую страницу
root.bind('в', next_page)  #следующую страницу


root.mainloop()
