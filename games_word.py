# import requests
# from bs4 import BeautifulSoup
# from googletrans import Translator
#
# translator = Translator()
#
#
# def get_english_words():
#     url = "https://randomword.com/"
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#
#         english_words = soup.find("div", id="random_word").text.strip()
#         word_definitionid = soup.find("div", id="random_word_definition").text.strip()
#
#         # Перевод
#         russian_word = translator.translate(english_words, dest="ru").text
#         russian_definition = translator.translate(word_definitionid, dest="ru").text
#
#         return {
#             "english_words": english_words,
#             "word_definitionid": word_definitionid,
#             "russian_word": russian_word,
#             "russian_definition": russian_definition
#         }
#     except:
#         print("Произошла ошибка")
#
#
# def word_game():
#     print("Добро пожаловать в игру")
#     while True:
#         word_dict = get_english_words()
#
#         if word_dict is None:
#             print("Не удалось получить слово. Попробуйте еще раз.")
#             continue
#
#         word = word_dict.get("english_words")
#         word_definitionid = word_dict.get("word_definitionid")
#         russian_word = word_dict.get("russian_word")
#         russian_definition = word_dict.get("russian_definition")
#
#         # Вывод перевода
#         print(f"Значение слова - {russian_definition}")
#         user = input("Что это за слово (ответ на русском)? ")
#
#         if user.lower() == russian_word.lower():
#             print("Всё верно!")
#         else:
#             print(f"Ответ не верный, было загадано это слово - {russian_word}")
#
#         play_again = input("Хотите сыграть ещё раз? y/n ")
#         if play_again != "y":
#             print("Спасибо за игру!")
#             break
#
#
# word_game()