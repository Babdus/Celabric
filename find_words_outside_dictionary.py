import re

from generate_ipa_section import generate_ipa_section

with open('index.html', 'r') as f:
    text = f.read()

all_words = re.findall('href="#word-(.*?)"', text)
missing_words = set()

for word in all_words:
    if re.search(f'id="word-{word}"', text) is None:
        missing_words.add(word)

print(' '.join(sorted(missing_words)))