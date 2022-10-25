"""find and generarate words for contest"""

import utils

def latin_words_generator():
    """a generator that yields latin words

    Yields:
        str: latin word
    """
    # words = utils.get_five_letter_words_from_file('latin_words.txt') # pylint: disable=E1101
    yield from utils.get_five_letter_words_from_file('latin_words.txt') # pylint: disable=E1101


def palindrome_generator():
    """a generator that yields palindromes

    Yields:
        str: palindrome
    """
    # palindromes = utils.get_five_letter_words_from_file('palindromes.txt') # pylint: disable=E1101
    yield from utils.get_five_letter_words_from_file('palindromes.txt') # pylint: disable=E1101

def gen_answer(square: tuple):
    """Join all the words in the square together"""
    return ''.join(square)

if __name__=='__main__':
    squares = (
        utils.get_square(a, (b, c))
        for a in latin_words_generator()
        for b in palindrome_generator()
        for c in latin_words_generator()
    )

    valid_squares = filter(utils.validate_square, squares)

    try:
        with (
            open('all_puzzles.txt', 'w+', encoding='utf8') as p,
            open('all_answers.txt', 'w+', encoding='utf8') as a):
            for i, valid_square in enumerate(valid_squares, start=1):
                print(f'Square {i}: {valid_square}', '\n', utils.print_square(valid_square)) # pylint: disable=E1101
                PUZZLE = '|'.join(valid_square[:3])
                ANSWER = gen_answer(valid_square)
                p.write(f'{PUZZLE}\n')
                a.write(f'{ANSWER}\n')
    except KeyboardInterrupt:
        print()
