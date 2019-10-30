from histogram import *
import random


def random_word(histogram):
    # gives uniform distribution
    for i in range(len(histogram)):
        frequency = histogram[i][1]
        word = histogram[i][0]
        if frequency > 1:
            for i in range(1, frequency):
                histogram.append([word, frequency])

    random_num = random.randint(0, unique_words(histogram))
    random_word = histogram[random_num][0]
    return random_word

histogram = list_of_lists_histogram('poetry_snippet.txt')
print(random_word(histogram))