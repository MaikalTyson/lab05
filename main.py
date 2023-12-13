"""
A CLI app, that outputs trending movies and tv shows, using The Movie Database API.
"""

from typing import List

from cli import load_cli
from api import fetch_data
from movie import Movie
from data_processing import sort_data, format_output

import asyncio


if __name__ == '__main__':
    media_type, time_period, output_format = load_cli()

    data = asyncio.run(fetch_data(media_type, time_period))
    sorted_data = sort_data(data)
    
    output = format_output(sorted_data, output_format)
    print(output)
