def settings_menu(max_length, blocksize, min_word_length, benchmark_limit_seconds, benchmark_limit_seconds_search,
                  benchmark_sizes):
    while True:
        print("Settings:")
        print("1. MAX_LENGTH: " + str(max_length))
        print("2. BLOCKSIZE: " + str(blocksize))
        print("3. MIN_WORD_LENGTH: " + str(min_word_length))
        print("4. BENCHMARK_LIMIT_SECONDS: " + str(benchmark_limit_seconds))
        print("5. BENCHMARK_LIMIT_SECONDS_SEARCH: " + str(benchmark_limit_seconds_search))
        print("6. BENCHMARK_SIZES: " + str(benchmark_sizes))
        print("7. Exit")

        option = input("Choose an option to change: ")
        if option == "7":
            break

        if option == "1":
            max_length = max_length_menu()
        elif option == "2":
            blocksize = blocksize_menu()
        elif option == "3":
            min_word_length = min_word_length_menu()
        elif option == "4":
            benchmark_limit_seconds = benchmark_limit_menu()
        elif option == "5":
            benchmark_limit_seconds_search = benchmark_limit_search_menu()
        elif option == "6":
            benchmark_sizes = benchmark_sizes_menu()
        else:
            invalid_option()

    return max_length, blocksize, min_word_length, benchmark_limit_seconds, benchmark_limit_seconds_search, benchmark_sizes


def max_length_menu():
    print("Enter a new MAX_LENGTH:")
    while True:
        try:
            max_length = int(input("MAX_LENGTH: "))
            return max_length
        except ValueError:
            print("Invalid input. Please enter a number.")


def blocksize_menu():
    print("Enter a new BLOCKSIZE:")
    while True:
        try:
            blocksize = int(input("BLOCKSIZE: "))
            return blocksize
        except ValueError:
            print("Invalid input. Please enter a number.")

def min_word_length_menu():
    print("Enter a new MIN_WORD_LENGTH:")
    while True:
        try:
            min_word_length = int(input("MIN_WORD_LENGTH: "))
            return min_word_length
        except ValueError:
            print("Invalid input. Please enter a number.")


def benchmark_limit_menu():
    print("Enter a new BENCHMARK_LIMIT_SECONDS:")
    while True:
        try:
            benchmark_limit_seconds = int(input("BENCHMARK_LIMIT_SECONDS: "))
            return benchmark_limit_seconds
        except ValueError:
            print("Invalid input. Please enter a number.")


def benchmark_limit_search_menu():
    print("Enter a new BENCHMARK_LIMIT_SECONDS_SEARCH:")
    while True:
        try:
            benchmark_limit_seconds_search = int(input("BENCHMARK_LIMIT_SECONDS_SEARCH: "))
            return benchmark_limit_seconds_search
        except ValueError:
            print("Invalid input. Please enter a number.")


def benchmark_sizes_menu():
    print("Enter new BENCHMARK_SIZES separated by spaces:")
    while True:
        try:
            sizes = input("BENCHMARK_SIZES: ").split()
            benchmark_sizes = [int(size) for size in sizes]
            return benchmark_sizes
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")


def exit_program():
    print("Exiting settings...")
    exit()


def invalid_option():
    print("Invalid option selected!")



