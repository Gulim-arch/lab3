def gronsfeld_cipher(message, key, encrypt=True):
    message = message.replace(" ", "").upper()
   
    key = [int(digit) for digit in str(key)]
    
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    n = len(alphabet)
    
    result_message = ""
    
    for i, char in enumerate(message):
        if char in alphabet:

            old_index = alphabet.index(char)
            
            shift = key[i % len(key)]
            
            if encrypt:
                new_index = (old_index + shift) % n
            else:
                new_index = (old_index - shift) % n
            
            result_message += alphabet[new_index]
        else:
            result_message += char
    
    return result_message

message = input("Введите сообщение для шифрования: ")
key = input("Введите числовой ключ: ")

encrypted_message = gronsfeld_cipher(message, key, encrypt=True)
print("Зашифрованное сообщение:", encrypted_message)

decrypt_message = input("Введите сообщение для дешифрования: ")

decrypted_message = gronsfeld_cipher(decrypt_message, key, encrypt=False)
print("Расшифрованное сообщение:", decrypted_message)
