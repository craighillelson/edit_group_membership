"""Create required files and directories."""

from pathlib import Path
import functions

required_directories = [
    'csvs',
    'output',
]


def make_output_dir(req_directory) -> Path:
    """Create required directories."""
    output_dir = Path('.') / f'{req_directory}'
    output_dir.mkdir(exist_ok=True)

    return output_dir


for directory in required_directories:
    make_output_dir(directory)

functions.update_user('\nrequired directories created successfully\n')
