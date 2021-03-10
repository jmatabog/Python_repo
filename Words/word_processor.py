import string
import collections

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''Function to split to specifics''' 
    text1 = split(" ;.:,?", text.lower())
    my_list = [i for i in text1 if i != '']
    return my_list


def words_longer_than(length, text):
    '''function to print a word with a specific length'''
    text1 = convert_to_word_list(text)
    result = [word for word in text1 if len(word)>length]
    return result


def words_lengths_map(text):
    lister = convert_to_word_list(text)
    lengths = list(map(lambda word: len(word), lister))
    my_dict = {}
    for point in lengths:
        my_dict[point] = my_dict.get(point, 0) + 1
    return my_dict


def letters_count_map(text):
    
    return {key : text.lower().count(key) for key in string.ascii_lowercase}


def most_used_character(text):
    if text == "":
        return None
    list4 = letters_count_map(text)
    return max(list4, key=list4.get)
