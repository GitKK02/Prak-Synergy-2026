import nltk
from nltk.tokenize import word_tokenize
from intents import INTENTS

# Первоначальная загрузка ресурсов NLTK
nltk.download('punkt')


def preprocess_text(text):
    """
    Приведение текста к нижнему регистру
    и разбиение на слова
    """
    text = text.lower()
    tokens = word_tokenize(text, language="russian")
    return tokens


def get_response(user_message):
    tokens = preprocess_text(user_message)

    for token in tokens:
        if token in INTENTS:
            return INTENTS[token]

    return (
        "Извините, я не смог понять вопрос. "
        "Попробуйте спросить о поступлении, расписании, "
        "стоимости обучения или общежитии."
    )


def main():
    print("=" * 60)
    print("Виртуальный помощник Университета 'Синергия'")
    print("Введите 'выход' для завершения работы")
    print("=" * 60)

    while True:

        user_message = input("\nВы: ")

        if user_message.lower() == "выход":
            print("Бот: До свидания!")
            break

        response = get_response(user_message)
        print("Бот:", response)


if __name__ == "__main__":
    main()
