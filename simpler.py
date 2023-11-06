 
import re
import string
from collections import Counter

frequency = Counter()

with open("input.txt", mode="r", encoding="utf-8") as input_file:
    for line in input_file:
        # string.punctutation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        cleaned_line = re.sub(f'[{string.punctuation}]', ' ', line).lower()
        frequency.update(cleaned_line.split())

# Print the word frequencies in descending order
print("SÖZ".ljust(20, ' ') , "SAY".ljust(20, ' '))
print("="*20, "="*20)
for word, count in frequency.most_common():
    print(word.ljust(20, ' ') , count)

print("="*20, "="*20)
print("Fərqli söz sayı".ljust(20, ' ') , f"{len(frequency)}".ljust(20, ' '))
print("Ümumi söz sayı".ljust(20, ' ') , f"{frequency.total()}".ljust(20, ' '))
