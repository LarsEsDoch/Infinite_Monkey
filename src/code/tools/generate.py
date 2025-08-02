import random
import string
from tqdm import tqdm

def generate_random_text(max_length, blocksize):
    print(f"\n--- Generating Random Text {max_length} ---\n")
    chars = [random.choice(string.ascii_lowercase + '., ') for _ in tqdm(range(max_length), desc="Generating")]
    text = ''.join(chars)
    print("\n--- Random Text ---\n")
    for i in range(0, len(text), blocksize):
        if i < 330:
            print(text[i:i + blocksize])
        else:
            print("...")
            break

    return text