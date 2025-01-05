from bs4 import BeautifulSoup

# Define your replacement dictionary
replacement_dict = {
    'q': 'ts',
    'Q': 'tsh',
    'S': 'sh',
    'C': 'ch',
    'T': 'th',
    'K': 'kh',
    'P': 'ph',
    'w': 'gh',
    'Z': 'zh',
    'y': 'j',
    'h': 'xj',
    'j': 'gj',
    'U': 'y',
    'O': 'ø',
    # Add more character replacements as needed
}

def replace_text_and_bold(text, replacement_dict):
    """
    Replace characters in text based on the given replacement dictionary and make the text bold.
    """
    replaced_text = ''.join(replacement_dict.get(char, char) for char in text)

    words = replaced_text.split()
    replaced_words = [f'[[{word}]]' for word in words]
    replaced_text = ' '.join(replaced_words)
    # Wrap the replaced text in a <b> tag to make it bold
    return BeautifulSoup(f"<b>{replaced_text}</b>", "html.parser")

def replace_brackets_in_ipa(text):
    """
    Replace '[' with '/' and ']' with '/' in the text for 'ipa' elements.
    """
    return text.replace('[', '/').replace(']', '/')

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Remove all <button> and <audio> elements
for tag in soup.find_all(['button', 'audio']):
    tag.decompose()

# Replace the class "celabric" with "romanization"
for element in soup.find_all(class_='celabric'):
    element['class'] = ['romanization']

# Find all <a> elements with class 'tooltip' and unwrap them
for link in soup.find_all('a', class_='tooltip'):
    link.unwrap()  # Unwrap removes the <a> element but keeps its content

# Find all elements with class 'romanization' and replace text with bolded replacements
elements = soup.find_all(class_='romanization')
for element in elements:
    if element.string:  # Check if the element has a string to replace
        bold_tag = replace_text_and_bold(element.string, replacement_dict)
        element.clear()  # Clear existing content
        element.append(bold_tag)  # Append the new bolded content

# Find all elements with class 'ipa' and replace brackets
ipa_elements = soup.find_all(class_='ipa')
for element in ipa_elements:
    if element.string:  # Check if the element has a string to replace
        element.string = replace_brackets_in_ipa(element.string)

# Write the modified HTML back to a new file or overwrite the original one
with open('modified_index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HTML file has been modified and saved as 'modified_index.html'")



