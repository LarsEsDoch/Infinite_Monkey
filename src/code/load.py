import os

def load_text():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/output.txt"))
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_words(MIN_WORD_LENGTH):
    english_words = set()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../words/words.txt"))
    with open(file_path, "r", encoding="utf-8") as f:
        for zeile in f:
            word = zeile.strip().lower()
            if word.isalpha() and len(word) >= MIN_WORD_LENGTH:
                english_words.add(word)

    german_words = set()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../words/wortliste.txt"))
    with open(file_path, "r", encoding="utf-8") as f:
        for zeile in f:
            word = zeile.strip().lower()
            if word.isalpha() and len(word) >= MIN_WORD_LENGTH:
                german_words.add(word)

    return english_words, german_words

def load_benchmark():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/benachmark.txt"))
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()