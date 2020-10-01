"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""
    # split phrase into list
    word_list = phrase.split(' ')
    # sort it 
    word_list.sort()
    # add count of each word to dict
    word_dict = {}
    for item in word_list:
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    for key, value in word_dict.items():
        print(key + ':', value)


    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
