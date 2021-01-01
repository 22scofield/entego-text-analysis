# --Databáze--
# Databáze článků
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Databáze registrovaných uživatelů
registred_users = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123 '}

# Obecné proměnné
main_separator = 60*'-'
separator = 40*'-'

# Úvodní pozdrav uživatele, přihlášení uživatele a kontrola správnosti zadaných údajů
print('Vítej, přihlaš se prosím zadáním uživatelského jména a hesla.')
print(main_separator)

# --Interakce s uživatelem--
# Vyzvání k přihlášení a ověření, zda je uživatel registrovaný
while True:
    user_name = input('Uživatelské jméno: ')
    user_pass = input('Uživatelské heslo: ')
    if user_name in registred_users.keys() and user_pass in registred_users.get(user_name):
        print(f'Vítej uživateli {user_name}, přihlášení proběhlo úspěšně.')
        print(main_separator)
        break
    else:
        print('Litujeme, uživatelské jméno, nebo heslo bylo zadáno nesprávně.')
        continue

# Výběr textu k analýze
while True:
    user_text_choice = input('Prosím, text k analýze výberem čísla 1 až 3: ')

    # Kontrola, zda uživatel zadal opravdu číslo
    if user_text_choice.isdigit() == False:
        print('Musíte zadat celé číslo v rozmězí 1 až 3.')
        continue

    # Kontrola jestli uživatel zadal číslo v požadovaném rozsahu
    if int(user_text_choice) < 1 or int(user_text_choice) > 3:
        print('Musíte zadat celé číslo v rozmězí 1 až 3.')
        continue
    else:
        # Potvrzení vybraného text a jeho vypasání
        print(f'Vybrali jste text, číslo {int(user_text_choice)}.')
        print(main_separator)
        print(TEXTS[int(user_text_choice) - 1])
        print(main_separator)
        break

# --Analýza zvoleného textu--
# Zvolený text
target_text = TEXTS[int(user_text_choice) - 1]

# Rozdělení textu na jednotlivá slova
target_text_by_words = target_text.split()
target_text_by_words_clear = []

# Očištění jednotlivých slov od zbytečných znaků
for word in target_text_by_words:
    target_text_by_words_clear.append(word.strip(',.!?'))

# Zjistění počtu slov v textu
target_text_words_count = len(target_text_by_words_clear)
# Proměnná pro počítání slov, které začínají velkým písmenem
target_text_words_first_upper_char_count = 0
# Proměnná pro počítání slov, které jsou napsané velkým písmem
target_text_words_upper_count = 0
# Proměnná pro počítání slov, které jsou napsané malým písmem
target_text_words_lower_count = 0
# Proměnná pro počítání čísel v textu
target_text_number_count = 0
# Slovník do kterého se bude ukládat délka slov a jejich počet
target_text_word_len_count = dict()
# Proměnná pro součet čísel z textu
target_text_sum_num = int()

# Cyklus, který projde slova v očištěném textu
for word in target_text_by_words_clear:
    # Proměnná, ve které se bude počítat, kolik velkých písmen je v daném slovu
    i = 0
    # Uložení délky slova
    word_len = len(word)
    # Uložení délky slova do slovníku
    target_text_word_len_count.setdefault(word_len)
    # Nastavení výchozí hodnoty v slovníku
    target_text_word_len_count.update({word_len: 0})
    # Podmínka, která zaznamená, zda bylo slovo napsané velkým písmem
    if word.isupper():
        target_text_words_upper_count += 1
    # Podmínka, která zaznamená, zda bylo slovo napsané malým písmem
    if word.islower():
        target_text_words_lower_count += 1
    # Podmínka, která zjistí, zda je v stringu číslo a přičte ho do proměnné celkového součtu čísel
    if word.isnumeric():
        target_text_number_count += 1
        target_text_sum_num = target_text_sum_num + int(word)
    # Cyklus, který projde jednotlivá písmena slova a zkontroluje, zda se jedná o velké písmeno
    for char in word:
        if char.isupper():
            i += 1
    # Podmínka, která hlídá, kolik bylo velkých písmen v slovu a ošetřuje tím duplicitní počítání
    if i > 0:
        target_text_words_first_upper_char_count += 1

# Cyklus, který znovu projde slova v očištěném textu
for word2 in target_text_by_words_clear:
    # Proměnná, ve které se bude počítat, počet slov dané délky v textu
    word_len_count = 0
    # Uložení délky slova
    word2_len = len(word2)
    # Získání hodnoty o počtu již zaevidovaných slov dané délky z slovníku
    word_len_count2 = target_text_word_len_count.get(len(word2)) + 1
    # Proměnná, která posupně do slovníku přičítá počty délky slov
    word_len_count3 = target_text_word_len_count.update({len(word2) : word_len_count2})

# Získání variant délky slov a převedení do listu
list_target_text_word_len_count = list(target_text_word_len_count.keys())
# Sezaření hodnot v listu
list_target_text_word_len_count.sort()

# Proměnná, ve které se bude počítat projetí všech hodnot cyklem níže
num_index = 0

# --Výstup pro uživatele--
print(str('Základní analýza textu:').upper())
print(separator)
print(f'''Počet slov: {target_text_words_count}
Počet slov začínajích s velkým písmenem: {target_text_words_first_upper_char_count}
Počet slov napsaný velkým písmem: {target_text_words_upper_count}
Počet slov napsaný malým písmem: {target_text_words_lower_count}
Počet čísel v textu: {target_text_number_count}
Součet čísel v textu: {target_text_sum_num}''')
print(main_separator)
print(str('Graf znázorňující délku slov a jejich počet v textu:').upper())
print(separator)
# Graf, který zobrazuje unikátní hodnoty délky slov ze slovníku a jejich počet
for num in list_target_text_word_len_count:
    print(f'{list_target_text_word_len_count[num_index]} {"*" * target_text_word_len_count.get(list_target_text_word_len_count[num_index])} {target_text_word_len_count.get(list_target_text_word_len_count[num_index])}')
    num_index += 1
print(main_separator)