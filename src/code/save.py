import os

def save_text(text):
    os.makedirs("../results", exist_ok=True)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/output.txt"))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def save_founds(english_found_words, german_found_words):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/found_english_words.txt"))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(english_found_words)))

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/found_german_words.txt"))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(german_found_words)))