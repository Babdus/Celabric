import sys
from generate_ipa_section import generate_ipa_section

words = sys.argv[1:]

for word in words:
    sections = generate_ipa_section(word)[1]

    html = f'{" "*12}<li id="word-{word}">'
    html += f'\n{" "*16}{sections["celabric"]}'
    html += f' {sections["ipa"]}'
    html += f'\n{" "*16}{sections["button"]}'
    html += f'\n{" "*16}<ul>\n{" "*20}<li>'
    html += f'\n{" "*24}<span class="grammar"></span>'
    html += f'\n{" "*20}</li>\n{" "*16}</ul>\n{" "*12}</li>'

    print(html)