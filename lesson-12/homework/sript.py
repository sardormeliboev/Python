#Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    local_primes = []
    for number in range(start, end):
        if is_prime(number):
            local_primes.append(number)
    result.extend(local_primes)

def threaded_prime_checker(start_range, end_range, num_threads):
    threads = []
    result = []
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i != num_threads - 1 else end_range
        t = threading.Thread(target=check_primes, args=(start, end, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    result.sort()
    print("Found prime numbers:", result)

# Example usage
threaded_prime_checker(1, 100, 4)


#Exercise 2: Threaded File Processing (Word Count)

import threading
from collections import defaultdict

def count_words(lines, word_count_dict):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            word = word.lower().strip('.,!?":;()[]{}')  # simple cleaning
            local_count[word] += 1
    # merge local count into shared dictionary
    for word, count in local_count.items():
        with threading.Lock():
            word_count_dict[word] += count

def threaded_word_counter(file_path, num_threads):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    threads = []
    word_count = defaultdict(int)
    step = len(lines) // num_threads

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=count_words, args=(lines[start:end], word_count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Print word counts
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")


