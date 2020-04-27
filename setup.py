"""Create required files and directories."""

import csv
import functions
from pathlib import Path
import datetime

required_directories = [
    'csvs',
    'output',
]


def make_output_dir(a) -> Path:
    """Create required directories."""
    output_dir = Path('.') / f'{a}'
    output_dir.mkdir(exist_ok=True)

    return output_dir


for directory in required_directories:
    make_output_dir(directory)

functions.print_return()
functions.update_user('required directories created successfully')
