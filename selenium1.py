from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def search_article(driver, query):
    """Осуществляет поиск статьи по запросу."""
    driver.get("https://ru.wikipedia.org/")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Задержка для загрузки страницы


def display_paragraphs(driver):
    """Отображает первые несколько параграфов статьи."""
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text p")
    if not paragraphs:
        print("Параграфы не найдены.")
        return
    for i, para in enumerate(paragraphs[:5], 1):  # Ограничиваем до 5 первых параграфов
        print(f"\nПараграф {i}: {para.text}")


def show_related_articles(driver):
    """Показывает связанные статьи и возвращает ссылки на них из основного текста."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mw-content-text"))
    )
    links = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text a[title]")
    related_articles = []
    for link in links:
        title = link.get_attribute("title")
        url = link.get_attribute("href")
        # Проверка, чтобы ссылка вела на статью, а не на служебную страницу
        if url and title and "wiki" in url and not url.startswith("https://ru.wikipedia.org/wiki/Служебная:"):
            related_articles.append((title, url))
            if len(related_articles) >= 10:  # Ограничиваем до 10 связанных статей
                break

    if related_articles:
        for i, (title, _) in enumerate(related_articles, 1):
            print(f"{i}. {title}")
    else:
        print("Нет связанных страниц.")
    return related_articles


def main():
    print("Добро пожаловать в Wikipedia CLI с Selenium!")

    driver = webdriver.Chrome()  # Убедитесь, что chromedriver доступен в PATH
    try:
        while True:
            query = input("\nВведите запрос для поиска на Википедии или 'выход' для завершения: ").strip()
            if query.lower() == 'выход':
                break

            search_article(driver, query)

            while True:
                print("\nЧто вы хотите сделать?")
                print("1. Листать параграфы текущей статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Выйти из программы")

                choice = input("Введите номер действия: ").strip()

                if choice == '1':
                    display_paragraphs(driver)

                elif choice == '2':
                    related_articles = show_related_articles(driver)
                    if not related_articles:
                        continue

                    link_choice = input("Введите номер связанной страницы или 'назад' для возврата: ").strip()
                    if link_choice.lower() == 'назад':
                        continue

                    try:
                        selected_url = related_articles[int(link_choice) - 1][1]
                        driver.get(selected_url)
                        time.sleep(2)  # Задержка для загрузки новой страницы
                    except (IndexError, ValueError):
                        print("Неверный выбор. Попробуйте снова.")

                elif choice == '3':
                    print("Выход из программы.")
                    return

                else:
                    print("Неверный выбор. Попробуйте снова.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
