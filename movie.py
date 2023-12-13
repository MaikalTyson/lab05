"""
Class representing a movie or a tv show
"""

class Movie:
    def __init__(self, title:str , rating: float = 0.0):
        self.__title = title
        self.__rating = rating

    @property
    def title(self) -> str:
        return self.__title

    @property
    def rating(self) -> float:
        return self.__rating

    def to_dict(self):
        return {
            'title': self.__title,
            'rating': self.__rating
        }

    def __str__(self) -> str:
        return f'{self.__title}: {self.__rating}'
