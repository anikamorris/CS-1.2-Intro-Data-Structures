from histogram import list_of_lists_histogram, file_or_string
from stochastic_sampling import get_total_weight, random_word
import random

def test_random_word():
    words = []
    for i in range(0, 10000):
        rand_word = random_word(list_of_lists_histogram('poetry_snippet.txt'))
        words.append(rand_word)

    histogram = []
    for word in words:
        is_in_histogram = False
        for i in range(len(histogram)):
            if word == histogram[i][0]:
                histogram[i][1] += 1
                is_in_histogram = True

        if is_in_histogram == False:
            histogram.append([word, 1])
    print(histogram)

test_random_word()