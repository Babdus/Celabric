import sys
import pyperclip


letters_to_ipa = [
    ('sh', '&#643;'),
    ('zh', '&#658;'),
    ('gh', '&#611;'),
    ('h', '&#688;'),
    ('gj', '&#607;'),
    ('a', '&#593;'),
    ('i', '&#618;'),
    ('u', '&#650;'),
    ('oe', '&oslash;'),
    ('e', '&aelig;'),
    ('xj', '&ccedil;'),
    ('j', '&#669;'),
]


def word_to_ipa(word):
    for letter, ipa in letters_to_ipa:
        word = word.replace(letter, ipa)
    return word

def generate_ipa_section(word, n_tabs=0):
    ipa_word = word_to_ipa(word)
    tabs = '    '*n_tabs
    html = f'{tabs}<a class="tooltip" href="#word-{word}"><span class="ipa">{ipa_word}</span></a>\n{tabs}<audio id="audio-{word}"><source src="audio/{word}.mp3" type="audio/mp3"></audio>\n{tabs}<button class="play-button" onclick="document.getElementById(\'audio-{word}\').play()">&#9658;</button>'
    pyperclip.copy(html)
    return html

print(generate_ipa_section(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0))