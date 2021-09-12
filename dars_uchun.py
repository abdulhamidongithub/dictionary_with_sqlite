from sqlite3 import connect
#If the input is admin, they can add new words to the dictionary. If it is a user, they can search for words
ask = input("Choose one of the two options: User/Admin -> ").lower()
if ask == 'admin':
    with connect("dictionary.db") as my_db:
        cursor = my_db.cursor()
        again = 'yes'
        while again == 'yes':
            uz = input("O'zbekcha so'zni kiriting: ")
            eng = input("Enter the word in English: ")
            cursor.execute(
                """
                INSERT INTO DICT(uz, eng)
                VALUES(?, ?)
                
                """, (uz, eng)
            )
            print("So'z ma'lumotlar omboriga qo'shildi")
            again = input("Do you want to add some more words?(yes/no)").lower()
        else:
            print("Dasturchamizdan foydalanganingiz uchun rahmat!")
elif ask == 'user':
    with connect("dictionary.db") as my_db:
        cursor = my_db.cursor()
        again = 'yes'
        while again == 'yes':
            lang = input("Tilni tanlang/Choose the language. (uz/eng): ")
            if lang == 'uz':
                soz = input("Qidirilayotgan so'zni kiriting: ")
                cursor.execute(
                    """
                    SELECT eng FROM DICT WHERE uz=?
                    """, (soz,)
                )
                uz_soz = cursor.fetchall()
                if uz_soz:
                    print(uz_soz[0][0])
                else:
                    print("Qidirilayotgan so'z ma'lumotlar omborida yo'q")
            elif lang == 'eng':
                word = input("Enter the word you are looking for: ")
                cursor.execute(
                    """
                    SELECT uz FROM DICT WHERE eng=?
                    """, (word,)
                )
                en_word = cursor.fetchall()
                if en_word:
                    print(en_word[0][0])
                else:
                    print("The word you are looking for doesn't exist in our database")
            else:
                print("You made a mistake inputting the data.")
            again = input("Do you want to search some more words?(yes/no)").lower()
elif ask=='show_all':
    with connect("dictionary.db") as my_db:
        cursor = my_db.cursor()
        cursor.execute(
            """
            SELECT * FROM DICT
            """
        )
        all_words = cursor.fetchall()
        for word in all_words:
            print(word)
else:
    print("You made a mistake inputting the data. Rerun the project:))")
