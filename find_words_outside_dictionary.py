import re

from generate_ipa_section import word_to_ipa, ipa_to_celabric_word

with open('index.html', 'r') as f:
    text = f.read()

all_words = re.findall('href="#word-(.*?)"', text)
missing_words = set()

for word in all_words:
    if re.search(f'id="word-{word}"', text) is None:
        missing_words.add(word)

alphabet = 'ieaouUOpbPtdTcjCkgKvfzsZSyhwxqQmnrl'
alphabet_list = [ch for ch in alphabet]
alphabet_dict = {ch: f'{i:02}' for i, ch in enumerate(alphabet_list)}

def sorting_helper(word):
    celabric_word = ipa_to_celabric_word(word_to_ipa(word))
    number_word = ''.join([str(alphabet_dict[ch]) for ch in celabric_word])
    return number_word

print(' '.join(sorted(missing_words, key=sorting_helper)))