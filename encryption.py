# -*- coding: cp1251 -*-
import time


print('\n' 'Crypter Program 1.1.5 Public version, stable' '\n' 'by CISCer' '\n')
main_lyster = ' abcefghjklnopqdrystiuvmwxzABCSEFGHIJKLMDNXOPQRTUVWYZ4123568907�������������������������ƨ��������������������������������������.,/?;:<>!@#�$%^&*()-_=+{[]}'
symbols = ['�', '&', '-', ')', '%', '/', ']', ';', ':', '^', '>', ',', '+', '@', '*', '=', '{', '#', '[', '}', '(', '.', '$', '!', '_', '<', '?', ' ']

lyster_shuffle = ['/', '9', '�', '�', '^', 'c', 'O', '�', 'o', '�', '�', 'Q', '�', '!', '�', '�', '�', 'Z', '�', 'X', '�', 'q', 'y', '_', '8', '�', ')', 'b', 'B', '�', '�', '�', 'M', 'm', '�', '�', '@', '�', '�', '�', 'U', '&', 'g', '}', '=', '�', '�', 'E', '�', '�', '�', 'a', 'p', '�', 'n', 'x', ',', '�', '�', '%', 'r', '�', '7', 'j', 'V', '�', '�', '�', 'i', '�', ' ', '>', '�', 'w', '�', '�', '�', 'L', '�', 'u', '0', '�', '�', '�', 'd', '$', '2', 'J', '�', 'P', '1', '�', '-', '�', '{', '�', '?', 'F', '�', '6', 'W', 'l', '*', 'D', '�', 's', '�', 'I', 'A', 'C', '�', 'H', '�', '�', '�', ']', '�', '�', 'k', '5', 'G', '�', '[', 'S', '+', 'R', 'T', 'e', 'K', 'f', '(', '�', '�', '�', 'z', '3', '�', 'N', '�', ';', '<', '�', '�', '#', 'Y', 't', '�', ':', '�', '4', '�', 'v', 'h', '�', '�', '.']
lyster_shuffle_def_null = ['{', '3', 'N', 's', '�', 'c', 'T', '�', '^', '�', '<', 'a', '�', '�', '�', '9', 'M', 'V', 'w', '/', 'e', 'i', 'g', '>', 'l', ']', '4', 'p', '�', '5', '�', '7', 'J', 'W', '}', '-', '�', 'm', '@', 'q', 'K', '$', 'f', '�', 'I', '�', ';', '�', '�', '�', '�', 'h', '0', '�', 'S', '!', '6', 'd', 'z', '�', '(', '�', '�', '[', '?', '�', '�', '�', '�', 'H', 'u', '�', 'O', '�', 'j', '*', 'o', 'k', '�', '2', '�', '�', 'Y', '=', '1', '�', 't', 'U', 'Z', '�', '�', '#', '�', 'x', '�', '�', 'F', 'A', 'X', 'b', '�', '�', '�', '�', '�', '�', '8', '�', '.', '�', 'C', '�', 'Q', '+', '�', '�', '_', '�', '�', '�', '�', '�', '�', '�', '�', 'R', ':', '�', ' ', '�', '�', ')', '�', 'v', '�', 'P', '�', 'L', ',', 'r', 'E', '�', '�', '%', '�', '&', 'B', 'G', 'D', '�', 'y', '�', '�', '�', '�', 'n']
lyster_shuffle_def_eins = ['�', '�', '�', 'h', 'k', '�', 'R', 'n', '?', 'Z', 's', '�', 'x', '@', 'F', ')', '�', '{', '=', '^', 'r', 'm', 'V', '�', '�', '-', '�', '�', 'A', 'P', 'I', 'L', '�', '�', '�', '2', '7', '�', '�', '�', '0', '�', '�', 'H', 'i', 'y', 'C', '�', '�', '�', '�', '�', '+', 'w', '�', '[', 'O', '�', '�', '�', '�', 'a', '�', '1', '�', '�', 'q', '9', 'U', '>', ',', '�', '�', 'e', 'v', 'N', '!', '�', '�', ':', '�', '�', 'J', '#', '<', '�', ';', '5', ']', 'z', '�', 'f', 'b', '�', 'u', '%', '/', '�', 'd', '�', '�', '�', '�', '�', '�', '�', 'E', 'p', '6', '4', '�', '�', '�', '�', 'K', '.', '�', '�', 'D', '�', 'j', 'Q', '�', '$', 'T', '�', '_', 'o', '�', 'g', 'G', '�', 'S', '*', ' ', '�', '�', '&', 'B', '�', '8', '�', 'X', '�', 'W', 'Y', 't', 'M', '}', '(', '�', '�', '�', 'l', '3', 'c']
lyster_shuffle_def_zwei = ['�', 'H', '�', 'A', '�', 'y', '_', '�', '*', 'q', '�', '[', '�', '@', '(', 'E', 'Y', 'e', '�', '�', '�', '�', 'n', '>', '�', '=', '�', 'P', '8', 'S', 'j', '#', 'Q', 'C', '�', 'r', '�', 'R', '�', '�', '?', '�', 'm', '�', '^', '�', '!', 'u', ';', 'v', '�', ']', 'U', '�', '�', '�', '�', 'D', '�', '9', '�', 's', 'c', '�', '$', 'i', 'b', '�', '�', '1', '%', 'M', 'W', '-', 'z', '�', '�', 'w', 'X', '�', '7', '&', 'T', '+', 'Z', 'x', '�', '4', 'p', '�', 'h', '�', '�', 'K', '�', '�', '�', '�', '5', '�', ')', '}', '/', '6', 'o', '�', '�', '�', '�', '0', 'G', 'B', '�', 'N', 'I', 't', 'F', '�', '�', 'f', ' ', 'l', 'V', '3', '<', '�', 'g', '�', '�', 'a', 'O', '{', '�', '�', '�', '�', '2', '�', '�', ':', '�', '�', 'k', '.', '�', 'J', '�', ',', 'L', '�', '�', 'd', '�', '�', '�', '�']
lyster_shuffle_def_drei = ['z', '+', '�', '�', '�', '$', '�', 'H', 'e', '�', '�', 'j', 'n', 'y', '�', ',', 'd', 'i', 'r', 'k', '�', '!', 'g', '�', '>', '�', '�', 'X', '�', 'Q', 'b', '�', '�', '�', '6', '(', '.', '#', 'f', '�', '^', 'm', '}', '�', '=', 'c', 'v', 'W', 'F', '5', '�', '�', '@', '8', '9', 't', '�', '�', '�', 'D', '�', '[', '�', 'T', '�', '�', '-', '{', 'R', '�', ' ', '4', 'o', '�', '�', '�', '�', 'Z', 'S', 'B', ']', '�', '�', '�', 'l', 'J', '�', '�', 'h', '�', 'x', 'K', '�', 'O', '�', '�', '1', '0', '�', '<', '�', '�', '*', '�', '�', '�', ')', '�', '%', '�', '�', '�', '�', 'M', '�', 'G', 'C', '�', '/', '3', '7', 'N', ';', 'P', '2', 'U', 'a', '�', '&', '�', 'I', '�', '�', 'E', '�', '�', '�', '�', 'q', 'Y', '�', '_', '�', ':', 'V', '�', 'u', '�', 'p', 'w', '?', '�', '�', 's', 'L', 'A']

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
        print('-- Invalid change, try again, ��Tzi�Y8^�Dim� --')
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
            s = input('- Decipher: ').strip()   # ����������� �� ���� ��� ������� � ���������� ������������
            if s == '0':        # ������� ����������� ���������
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