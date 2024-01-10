class NumberOfAppearances:

    def sumOfWordsOnFile(self, file_path_txt):
        """

        :param file_path_txt: The path for the txt file
        :return: Dictionary that keys are words and values are number of word appearances
        """
        word_appear = {}
        try:
            with open(file_path_txt, 'r', encoding='UTF-8') as file:
                file_data = file.read()

                words = file_data.split()

                for wordOnTxt in words:
                    wordOnTxt = wordOnTxt.strip('!@#$%^&*()|/|-+=_`~?."":;,')

                    word_appear[wordOnTxt] = word_appear.get(wordOnTxt, 0) + 1

            return word_appear

        except FileNotFoundError:
            print(f"Error: File not found at path {file_path_txt}")
        except Exception as e:
            print(f"Error: {e}")


wordOnFileInstance = NumberOfAppearances()

file_path = r'C:\Users\OS174\Documents\NadavTxt.txt'

word_appearances = wordOnFileInstance.sumOfWordsOnFile(file_path)

if word_appearances is not None:
    print("Word Appearances:")
    for word, count in word_appearances.items():
        print(f"{word}: {count}")
