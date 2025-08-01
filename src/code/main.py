from src.code.benchmark import benchmark
from src.code.decide_words import decide_words
from src.code.generate import generate_random_text
from src.code.load import load_benchmark, load_text
from src.code.search import search_english_german, search_custom_words
from src.code.save import save_text, save_founds

MAX_LENGTH = 100000000
BLOCKSIZE = 100
MIN_WORD_LENGTH = 3
BENCHMARK_LIMIT_SECONDS = 10
BENCHMARK_SIZES = [10000, 25000, 50000, 100000, 250000, 500000, 1000000, 2500000, 5000000, 10000000, 25000000, 50000000, 100000000]

def full_process():
    print("Running full process...")
    best_length = benchmark(BENCHMARK_SIZES, BENCHMARK_LIMIT_SECONDS)
    custom_length = decide_words(best_length, MAX_LENGTH)
    text = generate_random_text(custom_length, BLOCKSIZE)
    english_found_words, german_found_words = search_english_german(MIN_WORD_LENGTH, text)
    save_text(text)
    save_founds(english_found_words, german_found_words)

def benchmark_mode():
    print("Running benchmark...")
    benchmark(BENCHMARK_SIZES, BENCHMARK_LIMIT_SECONDS)

def generate_mode():
    print("Generating random text...")
    custom_length = decide_words(load_benchmark(), MAX_LENGTH)
    text = generate_random_text(custom_length, BLOCKSIZE)
    save_text(text)

def search_mode():
    print("Searching (English, German)...")
    text = load_text()
    english_found_words, german_found_words = search_english_german(MIN_WORD_LENGTH, text)
    save_founds(english_found_words, german_found_words)

def search_mode_custom():
    print("Searching (English, German)...")
    text = load_text()
    search_custom_words(text)

def exit_program():
    print("Exiting program...")
    exit()

def invalid_option():
    print("Invalid option selected!")

menu_options = {
    "1": full_process,
    "2": benchmark_mode,
    "3": generate_mode,
    "4": search_mode,
    "5": search_mode_custom,
    "6": exit_program
}

def main():
    while True:
        print("\n--- Decide process mode ---")
        print("1. Full process")
        print("2. Benchmark")
        print("3. Generate")
        print("4. Search (English, German)")
        print("5. Search Custom")
        print("6. Exit")
        input_mode = input("Choose mode: ")
        print()

        menu_options.get(input_mode, invalid_option)()

main()
