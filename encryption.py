# -*- coding: cp1251 -*-
import time


print('\n' 'Crypter Program 1.1.5 Public version, stable' '\n' 'by CISCer' '\n')
main_lyster = ' abcefghjklnopqdrystiuvmwxzABCSEFGHIJKLMDNXOPQRTUVWYZ4123568907ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБАяюэьыъщшчцхфутсрпонмлкйизжёедгвба.,/?;:<>!@#№$%^&*()-_=+{[]}'
symbols = ['№', '&', '-', ')', '%', '/', ']', ';', ':', '^', '>', ',', '+', '@', '*', '=', '{', '#', '[', '}', '(', '.', '$', '!', '_', '<', '?', ' ']

lyster_shuffle = ['/', '9', 'к', 'Ь', '^', 'c', 'O', 'ч', 'o', 'ь', 'П', 'Q', 'т', '!', 'Ю', 'р', 'Р', 'Z', 'Д', 'X', 'з', 'q', 'y', '_', '8', 'Ъ', ')', 'b', 'B', '№', 'Я', 'г', 'M', 'm', 'й', 'ъ', '@', 'О', 'Ы', 'К', 'U', '&', 'g', '}', '=', 'Ф', 'а', 'E', 'Т', 'ш', 'б', 'a', 'p', 'С', 'n', 'x', ',', 'ц', 'у', '%', 'r', 'ы', '7', 'j', 'V', 'ё', 'л', 'Ж', 'i', 'и', ' ', '>', 'щ', 'w', 'ф', 'Ц', 'Й', 'L', 'о', 'u', '0', 'я', 'с', 'А', 'd', '$', '2', 'J', 'В', 'P', '1', 'И', '-', 'Ё', '{', 'Л', '?', 'F', 'Х', '6', 'W', 'l', '*', 'D', 'н', 's', 'п', 'I', 'A', 'C', 'м', 'H', 'Б', 'М', 'З', ']', 'Щ', 'е', 'k', '5', 'G', 'в', '[', 'S', '+', 'R', 'T', 'e', 'K', 'f', '(', 'Г', 'х', 'ю', 'z', '3', 'Э', 'N', 'У', ';', '<', 'д', 'ж', '#', 'Y', 't', 'Ш', ':', 'э', '4', 'Ч', 'v', 'h', 'Е', 'Н', '.']
lyster_shuffle_def_null = ['{', '3', 'N', 's', 'Й', 'c', 'T', 'С', '^', 'О', '<', 'a', 'о', 'З', 'а', '9', 'M', 'V', 'w', '/', 'e', 'i', 'g', '>', 'l', ']', '4', 'p', 'Б', '5', 'е', '7', 'J', 'W', '}', '-', 'п', 'm', '@', 'q', 'K', '$', 'f', 'н', 'I', 'Ы', ';', 'р', 'Е', 'А', 'К', 'h', '0', 'И', 'S', '!', '6', 'd', 'z', 'ы', '(', 'ф', 'Щ', '[', '?', 'ъ', 'Д', 'и', 'ч', 'H', 'u', 'М', 'O', 'В', 'j', '*', 'o', 'k', 'Р', '2', 'ш', 'Ц', 'Y', '=', '1', 'Э', 't', 'U', 'Z', 'з', 'Н', '#', 'г', 'x', 'Ю', 'с', 'F', 'A', 'X', 'b', 'й', 'ь', 'Ч', 'П', 'к', 'в', '8', 'Г', '.', 'у', 'C', 'ж', 'Q', '+', 'Ъ', 'Х', '_', 'б', 'щ', 'Ё', 'х', 'ё', 'Л', 'д', 'ц', 'R', ':', 'м', ' ', 'У', 'Ж', ')', 'Ш', 'v', 'ю', 'P', 'я', 'L', ',', 'r', 'E', 'л', 'Ь', '%', '№', '&', 'B', 'G', 'D', 'Ф', 'y', 'т', 'Т', 'э', 'Я', 'n']
lyster_shuffle_def_eins = ['П', 'Й', 'Л', 'h', 'k', 'г', 'R', 'n', '?', 'Z', 's', 'ы', 'x', '@', 'F', ')', 'Щ', '{', '=', '^', 'r', 'm', 'V', 'п', 'я', '-', 'В', 'Ь', 'A', 'P', 'I', 'L', 'Ы', 'Ю', 'в', '2', '7', 'Я', 'б', '№', '0', 'ь', 'Р', 'H', 'i', 'y', 'C', 'р', 'ё', 'С', 'т', 'М', '+', 'w', 'Б', '[', 'O', 'Ш', 'х', 'о', 'с', 'a', 'н', '1', 'Ц', 'и', 'q', '9', 'U', '>', ',', 'А', 'Ф', 'e', 'v', 'N', '!', 'Т', 'ц', ':', 'Д', 'к', 'J', '#', '<', 'е', ';', '5', ']', 'z', 'Ж', 'f', 'b', 'Е', 'u', '%', '/', 'Ъ', 'd', 'у', 'ч', 'К', 'щ', 'ъ', 'ж', 'л', 'E', 'p', '6', '4', 'Г', 'д', 'з', 'м', 'K', '.', 'И', 'Ё', 'D', 'ф', 'j', 'Q', 'ш', '$', 'T', 'Х', '_', 'o', 'О', 'g', 'G', 'а', 'S', '*', ' ', 'З', 'У', '&', 'B', 'ю', '8', 'Н', 'X', 'Э', 'W', 'Y', 't', 'M', '}', '(', 'й', 'Ч', 'э', 'l', '3', 'c']
lyster_shuffle_def_zwei = ['п', 'H', 'с', 'A', 'ц', 'y', '_', 'П', '*', 'q', '№', '[', 'Щ', '@', '(', 'E', 'Y', 'e', 'Н', 'У', 'ю', 'и', 'n', '>', 'Й', '=', 'м', 'P', '8', 'S', 'j', '#', 'Q', 'C', 'Г', 'r', 'ф', 'R', 'т', 'в', '?', 'Ф', 'm', 'щ', '^', 'э', '!', 'u', ';', 'v', 'е', ']', 'U', 'д', 'Ш', 'Ъ', 'ъ', 'D', 'ё', '9', 'н', 's', 'c', 'з', '$', 'i', 'b', 'Ж', 'г', '1', '%', 'M', 'W', '-', 'z', 'Э', 'к', 'w', 'X', 'Т', '7', '&', 'T', '+', 'Z', 'x', 'О', '4', 'p', 'А', 'h', 'Л', 'Ь', 'K', 'ь', 'б', 'й', 'ы', '5', 'а', ')', '}', '/', '6', 'o', 'Ч', 'В', 'ч', 'К', '0', 'G', 'B', 'С', 'N', 'I', 't', 'F', 'Х', 'Р', 'f', ' ', 'l', 'V', '3', '<', 'Б', 'g', 'ш', 'р', 'a', 'O', '{', 'у', 'о', 'М', 'Ы', '2', 'Ё', 'З', ':', 'И', 'Д', 'k', '.', 'я', 'J', 'Ю', ',', 'L', 'ж', 'х', 'd', 'Ц', 'л', 'Я', 'Е']
lyster_shuffle_def_drei = ['z', '+', 'О', 'З', 'П', '$', 'п', 'H', 'e', 'В', 'э', 'j', 'n', 'y', 'ю', ',', 'd', 'i', 'r', 'k', 'щ', '!', 'g', 'Р', '>', 'Л', 'н', 'X', 'я', 'Q', 'b', 'Е', 'д', 'с', '6', '(', '.', '#', 'f', 'ы', '^', 'm', '}', 'Ю', '=', 'c', 'v', 'W', 'F', '5', 'б', 'Т', '@', '8', '9', 't', 'ф', 'Ё', 'р', 'D', 'Д', '[', 'х', 'T', 'Ь', 'м', '-', '{', 'R', 'Э', ' ', '4', 'o', 'Ч', 'А', 'т', 'Ы', 'Z', 'S', 'B', ']', 'з', 'И', 'Я', 'l', 'J', 'ъ', 'Н', 'h', 'о', 'x', 'K', 'е', 'O', 'у', 'а', '1', '0', 'Ж', '<', 'Й', 'Ш', '*', 'л', 'Х', 'Б', ')', 'ш', '%', 'Ф', 'г', 'Г', 'ч', 'M', 'М', 'G', 'C', 'ё', '/', '3', '7', 'N', ';', 'P', '2', 'U', 'a', 'к', '&', '№', 'I', 'К', 'С', 'E', 'ц', 'Ъ', 'й', 'ж', 'q', 'Y', 'в', '_', 'Щ', ':', 'V', 'ь', 'u', 'Ц', 'p', 'w', '?', 'У', 'и', 's', 'L', 'A']

