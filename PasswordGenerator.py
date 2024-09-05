import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random
import string


def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите корректное значение длины пароля!")
        return

    if length < 8:
        messagebox.showwarning("Ошибка", "Минимальная длина пароля должна быть 8 символов!")
        return

    characters = string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if numbers_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    update_password_strength(password)


def update_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = length
    if has_upper:
        score += 2
    if has_digit:
        score += 2
    if has_special:
        score += 2

    if score < 12:
        strength_label.config(text="Сложность: Низкая", fg="red")
    elif 12 <= score < 16:
        strength_label.config(text="Сложность: Средняя", fg="orange")
    else:
        strength_label.config(text="Сложность: Высокая", fg="green")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена!")


def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text="Показать")
    else:
        password_entry.config(show='')
        toggle_button.config(text="Скрыть")


# Создание основного окна
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#2E4053")

# Заголовок
title_label = tk.Label(root, text="Генератор паролей", font=("Helvetica", 16, "bold"), bg="#2E4053", fg="#ECF0F1")
title_label.pack(pady=10)

# Поле для ввода длины пароля
length_frame = tk.Frame(root, bg="#2E4053")
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Длина пароля:", font=("Helvetica", 12), bg="#2E4053", fg="#ECF0F1")
length_label.pack(side=tk.LEFT, padx=10)

length_var = tk.StringVar(value="12")
length_entry = tk.Entry(length_frame, textvariable=length_var, width=5)
length_entry.pack(side=tk.LEFT, padx=10)

# Флажки для параметров пароля
options_frame = tk.Frame(root, bg="#2E4053")
options_frame.pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

uppercase_check = tk.Checkbutton(options_frame, text="Заглавные буквы", variable=uppercase_var, bg="#2E4053", fg="#ECF0F1", selectcolor="#2E4053")
uppercase_check.pack(anchor=tk.W)

numbers_check = tk.Checkbutton(options_frame, text="Цифры", variable=numbers_var, bg="#2E4053", fg="#ECF0F1", selectcolor="#2E4053")
numbers_check.pack(anchor=tk.W)

special_check = tk.Checkbutton(options_frame, text="Спецсимволы", variable=special_var, bg="#2E4053", fg="#ECF0F1", selectcolor="#2E4053")
special_check.pack(anchor=tk.W)

# Поле для отображения пароля
password_frame = tk.Frame(root, bg="#2E4053")
password_frame.pack(pady=10)

password_entry = tk.Entry(password_frame, font=("Helvetica", 14), width=24, justify="center", bg="#ECF0F1", fg="#2E4053", show='*')
password_entry.pack()

# Кнопка для изменения видимости пароля
toggle_button = tk.Button(password_frame, text="Показать", command=toggle_password_visibility, bg="#5DADE2", fg="white",
                         font=("Helvetica", 12), relief="raised", bd=3)
toggle_button.pack(pady=5)

# Индикатор сложности пароля
strength_label = tk.Label(root, text="Сложность: ", font=("Helvetica", 12), bg="#2E4053", fg="#ECF0F1")
strength_label.pack(pady=5)

# Кнопки
button_frame = tk.Frame(root, bg="#2E4053")
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Сгенерировать", command=generate_password, bg="#5DADE2", fg="white",
                            font=("Helvetica", 12), relief="raised", bd=3)
generate_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Копировать", command=copy_to_clipboard, bg="#5DADE2", fg="white",
                        font=("Helvetica", 12), relief="raised", bd=3)
copy_button.pack(side=tk.LEFT, padx=10)

# Запуск основного цикла приложения
root.mainloop()
