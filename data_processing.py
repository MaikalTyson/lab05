"""
A module that sorts and formats the data.
"""
import json
from typing import List
from movie import Movie

def sort_data(data: List[Movie]) -> List[Movie]:
    sorted_data = sorted(data, key=lambda movie: movie.rating, reverse=True)
    return sorted_data

def format_output(sorted_data: List[Movie], output_format: str) -> str:
    if output_format == 'json':
        output = json.dumps([movie.to_dict() for movie in sorted_data])
    elif output_format == 'csv':
        output = "title,rating\n"
        for movie in sorted_data:
            output += f"{movie.title},{movie.rating}\n"
    return output