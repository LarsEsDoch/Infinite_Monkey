from tqdm import tqdm

from src.code.utils.load import load_words

def search_english_german(min_word_length, text):
    english_words, german_words = load_words(min_word_length)

    word_sets = {
        "English": english_words,
        "German": german_words
    }
    print("\n--- Search words ---")
    found_words = find_words_in_text(text, min_word_length, word_sets, 10)
    print("\n--- Found words (english) ---")
    for i, w in enumerate(sorted(found_words["English"]), 1):
        print(f"{i:2d}. {w:<20}", end='')
        if i % 3 == 0:
            print()
    print("\n\n--- Found words (german) ---")
    for i, w in enumerate(sorted(found_words["German"]), 1):
        print(f"{i:2d}. {w:<20}", end='')
        if i % 3 == 0:
            print()

    #phrases = find_phrases_from_text(text, word_sets, 3, 20, 30, 4)

    #print("\n--- Found Phrases ---")
    #for phrase in sorted(phrases):
    #    print(phrase)

    return sorted(found_words["English"]), sorted(found_words["German"])

def find_words_in_text(text, min_len, word_sets, max_word_len=20):
    found_words = {lang: set() for lang in word_sets}

    text_len = len(text)
    total_iterations = sum(
        max(0, min(max_word_len, text_len - i) - min_len + 1)
        for i in tqdm(range(text_len), desc="Calculating iterations", unit="checks")
    )

    with tqdm(total=total_iterations, desc="Searching words", unit="checks") as pbar:
        for i in range(text_len):
            for l in range(min_len, min(max_word_len, text_len - i) + 1):
                word = text[i:i + l]
                for lang, word_set in word_sets.items():
                    if word in word_set:
                        found_words[lang].add(word)
                pbar.update(1)

    return found_words

def is_valid_word(word, word_sets):
    return any(word in word_set for word_set in word_sets.values())

def find_phrases_from_text(text, word_sets, min_word_len, max_word_len, max_phrase_len, max_words_per_phrase):
    found_phrases = set()
    text_len = len(text)

    with tqdm(total=text_len, desc="Searching phrases", unit="chars") as pbar:
        for start in range(text_len):
            for end in range(start + min_word_len * 2, min(start + max_phrase_len + 1, text_len + 1)):
                substring = text[start:end]

                def try_split(pos=0, path=[]):
                    if len(path) > max_words_per_phrase:
                        return
                    if pos == len(substring) and len(path) >= 2:
                        found_phrases.add(' '.join(path))
                        return
                    for i in range(min_word_len, min(max_word_len, len(substring) - pos) + 1):
                        word = substring[pos:pos + i]
                        if is_valid_word(word, word_sets):
                            try_split(pos + i, path + [word])

                try_split()
            pbar.update(1)

    return found_phrases

def search_custom_words(text):
    print("--- Search words ---")
    print("Enter a word or phrase to search for or exit with exit")
    while True:
        word = input("Search after: ")
        if word.lower() == "exit":
            break
        if word.lower() in text:
            count = text.lower().count(word.lower())
            if count < 2:
                print(f"Characters found: {word}")
            else:
                print(f"Characters found {count:,} times: {word}".replace(',', '.'))
        else:
            print(f"Characters not found: {word}")