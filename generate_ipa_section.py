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

ipa_to_celabric = [
    ('p&#688;', 'P'),
    ('t&#688;', 'T'),
    ('c&#688;', 'C'),
    ('k&#688;', 'K'),
    ('ts', 'q'),
    ('t&#643;', 'Q'),
    ('&#643;', 'S'),
    ('&#658;', 'Z'),
    ('&ccedil;', 'h'),
    ('y', 'U'),
    ('&#669;', 'y'),
    ('&#607;', 'j'),
    ('&#611;', 'w'),
    ('&#593;', 'a'),
    ('&aelig;', 'e'),
    ('&#618;', 'i'),
    ('&#650;', 'u'),
    ('&oslash;', 'O'),
]


def ipa_to_celabric_word(word):
    for ipa, letter in ipa_to_celabric:
        word = word.replace(ipa, letter)
    return word


def word_to_ipa(word):
    for letter, ipa in letters_to_ipa:
        word = word.replace(letter, ipa)
    return word


def generate_ipa_section(word, n_tabs=0):
    if len(word.split('_')) > 1:
        return generate_ipa_sentence_section(word, n_tabs)
    ipa_word = word_to_ipa(word)
    celabric_word = ipa_to_celabric_word(ipa_word)
    tabs = '    '*n_tabs
    html = f'{tabs}<a class="tooltip" href="#word-{word}"><span class="celabric">{celabric_word}</span> <span class="ipa">[{ipa_word}]</span></a>\n{tabs}<audio id="audio-{word}"><source src="audio/{word}.mp3" type="audio/mp3"></audio>\n{tabs}<button class="play-button" onclick="document.getElementById(\'audio-{word}\').play()">&#9658;</button>'
    pyperclip.copy(html)
    return html


def generate_ipa_sentence_section(sentence, n_tabs=0):
    words = sentence.split('_')
    tabs = '    ' * n_tabs
    ipa_sections = []
    celabric_sections = []
    for i, word in enumerate(words[:-1]):
        ipa_word = word_to_ipa(word)
        celabric_word = ipa_to_celabric_word(ipa_word)
        celabric_section = f'{tabs}<a class="tooltip" href="#word-{word}"><span class="celabric">{celabric_word}</span></a>'
        celabric_sections.append(celabric_section)
        ipa_section = f'{tabs}<a class="tooltip" href="#word-{word}"><span class="ipa">{"[" if i == 0 else ""}{ipa_word}{"]" if i == len(words) - 2 else ""}</span></a>'
        ipa_sections.append(ipa_section)
    celabric_html = f'\n'.join(celabric_sections)
    ipa_html = f'\n'.join(ipa_sections)
    html = f'{celabric_html}\n\n{ipa_html}\n{tabs}<audio id="audio-sentence{words[-1]}"><source src="audio/{words[-1]}.mp3" type="audio/mp3"></audio>\n{tabs}<button class="play-button" onclick="document.getElementById(\'audio-{words[-1]}\').play()">&#9658;</button>'
    pyperclip.copy(html)
    return html


print(generate_ipa_section(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0))
