"""Get a random subset of the generated tests and puzzles"""

from random import choice, shuffle

with (
    open('all_puzzles.txt', 'r', encoding='utf8') as p,
    open('all_answers.txt', 'r', encoding='utf8') as a,
    open('contest_puzzles.txt', 'w+', encoding='utf8') as tp,
    open('contest_answers.txt', 'w+', encoding='utf8') as ta):
    puzzles = p.read().splitlines()
    answers = a.read().splitlines()
    tests = list(zip(puzzles, answers))
    print(len(tests))
    shuffle(tests)
    LIM = 100
    for i, (puzzle, answer) in zip(range(LIM), tests):
        print(i,puzzle,answer)
        a, b, c = puzzle.split('|')
        b = b if choice((1, 0)) else b[::-1]
        print(f'"{a}", "{b}", "{c}"')
        PUZZLE = '|'.join((a, b, c))
        print(PUZZLE, ' -> ', answer)
        tp.write(f'{PUZZLE}\n')
        ta.write(f'{answer}\n')
