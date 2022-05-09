import re


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


def add_celabric(matched):
    if matched.group() is not None:
        transcription = matched.group()[19:-8]
        celabric = transcription
        for replacement in ipa_to_celabric:
            celabric = celabric.replace(replacement[0], replacement[1])
        return "<span class=\"celabric\">"+celabric+"</span> "+matched.group()


with open('index.html', 'r') as f:
    text = f.read()

res_str = re.sub(r"<span class=\"ipa\">.+</span>", add_celabric, text)

with open('index.html', 'w') as f:
    f.write(res_str)
