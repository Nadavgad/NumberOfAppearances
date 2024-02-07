import os
import unittest
import NumberOfAppearances


class TestNumberOfAppearances(unittest.TestCase):

    def test_read_non_empty_file(self):
        """
        Test reading a non-empty file.
        """
        file_content = NumberOfAppearances.read_file(r'C:\Users\OS174\Documents\NadavTxt.txt')
        self.assertNotEqual(len(file_content), 0, "Test failed: The file is empty!")

    def test_read_file_content(self):
        """
        Test reading file content and comparing with expected content.
        """
        file_path = r'C:\Users\OS174\Documents\NadavTxt1.txt'

        try:
            with open(file_path, 'w') as file:
                file.write('Venus is the second planet from the sun')

            file_content = NumberOfAppearances.read_file(file_path)

            expected_content = ['Venus', 'is', 'the', 'second', 'planet', 'from', 'the', 'sun']

            self.assertEqual(file_content, expected_content, "Test failed: Content does not match the expected content")
        finally:
            # Clean up: Delete the test file
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_word_counts_in_text(self):
        """
        Test counting word occurrences in a text.
        """
        simple_string = 'Voldemort had 7 Horcruxes, one of the Horcruxes was Harry Potter himself. The words' \
                        ' Harry Potter, Horcruxes are part of the sentence'

        simple_string_list = simple_string.split()

        expected_simple_string = {'7': 1, 'are': 1, 'had': 1, 'harry': 2, 'himself': 1, 'horcruxes': 3, 'of': 2,
                                  'one': 1, 'part': 1, 'potter': 2, 'sentence': 1, 'the': 3, 'voldemort': 1,
                                  'was': 1, 'words': 1}

        self.assertEqual(NumberOfAppearances.words_counter(simple_string_list),
                         expected_simple_string, f"Test failed: Word counts do not match expected results")

    def test_word_counts_in_empty_text(self):
        """
        Test counting word occurrences in an empty text.
        """
        empty_string = ''
        expected_string = {}

        self.assertEqual(NumberOfAppearances.words_counter(empty_string),
                         expected_string, f"Test failed: Word counts do not match expected results")

    def test_appearances(self):
        """
        Test counting word appearances in a file.
        """
        file_path = r'C:\Users\OS174\Documents\NadavTxt.txt'

        expected_result = {'bad': 1, 'for': 2, 'great': 1, 'hardware': 1,
                           'is': 4, 'linux': 1, 'losers': 1, 'software': 1, 'windows': 1, 'winners': 1, 'במרחקו': 1,
                           'במשפט': 1, 'הוא': 1, 'הלכת': 2, 'הם': 1, 'הקודם': 1, 'השני': 1, 'כוכב': 2, 'מהשמש': 2,
                           'מילים': 1, 'נוגה': 1, 'שני': 1}

        self.assertEqual(NumberOfAppearances.appearances(file_path),
                         expected_result, f"Test failed: Word counts do not match expected results")

    def test_word_counts_with_punctuation(self):
        """
        Test counting word occurrences in text with punctuation.
        """
        text_with_punctuation = "Hello, World! How are you doing today?"
        words_with_punctuation = text_with_punctuation.split()
        expected_result = {'hello': 1, 'world': 1, 'how': 1, 'are': 1, 'you': 1, 'doing': 1, 'today': 1}
        self.assertEqual(NumberOfAppearances.words_counter(words_with_punctuation),
                         expected_result, f"Test failed: Word counts with punctuation do not match expected results")

    def test_appearances_with_custom_punctuation(self):
        """
        Test counting word appearances in a file with custom punctuation.
        """
        file_path = r'C:\Users\OS174\Documents\NadavTxt.txt'
        custom_punctuation = '!@#$%^&*()_+-={}[]|:;"\'<>,.?/~`'
        expected_result = {'bad': 1, 'for': 2, 'great': 1, 'hardware': 1,
                           'is': 4, 'linux': 1, 'losers': 1, 'software': 1, 'windows': 1, 'winners': 1, 'במרחקו': 1,
                           'במשפט': 1, 'הוא': 1, 'הלכת': 2, 'הם': 1, 'הקודם': 1, 'השני': 1, 'כוכב': 2, 'מהשמש': 2,
                           'מילים': 1, 'נוגה': 1, 'שני': 1}
        self.assertEqual(NumberOfAppearances.appearances(file_path, custom_punctuation),
                         expected_result,
                         f"Test failed: Word counts with custom punctuation do not match expected results")


if __name__ == '__main__':
    unittest.main()
