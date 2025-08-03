import random
import string
import time
import os

from tqdm import tqdm

from src.code.utils.load import load_words
from src.code.tools.search import find_words_in_text
from src.code.utils.save import save_benchmark


def benchmark(benchmark_sizes, benchmark_limit_seconds, benchmark_limit_seconds_search, min_word_length):
    print("\n--- Benchmark: random text generation ---")
    print("This will take up to 5 minutes. Please wait...")
    best_length = None
    best_length_search = None
    best_length_search_found = False
    english_words, german_words = load_words(min_word_length)
    for character_count in benchmark_sizes:
        start = time.time()
        chars = [random.choice(string.ascii_lowercase + '., ') for _ in tqdm(range(character_count), desc="Generating")]
        text = ''.join(chars)
        duration = time.time() - start
        print(f"{f'{character_count:,}'.replace(',', '.'):>12} characters generated in {duration:.3f} seconds\n")
        if duration <= benchmark_limit_seconds:
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
            words = find_words_in_text(text, min_word_length, word_sets, 10)
            duration_search = time.time() - start_search
            print(
                f"{f'{len(words["En"]) + len(words["Ge"]):,}'.replace(',', '.'):>12} words found searched in {duration_search:.3f} seconds\n")
        if duration_search <= benchmark_limit_seconds_search:
            best_length_search = character_count
        else:
            best_length_search_found = True
        time.sleep(0.2)

    if best_length is None:
        print("⚠️ Even 10.000 characters are too slow. The process is aborted.")
        exit()
    if best_length_search is None:
        print("⚠️ Even 10.000 characters are too slow to search. The process is aborted.")

    print(f"\n✅ Best text length: {f'{best_length:,}'.replace(',', '.')} characters")
    print(f"✅ Best text length for searching: {f'{best_length_search:,}'.replace(',', '.')} characters")

    save_benchmark(best_length, best_length_search)
    return best_length, best_length_search

