import time


print('\n' 'Crypter Program 1.1.5 Public version, stable' '\n' 'by CISCer' '\n')
main_lyster = ' abcefghjklnopqdrystiuvmwxzABCSEFGHIJKLMDNXOPQRTUVWYZ4123568907ßÞÝÜÛÚÙØ×ÖÕÔÓÒÑÐÏÎÍÌËÊÉÈÇÆ¨ÅÄÃÂÁÀÿþýüûúùø÷öõôóòñðïîíìëêéèçæ¸åäãâáà.,/?;:<>!@#¹$%^&*()-_=+{[]}'
symbols = ['¹', '&', '-', ')', '%', '/', ']', ';', ':', '^', '>', ',', '+', '@', '*', '=', '{', '#', '[', '}', '(', '.', '$', '!', '_', '<', '?', ' ']

lyster_shuffle = ['/', '9', 'ê', 'Ü', '^', 'c', 'O', '÷', 'o', 'ü', 'Ï', 'Q', 'ò', '!', 'Þ', 'ð', 'Ð', 'Z', 'Ä', 'X', 'ç', 'q', 'y', '_', '8', 'Ú', ')', 'b', 'B', '¹', 'ß', 'ã', 'M', 'm', 'é', 'ú', '@', 'Î', 'Û', 'Ê', 'U', '&', 'g', '}', '=', 'Ô', 'à', 'E', 'Ò', 'ø', 'á', 'a', 'p', 'Ñ', 'n', 'x', ',', 'ö', 'ó', '%', 'r', 'û', '7', 'j', 'V', '¸', 'ë', 'Æ', 'i', 'è', ' ', '>', 'ù', 'w', 'ô', 'Ö', 'É', 'L', 'î', 'u', '0', 'ÿ', 'ñ', 'À', 'd', '$', '2', 'J', 'Â', 'P', '1', 'È', '-', '¨', '{', 'Ë', '?', 'F', 'Õ', '6', 'W', 'l', '*', 'D', 'í', 's', 'ï', 'I', 'A', 'C', 'ì', 'H', 'Á', 'Ì', 'Ç', ']', 'Ù', 'å', 'k', '5', 'G', 'â', '[', 'S', '+', 'R', 'T', 'e', 'K', 'f', '(', 'Ã', 'õ', 'þ', 'z', '3', 'Ý', 'N', 'Ó', ';', '<', 'ä', 'æ', '#', 'Y', 't', 'Ø', ':', 'ý', '4', '×', 'v', 'h', 'Å', 'Í', '.']
lyster_shuffle_def_null = ['{', '3', 'N', 's', 'É', 'c', 'T', 'Ñ', '^', 'Î', '<', 'a', 'î', 'Ç', 'à', '9', 'M', 'V', 'w', '/', 'e', 'i', 'g', '>', 'l', ']', '4', 'p', 'Á', '5', 'å', '7', 'J', 'W', '}', '-', 'ï', 'm', '@', 'q', 'K', '$', 'f', 'í', 'I', 'Û', ';', 'ð', 'Å', 'À', 'Ê', 'h', '0', 'È', 'S', '!', '6', 'd', 'z', 'û', '(', 'ô', 'Ù', '[', '?', 'ú', 'Ä', 'è', '÷', 'H', 'u', 'Ì', 'O', 'Â', 'j', '*', 'o', 'k', 'Ð', '2', 'ø', 'Ö', 'Y', '=', '1', 'Ý', 't', 'U', 'Z', 'ç', 'Í', '#', 'ã', 'x', 'Þ', 'ñ', 'F', 'A', 'X', 'b', 'é', 'ü', '×', 'Ï', 'ê', 'â', '8', 'Ã', '.', 'ó', 'C', 'æ', 'Q', '+', 'Ú', 'Õ', '_', 'á', 'ù', '¨', 'õ', '¸', 'Ë', 'ä', 'ö', 'R', ':', 'ì', ' ', 'Ó', 'Æ', ')', 'Ø', 'v', 'þ', 'P', 'ÿ', 'L', ',', 'r', 'E', 'ë', 'Ü', '%', '¹', '&', 'B', 'G', 'D', 'Ô', 'y', 'ò', 'Ò', 'ý', 'ß', 'n']
lyster_shuffle_def_eins = ['Ï', 'É', 'Ë', 'h', 'k', 'ã', 'R', 'n', '?', 'Z', 's', 'û', 'x', '@', 'F', ')', 'Ù', '{', '=', '^', 'r', 'm', 'V', 'ï', 'ÿ', '-', 'Â', 'Ü', 'A', 'P', 'I', 'L', 'Û', 'Þ', 'â', '2', '7', 'ß', 'á', '¹', '0', 'ü', 'Ð', 'H', 'i', 'y', 'C', 'ð', '¸', 'Ñ', 'ò', 'Ì', '+', 'w', 'Á', '[', 'O', 'Ø', 'õ', 'î', 'ñ', 'a', 'í', '1', 'Ö', 'è', 'q', '9', 'U', '>', ',', 'À', 'Ô', 'e', 'v', 'N', '!', 'Ò', 'ö', ':', 'Ä', 'ê', 'J', '#', '<', 'å', ';', '5', ']', 'z', 'Æ', 'f', 'b', 'Å', 'u', '%', '/', 'Ú', 'd', 'ó', '÷', 'Ê', 'ù', 'ú', 'æ', 'ë', 'E', 'p', '6', '4', 'Ã', 'ä', 'ç', 'ì', 'K', '.', 'È', '¨', 'D', 'ô', 'j', 'Q', 'ø', '$', 'T', 'Õ', '_', 'o', 'Î', 'g', 'G', 'à', 'S', '*', ' ', 'Ç', 'Ó', '&', 'B', 'þ', '8', 'Í', 'X', 'Ý', 'W', 'Y', 't', 'M', '}', '(', 'é', '×', 'ý', 'l', '3', 'c']
lyster_shuffle_def_zwei = ['ï', 'H', 'ñ', 'A', 'ö', 'y', '_', 'Ï', '*', 'q', '¹', '[', 'Ù', '@', '(', 'E', 'Y', 'e', 'Í', 'Ó', 'þ', 'è', 'n', '>', 'É', '=', 'ì', 'P', '8', 'S', 'j', '#', 'Q', 'C', 'Ã', 'r', 'ô', 'R', 'ò', 'â', '?', 'Ô', 'm', 'ù', '^', 'ý', '!', 'u', ';', 'v', 'å', ']', 'U', 'ä', 'Ø', 'Ú', 'ú', 'D', '¸', '9', 'í', 's', 'c', 'ç', '$', 'i', 'b', 'Æ', 'ã', '1', '%', 'M', 'W', '-', 'z', 'Ý', 'ê', 'w', 'X', 'Ò', '7', '&', 'T', '+', 'Z', 'x', 'Î', '4', 'p', 'À', 'h', 'Ë', 'Ü', 'K', 'ü', 'á', 'é', 'û', '5', 'à', ')', '}', '/', '6', 'o', '×', 'Â', '÷', 'Ê', '0', 'G', 'B', 'Ñ', 'N', 'I', 't', 'F', 'Õ', 'Ð', 'f', ' ', 'l', 'V', '3', '<', 'Á', 'g', 'ø', 'ð', 'a', 'O', '{', 'ó', 'î', 'Ì', 'Û', '2', '¨', 'Ç', ':', 'È', 'Ä', 'k', '.', 'ÿ', 'J', 'Þ', ',', 'L', 'æ', 'õ', 'd', 'Ö', 'ë', 'ß', 'Å']
lyster_shuffle_def_drei = ['z', '+', 'Î', 'Ç', 'Ï', '$', 'ï', 'H', 'e', 'Â', 'ý', 'j', 'n', 'y', 'þ', ',', 'd', 'i', 'r', 'k', 'ù', '!', 'g', 'Ð', '>', 'Ë', 'í', 'X', 'ÿ', 'Q', 'b', 'Å', 'ä', 'ñ', '6', '(', '.', '#', 'f', 'û', '^', 'm', '}', 'Þ', '=', 'c', 'v', 'W', 'F', '5', 'á', 'Ò', '@', '8', '9', 't', 'ô', '¨', 'ð', 'D', 'Ä', '[', 'õ', 'T', 'Ü', 'ì', '-', '{', 'R', 'Ý', ' ', '4', 'o', '×', 'À', 'ò', 'Û', 'Z', 'S', 'B', ']', 'ç', 'È', 'ß', 'l', 'J', 'ú', 'Í', 'h', 'î', 'x', 'K', 'å', 'O', 'ó', 'à', '1', '0', 'Æ', '<', 'É', 'Ø', '*', 'ë', 'Õ', 'Á', ')', 'ø', '%', 'Ô', 'ã', 'Ã', '÷', 'M', 'Ì', 'G', 'C', '¸', '/', '3', '7', 'N', ';', 'P', '2', 'U', 'a', 'ê', '&', '¹', 'I', 'Ê', 'Ñ', 'E', 'ö', 'Ú', 'é', 'æ', 'q', 'Y', 'â', '_', 'Ù', ':', 'V', 'ü', 'u', 'Ö', 'p', 'w', '?', 'Ó', 'è', 's', 'L', 'A']

