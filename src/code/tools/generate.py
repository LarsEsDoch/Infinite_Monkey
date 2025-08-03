import random
import string
import os
import gc
import time
from tqdm import tqdm

from src.code.utils.save import save_large_text, save_text


def generate_random_text(max_length, blocksize):
    if max_length > blocksize:
        remaining = max_length
        remaining_steps = max_length // blocksize
        print(f"\n--- Generating Random Text {f'{max_length:,} in {remaining_steps:,} steps'.replace(',', '.'):>12} ---\n")
        while remaining > 0:
            chunk_size = min(remaining, blocksize)
            chars = [random.choice(string.ascii_lowercase + '., ') for _ in
                     tqdm(range(chunk_size), desc="Generating")]
            chunk = ''.join(chars)
            save_large_text(chunk)
            remaining -= chunk_size
            gc.collect()
            remaining_steps -= 1
            time.sleep(0.2)
            print(f"Remaining steps: {remaining_steps:,}".replace(',', '.'))
    else:
        print(f"\n--- Generating Random Text {f'{max_length:,}'.replace(',', '.'):>12} ---\n")
        chars = [random.choice(string.ascii_lowercase + '., ') for _ in tqdm(range(max_length), desc="Generating")]
        text = ''.join(chars)
        save_text(text)

    print("Generated")