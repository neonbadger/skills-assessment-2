"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    return list(set(words))


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    """

    # find the intersection of two lists

    return list(set(list1) & set(list2))




def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    word_list = input_string.split(" ")

    distinc_word_dict = {}

    for word in word_list:
        distinc_word_dict[word] = distinc_word_dict.get(word, 0) + 1
    
    return distinc_word_dict



def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dict = {
                    "sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "boy": "matey",
                    "madam": "proud beauty",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "lawyer": "foul blaggart",
                    "the": "th'",
                    "restroom": "head",
                    "my": "me",
                    "hello": "avast",
                    "is": "be",
                    "man": "matey",
                    }

    word_list = phrase.split(" ")
    new_word_list = []

    for word in word_list:
        if word in pirate_dict:
            word = pirate_dict[word]
        new_word_list.append(word)  

    new_phrase = " ".join(new_word_list)

    return new_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    word_length_dict = {}

    for word in words:
        word_len = len(word)
        if word_len not in word_length_dict:
            word_length_dict[word_len] = [word]
        else:
            word_length_dict[word_len].append(word)

    len_word_tuple_list = word_length_dict.items()

    return len_word_tuple_list



def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    unique_numbers = sorted(set(input_list))
    
    pairs = []
    
    for num in unique_numbers:
        potential_pair = 0 - num
        if potential_pair in unique_numbers:
            sum_zero_pair = sorted((num, potential_pair))
            pairs.append(sum_zero_pair)
    
    # convert pair-items from list to tuples
    tuple_pairs = [tuple(pair) for pair in pairs]

    # get unique items
    unique_pairs = set(tuple_pairs)
    
    zero_sum_pairs = []

    # convert pair-items from tuple to list
    for pair in unique_pairs:
        num1, num2 = pair
        zero_sum_pairs.append([num1, num2])
    
    return zero_sum_pairs







##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
