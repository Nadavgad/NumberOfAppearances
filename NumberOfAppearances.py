import string

FILE_PATH = r'C:\Users\OS174\Documents\NadavTxt.txt'


def read_file(file_path_read):
    """
    Read a file and split its content into a list of words.

    :param file_path_read: The path for the txt file
    :return: List of words
    """
    with open(file_path_read, 'r', encoding='UTF-8') as file:

        file_data = file.read()

        words = file_data.split()

        return words


def words_counter(words_file, punctuation_chars=string.punctuation):
    """
    Count the appearances of words in a list.

    :param words_file: List of words to count
    :param punctuation_chars: Set of punctuation characters to be stripped from words
    :return: Dictionary that keys are words and values are the number of word appearances
    """
    word_appear = {}

    for word_on_txt in words_file:

        word_on_txt = word_on_txt.strip(punctuation_chars)

        word_on_txt = word_on_txt.lower()

        word_appear[word_on_txt] = word_appear.get(word_on_txt, 0) + 1

    return word_appear


def appearances(file_path_txt, punctuation_chars=string.punctuation):
    """
    Count the appearances of words in a file.

    :param file_path_txt: The path for the txt file
    :param punctuation_chars: Set of punctuation characters to be stripped from words
    :return: Dictionary that keys are words and values are the number of word appearances
    """
    words_file = read_file(file_path_txt)

    number_of_words = words_counter(words_file, punctuation_chars)

    return number_of_words

