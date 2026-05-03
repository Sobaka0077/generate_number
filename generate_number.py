import tkinter as tk
from tkinter import messagebox
import random

def generate_number():
    """Генерирует случайное число в заданном диапазоне."""
    # Получаем значения из полей ввода
    min_value = entry_min.get()
    max_value = entry_max.get()
    
    # Проверка, что поля не пустые
    if not min_value or not max_value:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните оба поля!")
        return
    
    try:
        # Преобразуем в целые числа
        min_num = int(min_value)
        max_num = int(max_value)
        
        # Проверка, что min <= max
        if min_num > max_num:
            messagebox.showerror("Ошибка", "Минимальное значение не может быть больше максимального!")
            return
        
        # Генерация случайного числа
        random_number = random.randint(min_num, max_num)
        
        # Вывод результата
        label_result.config(text=f"Случайное число: {random_number}")
        
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа!")

# Создаем главное окно
root = tk.Tk()
root.title("Генератор случайных чисел")
root.geometry("400x250")
root.resizable(False, False)

# Создаем и размещаем виджеты
label_min = tk.Label(root, text="Минимум:", font=("Arial", 12))
label_min.pack(pady=(20, 5))

entry_min = tk.Entry(root, font=("Arial", 12), width=20)
entry_min.pack()

label_max = tk.Label(root, text="Максимум:", font=("Arial", 12))
label_max.pack(pady=(10, 5))

entry_max = tk.Entry(root, font=("Arial", 12), width=20)
entry_max.pack()

# Кнопка генерации
button_generate = tk.Button(
    root, 
    text="Сгенерировать", 
    font=("Arial", 12), 
    command=generate_number,
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5
)
button_generate.pack(pady=20)

# Метка для вывода результата
label_result = tk.Label(root, text="Результат будет здесь", font=("Arial", 14, "bold"), fg="blue")
label_result.pack(pady=10)

# Запускаем главный цикл
root.mainloop()