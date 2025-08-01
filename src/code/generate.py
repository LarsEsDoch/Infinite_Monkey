import random
import string

def generate_random_text(MAX_LENGTH, BLOCKSIZE):
    print(f"\n--- Generating Random Text {MAX_LENGTH} ---\n")
    text = ''.join(random.choice(string.ascii_lowercase) for _ in range(MAX_LENGTH))
    print("\n--- Random Text ---\n")
    for i in range(0, len(text), BLOCKSIZE):
        print(text[i:i+BLOCKSIZE])

    return text