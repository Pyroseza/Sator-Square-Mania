# README

These scripts were used to generate the EMKC contest found here: <https://emkc.org/contests/103/sator-square-mania>

The source of the "Latin" words found in [latin_words.txt](latin_words.txt) and [palindromes.txt](palindromes.txt) come from this site: <https://personal.math.ubc.ca/~cass/frivs/latin/latin-dict-full.html>

The main file that generates the puzzles and answers is [gen_words.py](gen_words.py), this takes all 5-letter words from [latin_words.txt](latin_words.txt) and generates the following 2 files:

- [all_puzzles.txt](all_puzzles.txt)
- [all_answers.txt](all_answers.txt)

You can then use [contest_tests.py](contest_tests.py) to generate a random subset of the puzzles and answers, a sample of the output files are these:

- [contest_puzzles.txt](contest_puzzles.txt)
- [contest_answers.txt](contest_answers.txt)

[utils.py](utils.py) is where you can find all the shared functions.

This was fun to make, if you feel inspired, please join us on [Discord](https://engineerman.org/discord) and [EMKC](https://emkc.org/) help make some more Contests 🤓
