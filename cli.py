"""
CLI module for the app
"""

import sys

if len(sys.argv) != 4:
    print("Usage: python main.py <media_type> <time_period> <output_format>")
    sys.exit(1)

def load_cli():
    valid_media_types = ['movie', 'tv']
    valid_time_periods = ['day', 'week']
    valid_output_formats = ['json', 'csv']

    media_type = sys.argv[1]
    if media_type not in valid_media_types:
        raise ValueError(f"Invalid media type. Expected one of {valid_media_types}")

    time_period = sys.argv[2]
    if time_period not in valid_time_periods:
        raise ValueError(f"Invalid time period. Expected one of {valid_time_periods}")

    output_format = sys.argv[3]
    if output_format not in valid_output_formats:
        raise ValueError(f"Invalid output format. Expected one of {valid_output_formats}")

    return media_type, time_period, output_format