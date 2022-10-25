"""useful functions to generate five letter words and sator squares"""

import hashlib
import re

FIVE_LETTER_WORD = r'^\w{5}$'
regex = re.compile(FIVE_LETTER_WORD)

def get_five_letter_words_from_file(filename: str) -> tuple:
    """read a file and return a uniq tuple of 5-letter words"""
    with open(filename, encoding='utf8') as file_obj:
        for line in file_obj:
            for word in line.split():
                clean_word = word.upper().strip()
                if regex.match(clean_word):
                    yield clean_word

def get_square(first: str, combo: tuple) -> tuple:
    """"make a square from given words"""
    new_combo = {first} | set(combo)
    all_words_set = new_combo | {word[::-1] for word in new_combo}
    return tuple(word.upper() for c in first for word in all_words_set if word.startswith(c))


def validate_square(square: tuple) -> bool:
    """validate a square transposing the orignal square and checking if they're the same"""
    transposed_square = tuple(''.join(str(c) for c in r) for r in zip(*square))
    return square == transposed_square


def print_square(square: tuple) -> str:
    """print a square in a formatted block"""
    return '\n'.join(' '.join(list(word)) for word in square)

if __name__=='__main__':

    FIRST_WORD = 'sator'
    combinations= [
        ('tenet', 'arepo'),
        ('arepo', 'tenet'),
        ('opera', 'tenet'),
        ('tenet', 'opera'),
    ]

    for combination in combinations:
        test_square = get_square(FIRST_WORD, combination)
        assert test_square == ('sator', 'arepo', 'tenet', 'opera', 'rotas')
        SQR_STR = print_square(test_square)
        print(SQR_STR)
        HASH_SUM_HEX = hashlib.sha256(SQR_STR.encode()).hexdigest()
        print(HASH_SUM_HEX)
        assert HASH_SUM_HEX == 'e180b2f13bc1d2f6d493cb01305776e84d4d80abe514b6819c37cafd857a6ab3'
        assert validate_square(test_square)
