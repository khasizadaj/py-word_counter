 
import re
import string
from collections import Counter

FREQUENCY = Counter()

try:
    with open("input.txt", mode="r", encoding="utf-8") as input_file:
        for line in input_file:
            # string.punctutation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            cleaned_line = line.lower().translate(str.maketrans('', '', string.punctuation))
            # cleaned_line = re.sub(f'[{string.punctuation}]', ' ', line.lower())
            FREQUENCY.update(cleaned_line.split())
except FileNotFoundError:
    print('"input.txt" faylı təmin edilməyib.')
    exit(0)

print("SÖZ".ljust(20, ' ') , "SAY".ljust(20, ' '))
print("="*20, "="*20)
for word, count in FREQUENCY.most_common():
    print(word.ljust(20, ' ') , count)

print("="*20, "="*20)
print("Fərqli söz sayı".ljust(20, ' ') , f"{len(FREQUENCY)}".ljust(20, ' '))
print("Ümumi söz sayı".ljust(20, ' ') , f"{FREQUENCY.total()}".ljust(20, ' '))
