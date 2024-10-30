import requests
from bs4 import BeautifulSoup
from googletrans import Translator



def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definitionid = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definitionid": word_definitionid
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definitionid = word_dict.get("word_definitionid")

        print(f"Значение слова - {word_definitionid}")
        user = input("Что это за слово? ")
        if user == word:
            print("Всё верно!")
        else:
            print(f"ответ не верный, было загадано это слово - {word}")

        play_again = input("хотите сыграть ещё раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()