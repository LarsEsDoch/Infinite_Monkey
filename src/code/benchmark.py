import random
import string
import time
import os

def benchmark(BENCHMARK_SIZES, BENCHMARK_LIMIT_SECONDS):
    print("\n--- Benchmark: random text generation ---")
    print("This may take a while...")
    best_length = None
    for menge in BENCHMARK_SIZES:
        start = time.time()
        _ = ''.join(random.choice(string.ascii_lowercase) for _ in range(menge))
        dauer = time.time() - start
        print(f"{menge:>8} characters generated in {dauer:.3f} seconds")
        if dauer <= BENCHMARK_LIMIT_SECONDS:
            best_length = menge
        else:
            break

    if best_length is None:
        print("⚠️ Even 10.000 characters are too slow. The process is aborted.")
        exit()

    print(f"\n✅ Best text length: {best_length} characters")

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results/benachmark.txt"))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(best_length)
    return best_length

