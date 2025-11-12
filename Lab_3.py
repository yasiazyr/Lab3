import tkinter as tk
import random
import string

def set_background_image(root):
        bg_image = tk.PhotoImage(file="gardenscapes.png")
        bg_label = tk.Label(root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_image  # сохраняем ссылку

def init_frames(root):
    # Главный фрейм
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Фрейм для отображения ключа
    key_frame = tk.Frame(main_frame)
    key_frame.pack(pady=20)

    # Фрейм для ввода числа
    input_frame = tk.Frame(main_frame)
    input_frame.pack(pady=10)

    # Фрейм для кнопки
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)

    return main_frame, key_frame, input_frame, button_frame


def init_input(input_frame, button_frame, key_frame):
    # Поле для ввода трехзначного числа
    number_label = tk.Label(input_frame, text="Введите 3-значное число:", font=("Arial", 12))
    number_label.pack(side=tk.LEFT, padx=5)

    number_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
    number_entry.pack(side=tk.LEFT, padx=5)

    # Поле для отображения сгенерированного ключа
    key_label = tk.Label(key_frame, text="Ключ будет здесь:", font=("Arial", 10))
    key_label.pack()

    key_display = tk.Label(key_frame, text="XXXXX-XXXX-XXX-XX", font=("Courier", 14, "bold"),
                           bg="white", relief=tk.SUNKEN, width=20)
    key_display.pack(pady=10)

    def generate_key():
        number = number_entry.get()

        # Проверка ввода
        if len(number) != 3 or not number.isdigit():
            key_display.config(text="Ошибка: введите 3 цифры!", fg="red")
            return

        # Генерация ключа
        key = generate_key_algorithm(number)
        key_display.config(text=key, fg="black")

    # Кнопка генерации
    generate_btn = tk.Button(button_frame,
                             text="Сгенерировать ключ",
                             command=generate_key,
                             font=("Arial", 12),
                             bg="#4CAF50",
                             fg="white")
    generate_btn.pack(pady=10)

    return number_entry, key_display


def generate_key_algorithm(number):
    # Алфавит для генерации
    alphabet = string.ascii_uppercase + string.digits  # A-Z и 0-9

    # Генерация первого блока (5 случайных символов)
    first_block = ''.join(random.choices(alphabet, k=5))
    key_parts = [first_block]

    current_string = first_block

    # Генерация остальных блоков с сдвигом
    for i, shift_digit in enumerate(number):
        shift = int(shift_digit)

        # Удаляем один символ
        current_string = current_string[:-1]

        # Применяем сдвиг (чередуем направление)
        if i % 2 == 0:  # Четный индекс - сдвиг вправо
            shifted_string = shift_right(current_string, shift, alphabet)
        else:  # Нечетный индекс - сдвиг влево
            shifted_string = shift_left(current_string, shift, alphabet)

        key_parts.append(shifted_string)
        current_string = shifted_string

    return '-'.join(key_parts)


def shift_right(text, shift, alphabet):
    """Сдвиг символов вправо"""
    result = []
    for char in text:
        current_index = alphabet.index(char)
        new_index = (current_index + shift) % len(alphabet)
        result.append(alphabet[new_index])
    return ''.join(result)


def shift_left(text, shift, alphabet):
    """Сдвиг символов влево"""
    result = []
    for char in text:
        current_index = alphabet.index(char)
        new_index = (current_index - shift) % len(alphabet)
        result.append(alphabet[new_index])
    return ''.join(result)


def set_background_image(root):
    # Здесь можно добавить фон-картинку
    # Для примера просто установим цвет фона
    root.configure(bg='#f0f0f0')


def init_gui():
    root = tk.Tk()
    root.geometry('600x400')
    root.title('KeyGen - Генератор ключей')

    # Устанавливаем фон
    set_background_image(root)

    # Инициализируем фреймы
    frames = init_frames(root)

    # Инициализируем элементы ввода
    init_input(frames[2], frames[3], frames[1])

    root.mainloop()
    return root


if __name__ == '__main__':
    init_gui()