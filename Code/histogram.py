def list_of_lists_histogram(source_text):
    words = []
    content = ''
    if '.txt' in source_text:
        file = open(source_text, 'r')
        content = file.read()
        file.close()
    else:
        content = source_text
    words = content.split()
    histogram = []
    for word in words:
        is_in_histogram = False
        for i in range(len(histogram)):
            if word == histogram[i][0]:
                histogram[i][1] += 1
                is_in_histogram = True

        if is_in_histogram == False:
            histogram.append([word, 1])
    
    return histogram

print(histogram('poetry_snippet.txt'))