mas_txt = '----- Start of correspondence -----''\n'     # Program start message


def StartApp():
    """" The main function responsible for the operation of the program """
    middle_message = ''
    crypto_2_message = ''
    crypto_3_message = ''

    print('\n' 'Encrypt - 1, Decipher - 2, Exit - 0' '\n' 'Encrypt/Decipher?')
    c_or_d = int(input('Change: '))    # Choice: encrypt, decrypt or exit
    if c_or_d == 0:     # Exit conditions
        quit()
    elif c_or_d > 2:
        print('-- Invalid change, try again, млTziЫY8^сDimР --')
        StartApp()
    n = int(input('Key: '))     # Encryption key

    oper_key = int(input('Oper key (0-4): '))   # Additional encryption key (choice from dictionaries)
    if oper_key == 0:
        d = lyster_shuffle
    elif oper_key == 1:
        d = lyster_shuffle_def_null
    elif oper_key == 2:
        d = lyster_shuffle_def_eins
    elif oper_key == 3:
        d = lyster_shuffle_def_zwei
    elif oper_key == 4:
        d = lyster_shuffle_def_drei
    else:
        print('-- Error "Oper key", restart --')    # If the selection fails, the program asks again
        oper_key = int(input('Oper key (0-4): '))

    print('Selected keys:', str(n) + ', ' + str(oper_key))      # Selected keys are shown
    time.sleep(1)   # 1 second delay

    print("\n" * 100)   # "Clearing" the terminal
    print(mas_txt)      # Program start message

    restart_program = 'Enter 0 to restart program'
    print(restart_program)  # A text prompting you to restart the program

    while True:     # Next in the loop is the input and output of messages
        if c_or_d == 1:     # Message encryption block
            s = input('- Message: ').strip()    # All characters from the user's keyboard are accepted for input
            if s == '0':
                print('\n''-- Restart --')
                StartApp()
            # Next comes 3-pass encryption
            for a in s:     # First pass
                middle_message += d[(d.index(a) - n) % len(d)]
            for b in middle_message:    # Second pass
                crypto_2_message += d[(d.index(b) - n) % len(d)]
            for c in crypto_2_message:  # Third pass
                crypto_3_message += d[(d.index(c) - n) % len(d)]

            print('- Encrypted in:', crypto_3_message, '\n')    # Outputting an encrypted message
            # Clearing all messages for subsequent correct work
            middle_message = ''
            crypto_2_message = ''
            crypto_3_message = ''

        elif c_or_d == 2:       # Block for decrypting messages
            s = input('- Decipher: ').strip()   # Принимаются на ввод все символы с клавиатуры пользователя
            if s == '0':        # Условие перезапуска программы
                print('\n''--Restart--')
                StartApp()
            # Next comes the decryption in 3 passes
            for a in s:    # First pass
                middle_message += d[(d.index(a) + n) % len(d)]
            for b in middle_message:    # Second pass
                crypto_2_message += d[(d.index(b) + n) % len(d)]
            for c in crypto_2_message:  # Third pass
                crypto_3_message += d[(d.index(c) + n) % len(d)]

            print('- Message:', crypto_3_message, '\n')     # Outputting the decrypted message
            # Clearing all messages for subsequent correct work
            middle_message = ''
            crypto_2_message = ''
            crypto_3_message = ''


try:    # Running a program through an exception
    StartApp()
except ValueError:      # With this error (not entered value), the program is restarted
    print('--- Error, program will restarted ---')
    StartApp()