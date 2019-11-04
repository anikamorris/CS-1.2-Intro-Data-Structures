from histogram import list_of_lists_histogram, file_or_string
import random

def get_total_weight(histogram):
    total_weight = 0
    for item in histogram:
        total_weight += item[1]
    return total_weight

def random_word(histogram):
    total_weight = get_total_weight(histogram)
    random_weight = random.randint(0, total_weight)
    print(str(random_weight) + " random weight")
    for item in histogram:
        random_weight = random_weight - item[1]
        print(random_weight)
        if random_weight <= 0:
            return item[0]

histogram = list_of_lists_histogram('poetry_snippet.txt')
print(random_word(histogram))