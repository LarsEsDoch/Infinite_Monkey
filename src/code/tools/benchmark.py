import random
import string
import time
import os

from tqdm import tqdm

from src.code.utils.load import load_words
from src.code.tools.search import find_words_in_text


def benchmark(BENCHMARK_SIZES, BENCHMARK_LIMIT_SECONDS, BENCHMARK_LIMIT_SECONDS_SEARCH, MIN_WORD_LENGTH):
    print("\n--- Benchmark: random text generation ---")
    print("This will take up to 5 minutes. Please wait...")
    best_length = None
    best_length_search = None
    best_length_search_found = False
    english_words, german_words = load_words(MIN_WORD_LENGTH)
    for character_count in BENCHMARK_SIZES:
        start = time.time()
        chars = [random.choice(string.ascii_lowercase + '., ') for _ in tqdm(range(character_count), desc="Generating")]
        text = ''.join(chars)
        duration = time.time() - start
        print(f"{character_count:>8} characters generated in {duration:.3f} seconds\n")
        if duration <= BENCHMARK_LIMIT_SECONDS:
            best_length = character_count
        else:
            break

        time.sleep(0.2)

        if not best_length_search_found:
            start_search = time.time()
            word_sets = {
                "En": english_words,
                "Ge": german_words
            }
            words = find_words_in_text(text, MIN_WORD_LENGTH, word_sets, 10)
            duration_search = time.time() - start_search
            print(f"{len(words["En"])+len(words["Ge"]):>8} words found searched in {duration_search:.3f} seconds\n")
        if duration_search <= BENCHMARK_LIMIT_SECONDS_SEARCH:
            best_length_search = character_count
        else:
            best_length_search_found = True
        time.sleep(0.2)

    if best_length is None:
        print("⚠️ Even 10.000 characters are too slow. The process is aborted.")
        exit()
    if best_length_search is None:
        print("️️⚠️ Even 10.000 characters are too slow to search. The process is aborted.")

    print(f"\n✅ Best text length: {best_length} characters")
    print(f"✅ Best text length for searching: {best_length_search} characters")


    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../results/benchmark.txt"))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(best_length) + "," + str(best_length_search))
    return best_length, best_length_search

