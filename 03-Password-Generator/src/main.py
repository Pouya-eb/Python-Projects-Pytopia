import random
import string
from abc import ABC, abstractmethod
import nltk

# downloading meaningful words
nltk.download('words')

class PasswordGenerator(ABC):
    """Base class for generating passwords"""
    @abstractmethod
    def generate(self) -> str:
        pass


class RandomPasswordGenerator(PasswordGenerator):
    """Class to generate a random password"""
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False ) -> None:
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """Generate a random password

        :return: random password
        """
        return ''.join(random.choice(self.characters) for _ in range(self.length))


class PinCodeGenerator(PasswordGenerator):
    """Class to generate a numeric password"""
    def __init__(self, length: int = 8) -> None:
        self.length = length

    def generate(self) -> str:
        """Generate a numeric password

        :return: numeric pin code
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))        


class MemorablePasswordGenerator(PasswordGenerator):
    """Class to generate a memorable password"""
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalization: bool = False,
        vocabulary : list[str] = None 
    ) -> None:
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        
        self.num_of_words = num_of_words
        self.separator = separator
        self.capitalization = capitalization
        self.vocabulary = vocabulary

    def generate(self) -> str:
        """Generate a password from given list

        :return: memorable password
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalization:
            password_words = [word.upper() for word in password_words]

        return self.separator.join(password_words)
    

if __name__ == "__main__":
    pass