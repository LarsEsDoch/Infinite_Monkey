def decide_words(best_length, best_length_search, words):
    print("\n--- Decide the number of characters ---")
    if best_length is None:
        print("Do you want to enter a custom length?")
        decision = input("Enter custom length? (y/n): ")
        if decision.lower().strip() == "y":
            custom_length = input("Enter a custom length: ")
            while not custom_length.isdigit():
                print("Please enter a number.")
                custom_length = input("Enter a custom length: ")
            words = int(custom_length)
        else:
            words = words
        return words
    else:
        print("Do you want to accept the recommended length for generating (g) or searching (s)? If not, it may take longer to get results.")
        print(f"Recommended length for generating: {best_length}")
        print(f"Recommended length for searching: {best_length_search}")
        print("Or you can enter a custom length. (c)")
        print("Else you use the default length. (n)")
        decision = input("Accept recommended length? (g/s/c/n): ")
        if decision.lower().strip() == "g":
            words = best_length
        elif decision.lower().strip() == "s":
            words = best_length_search
        elif decision.lower().strip() == "c":
            custom_length = input("Enter a custom length: ")
            while not custom_length.isdigit():
                print("Please enter a number.")
                custom_length = input("Enter a custom length: ")
            words = int(custom_length)
        else:
            words = words

        return words