from src.code.load import load_words

TYPE = 1

def search_english_german(MIN_WORD_LENGTH, text):
    english_words, german_words = load_words(MIN_WORD_LENGTH)

    english_found_words = set()
    german_found_words = set()
    if TYPE == 0:
        for i in range(len(text)):
            for j in range(i + MIN_WORD_LENGTH, len(text) + 1):
                word = text[i:j]
                if word in english_words:
                    english_found_words.add(word)
                elif word in german_words:
                    german_found_words.add(word)

        print("\n--- Found words (english) ---")
        for w in sorted(english_found_words):
            print(w)
        print("\n--- Found words (german) ---")
        for w in sorted(german_found_words):
            print(w)
    else:
        print("\n--- Found words ---")
        for i in range(len(text)):
            for j in range(i + MIN_WORD_LENGTH, len(text) + 1):
                word = text[i:j]
                if word in english_words:
                    english_found_words.add(word)
                    print(word)
                elif word in german_words:
                    german_found_words.add(word)
                    print(word)

    return sorted(english_found_words), sorted(german_found_words)

def search_custom_words(text):
    print("--- Search words ---")
    print("Enter a word to search for or exit with exit")
    while True:
        word = input("Search after: ")
        if word.lower() == "exit":
            break
        while not word.isalpha():
            print("Please enter a word.")
            word = input("Search after: ")
        if word in text:
            count = text.lower().count(word.lower())
            if count < 2:
                print(f"Word found: {word}")
            else:
                print(f"Word found {count} times: {word}")
        else:
            print(f"Word not found: {word}")