# -*- coding: cp1251 -*-
import time


print('\n' 'Crypter Program v1.2.0 ENG Public version, stable' '\n' 'by CISCer' '\n')
main_lyster = ' abcefghjklnopqdrystiuvmwxzABCSEFGHIJKLMDNXOPQRTUVWYZ4123568907.,/?;:<>!@#№$%^&*()-_=+{[]}'
symbols = ['№', '&', '-', ')', '%', '/', ']', ';', ':', '^', '>', ',', '+', '@', '*', '=', '{', '#', '[', '}', '(', '.', '$', '!', '_', '<', '?', ' ']

lyster_shuffle = ['C', '5', 'b', 's', '!', '[', 'V', 'm', 'H', ' ', 'e', '?', 'B', 'O', 'L', '9', 'E', ']', ')', 'F', 'M', '=', '0', '&', 'l', '6', 'S', 'P', '.', 'R', 'u', '*', 'p', 'z', 'c', '@', 'n', 'Y', '}', 'X', '_', 'T', 'x', 'j', '4', '7', 'r', 'w', 'G', '#', ',', 'W', 'K', 'q', '<', '3', 'y', 'N', 'h', 'v', 'D', '8', '^', '+', '{', 'a', '2', '-', '>', '(', '$', '%', 'd', '№', 'Q', '/', '1', 'I', 'J', 'g', 'Z', 'f', 'A', 'U', ';', 'o', 'i', ':', 'k', 't']
lyster_shuffle_def_null = ['N', '=', 'c', 'P', '0', 'y', '{', 'F', 's', 'U', 'w', 'R', 'T', '.', 'Q', 'm', 'Y', 'g', 'E', '(', 'S', 'v', '/', 'q', 'K', 'B', '№', 'A', 'r', ']', '_', 'h', 'o', '!', 'k', 'D', '6', '<', '[', '$', 'H', 'L', 'G', 'p', '4', '8', '3', 't', 'x', '1', '>', '9', '5', 'j', 'f', '2', 'V', 'a', ')', 'u', 'X', '&', 'n', '^', 'Z', 'e', '7', 'z', ' ', 'O', '?', ',', ':', '@', 'i', 'M', '*', '}', 'C', '+', 'b', 'd', 'W', '#', 'l', '%', '-', 'J', ';', 'I']
lyster_shuffle_def_eins = ['@', 'o', '=', 't', '#', 'F', 'l', 'f', 'e', 'q', 'w', 'p', '9', '_', 'X', 'x', 'I', 'h', '>', '.', '7', 'U', 'z', 'K', '&', 'G', '1', '(', '[', '6', 'u', 'Y', '}', '{', '?', 'M', '+', '8', 'D', 'b', 'O', 'k', 'E', '4', 'N', 'A', ')', 'R', 'g', 'r', 'V', 'v', 'S', 'C', '3', 'T', 'm', 'W', 'j', 'B', '!', 'a', 'd', 'H', '*', ',', 'c', '/', '<', 'n', 'L', ']', 'Z', 'P', '$', '5', '^', 's', '%', '№', '0', 'J', '2', ':', 'i', 'Q', ' ', '-', ';', 'y']
lyster_shuffle_def_zwei = ['P', ',', '@', '+', 'r', 'b', '?', 's', 'a', '#', '2', '(', 'd', 'Z', '6', 'i', 'E', 'S', '5', 'X', 'm', 'V', '.', '*', ']', 'C', 'I', '>', '/', 'u', 'l', 'Y', 'H', '!', 'h', '{', '[', 'Q', '}', ' ', 'B', 'D', '8', 'A', '$', '<', 'O', 'N', 'o', 'p', '%', 'v', 'f', '№', '7', 'G', '0', 'J', '_', 'U', 'x', 'T', 'W', 'k', 'w', '1', ';', ':', 'c', 'F', 'R', '9', 'j', 'M', ')', '^', '&', 't', '3', 'L', 'e', '4', '-', 'z', '=', 'n', 'K', 'y', 'g', 'q']
lyster_shuffle_def_drei = ['g', 'z', ',', 'S', ']', 'y', '@', 'W', '3', '-', ';', 'p', 'q', '%', '^', 'v', 'N', ' ', '/', 'G', 'Q', 'l', 'X', 'P', 'h', 'U', '$', '5', '№', 'b', '?', 'C', 'V', '.', 'E', 'u', 'o', ':', '<', '{', '&', '0', '8', 'O', '_', 't', 'w', 'H', 'J', 'm', '6', 'e', 's', '>', 'M', '1', '7', 'B', '4', 'K', 'A', '*', 'n', '+', 'Y', 'Z', '9', 'j', 'i', '!', ')', '}', 'R', 'r', '#', 'd', 'k', '[', 'x', 'I', '2', '(', 'F', 'L', 'f', 'D', 'c', 'a', 'T', '=']

mas_txt = '----- Start of correspondence -----''\n'     # Program start message


def StartApp():
    """" The main function responsible for the operation of the program """
    middle_message = ''     # First pass message
    crypto_2_message = ''   # Second pass message
    crypto_3_message = ''   # Third pass message

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
            s = input('- Decipher: ').strip()   # All characters from the user's keyboard are accepted for input
            if s == '0':        # Program restart condition
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