mas_txt = '----- Start of correspondence -----''\n'     # Ñîîáùåíèå î ñòàðòå ïðîãðàììû


def StartApp():
    """" Ãëàâíàÿ ôóíêöèÿ, îòâå÷àþùàÿ çà ðàáîòó ïðîãðàììû """
    middle_message = ''
    crypto_2_message = ''
    crypto_3_message = ''

    print('\n' 'Encrypt - 1, Decipher - 2, Exit - 0' '\n' 'Encrypt/Decipher?')
    c_or_d = int(input('Change: '))    # Âûáîð: çàøèôðîâàòü, ðàñøèôðîâàòü èëè âûéòè
    if c_or_d == 0:     # Óñëîâèÿ âûõîäà
        quit()
    elif c_or_d > 2:
        print('-- Invalid change, try again, ìëTziÛY8^ñDimÐ --')
        StartApp()
    n = int(input('Key: '))     # Êëþ÷ øèôðîâàíèÿ

    oper_key = int(input('Oper key (0-4): '))   # Äîïîëíèòåëüíûé êëþ÷ øèôðîâàíèÿ (âûáîð èç ñëîâàðåé)
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
        print('-- Error "Oper key", restart --')    # Ïðè îøèáêå âûáîðà ïðîãðàììà çàïðàøèâàåò ñíîâà
        oper_key = int(input('Oper key (0-4): '))

    print('Selected keys:', str(n) + ', ' + str(oper_key))      # Ïîêàçûâàþòñÿ âûáðàííûå êëþ÷è
    time.sleep(1)   # Çàäåðæêà â 1 ñåêóíäó

    print("\n" * 100)   # "Î÷èñòêà" òåðìèíàëà
    print(mas_txt)      # Ñîîáùåíèå î ñòàðòå ïðîãðàììû

    restart_program = 'Enter 0 to restart program'
    print(restart_program)  # Òåêñò ñ ïðåäëîæåíèåì ïåðåçàïóñòèòü ïðîãðàììó

    while True:     # Äàëåå â öèêëå èäåò ââîä è âûâîä ñîîáùåíèé
        if c_or_d == 1:     # Áëîê ïî çàøèôðîâêå ñîîáùåíèé
            s = input('- Message: ').strip()    # Ïðèíèìàþòñÿ íà ââîä âñå ñèìâîëû ñ êëàâèàòóðû ïîëüçîâàòåëÿ
            if s == '0':
                print('\n''-- Restart --')
                StartApp()
            # Äàëåå èäåò çàøèôðîâêà â 3 ïðîõîäà
            for a in s:     # Ïåðâûé ïðîõîä
                middle_message += d[(d.index(a) - n) % len(d)]
            for b in middle_message:    # Âòîðîé ïðîõîä
                crypto_2_message += d[(d.index(b) - n) % len(d)]
            for c in crypto_2_message:
                crypto_3_message += d[(d.index(c) - n) % len(d)]

            print('- Encrypted in:', crypto_3_message, '\n')    # Âûâîä çàøèôðîâàííîãî ñîîáùåíèÿ
            # Î÷èñòêà âñåõ ñîîáùåíèé äëÿ ïîñëåäóþùåé êîððåêòíîé ðàáîòû
            middle_message = ''
            crypto_2_message = ''
            crypto_3_message = ''

        elif c_or_d == 2:       # Áëîê ïî ðàñøèôðîâêå ñîîáùåíèé
            s = input('- Decipher: ').strip()   # Ïðèíèìàþòñÿ íà ââîä âñå ñèìâîëû ñ êëàâèàòóðû ïîëüçîâàòåëÿ
            if s == '0':        # Óñëîâèå ïåðåçàïóñêà ïðîãðàììû
                print('\n''--Restart--')
                StartApp()
            # Äàëåå èäåò ðàñøèôðîâêà â 3 ïðîõîäà
            for a in s:    # Ïåðâûé ïðîõîä
                middle_message += d[(d.index(a) + n) % len(d)]
            for b in middle_message:    # Âòîðîé ïðîõîä
                crypto_2_message += d[(d.index(b) + n) % len(d)]
            for c in crypto_2_message:  # Òðåòèé ïðîõîä
                crypto_3_message += d[(d.index(c) + n) % len(d)]

            print('- Message:', crypto_3_message, '\n')     # Âûâîä ðàñøèôðîâàííîãî ñîîáùåíèÿ
            # Î÷èñòêà âñåõ ñîîáùåíèé äëÿ ïîñëåäóþùåé êîððåêòíîé ðàáîòû
            middle_message = ''
            crypto_2_message = ''
            crypto_3_message = ''


try:    # Çàïóñê ïðîãðàììû ÷åðåç èñêëþ÷åíèå
    StartApp()
except ValueError:      # Ïðè ýòîé îøèáêå (íå ââåäåííîå çíà÷åíèå) ïðîãðàììà ïåðåçàïóñêàåòñÿ
    print('--- Error, program will restarted ---')
    StartApp()
