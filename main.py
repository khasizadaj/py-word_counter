import re
import string

frequency = {}
total_word_count = 0

with open("input.txt", mode="r", encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if line:
            # string.punctutation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            cleaned_line = re.sub(f'[{string.punctuation}]', ' ', line).lower()

            words = line.split()
            for word in words:
                # print(f"Söz: {word}")
                if frequency.get(word, None) is None:
                    frequency[word] = 1
                    total_word_count += 1
                    # print(f"Yeni söz tapıldı: {word}")
                else:
                    frequency[word] += 1
                    total_word_count += 1
                    # print(f"Təkrar söz tapıldı: {word} ({frequency[word]})")
        else:
            break

print("SÖZ".ljust(20, ' ') , "SAY".ljust(20, ' '))
print("="*20, "="*20)
already_printed = []
for i in range(total_word_count):
    max_count = 1
    max_word: str  = ''
    for word, count in frequency.items():
        if count >= max_count and word not in already_printed:
            max_count = count
            max_word = word
    
    if max_word != '':
        print(max_word.ljust(20, ' ') , max_count)
        already_printed.append(max_word)

print("="*20, "="*20)
print("Fərqli söz sayı".ljust(20, ' ') , f"{len(frequency)}".ljust(20, ' '))
print("Ümumi söz sayı".ljust(20, ' ') , f"{total_word_count}".ljust(20, ' '))