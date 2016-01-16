"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    char_list = [char for char in input_string if char.isalpha()]

    char_frequency_dict = {}

    for char in char_list:
        char_frequency_dict[char] = char_frequency_dict.get(char, 0) + 1

    top_freq = max(char_frequency_dict.values())

    top_characters_list = []

    for char, freq in char_frequency_dict.items():
        if freq == top_freq:
            top_characters_list.append(char)

    return top_characters_list


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    word_frequency_dict = {}

    for word in words:
        word_len = len(word)
        if word_len not in word_frequency_dict:
            word_frequency_dict[word_len] = [word]
        else:
            word_frequency_dict[word_len].append(word)

    for key in word_frequency_dict:
        word_frequency_dict[key].sort()

    word_frequency_tuple_list = sorted(word_frequency_dict.items())

    return word_frequency_tuple_list


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
