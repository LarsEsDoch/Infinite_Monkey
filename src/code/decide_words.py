def decide_words(best_length, words):
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
        print("Do you want to accept the recommended length? If not, it may take longer to get results.")
        print("Or you can enter a custom length. (c)")
        decision = input("Accept recommended length? (y/n/c): ")
        if decision.lower().strip() == "y":
            words = best_length
        elif decision.lower().strip() == "c":
            custom_length = input("Enter a custom length: ")
            while not custom_length.isdigit():
                print("Please enter a number.")
                custom_length = input("Enter a custom length: ")
            words = int(custom_length)
        else:
            words = words

        return words