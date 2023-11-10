import re
import string

FREQUENCY = {}
TOTAL_WORD_COUNT = 0

try:
    with open("input.txt", mode="r", encoding="utf-8") as input_file:
        while True:
            line = input_file.readline()
            if line:
                # string.punctutation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
                cleaned_line = line.lower().translate(str.maketrans('', '', string.punctuation))
                # cleaned_line = re.sub(f'[{string.punctuation}]', ' ', line).lower()

                words = cleaned_line.split()
                for word in words:
                    if FREQUENCY.get(word, None) is None:
                        FREQUENCY[word] = 1
                        TOTAL_WORD_COUNT += 1
                    else:
                        FREQUENCY[word] += 1
                        TOTAL_WORD_COUNT += 1
            else:
                break
except FileNotFoundError:
    print('"input.txt" faylı təmin edilməyib.')
    exit(0)

print("SÖZ".ljust(20, ' ') , "SAY".ljust(20, ' '))
print("="*20, "="*20)
already_printed = []
for i in range(TOTAL_WORD_COUNT):
    max_count = 1
    max_word: str  = ''
    for word, count in FREQUENCY.items():
        if count >= max_count and word not in already_printed:
            max_count = count
            max_word = word
    
    if max_word != '':
        print(max_word.ljust(20, ' ') , max_count)
        already_printed.append(max_word)

print("="*20, "="*20)
print("Fərqli söz sayı".ljust(20, ' ') , f"{len(FREQUENCY)}".ljust(20, ' '))
print("Ümumi söz sayı".ljust(20, ' ') , f"{TOTAL_WORD_COUNT}".ljust(20, ' '))