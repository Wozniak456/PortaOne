import re
from collections import Counter


def find_first_unique(entered):
    unique_chars = {}
    words = re.findall(r'\b\w+\'*\w*\b', entered)  # \'*\w* на випадок апострофа у середині слова

    for word in words:
        char_count = Counter(word)
        unique_char = None
        for char in word:
            if char_count[char] == 1:
                unique_char = char
                break
        if unique_char is not None:  # якщо це не слово "бубу", де немає унікальних символів
            if unique_char in unique_chars:
                unique_chars[unique_char] += 1
            else:
                unique_chars[unique_char] = 1

    result = None
    for key, value in unique_chars.items():
        if value == 1:
            result = key
            break
    print(f"The first unique characters in all words and their rarity: {unique_chars}")
    return result


if __name__ == '__main__':
    try:
        pattern = r'\S'
        text = input('input text: ')
        if re.search(pattern, text) is None:
            raise ValueError('Empty string!')
        print(f'The first unique character: {find_first_unique(text)}')
    except ValueError as e:
        print("Error: ", str(e))


    # The Tao gave birth to machine language.  Machine language gave birth to the assembler. The assembler gave birth to the compiler.  Now there are ten thousand languages. Each language has its purpose, however humble.  Each language expresses the Yin and Yang of software.  Each language has its place within the Tao. But do not program in COBOL if you can avoid it. -- Geoffrey James, "The Tao of Programming"








