def simple_transposition_cipher(message):
    rows, cols = 5, 7

    # Удаляем пробелы и переводим текст в верхний регистр
    message = message.replace(" ", "").upper()

    # Создаем пустую таблицу
    table = [[""] * cols for _ in range(rows)]
    index = 0

    # Заполняем таблицу по столбцам
    for c in range(cols):
        for r in range(rows):
            if index < len(message):
                table[r][c] = message[index]
                index += 1
            else:
                table[r][c] = " " 

    # Формируем зашифрованное сообщение
    encrypted_message = ""
    for row in table:
        encrypted_message += "".join(row)

    # Разбиваем сообщение на группы по 5 символов
    grouped_message = " ".join([encrypted_message[i:i+5] for i in range(0, len(encrypted_message), 5)])

    return grouped_message


def simple_transposition_decrypt(encrypted_message):
    rows, cols = 5, 7

    # Удаляем пробелы из зашифрованного сообщения
    encrypted_message = encrypted_message.replace(" ", "")

    # Создаем пустую таблицу
    table = [[""] * cols for _ in range(rows)]
    index = 0

    # Заполняем таблицу по строкам
    for r in range(rows):
        for c in range(cols):
            if index < len(encrypted_message):
                table[r][c] = encrypted_message[index]
                index += 1

    # Формируем расшифрованное сообщение
    decrypted_message = ""
    for c in range(cols):
        for r in range(rows):
            decrypted_message += table[r][c] 

    # Удаляем лишние пробелы
    decrypted_message = decrypted_message.rstrip()

    return decrypted_message


# Основная часть программы
message = input("Введите сообщение для шифрования: ")
encrypted_message = simple_transposition_cipher(message)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = simple_transposition_decrypt(encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
