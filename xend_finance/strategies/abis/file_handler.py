import json
from pathlib import Path


def read_abis(dir: str):
    """
    > Reads the JSON file at the given path and returns the data as a Python dictionary

    :param dir: The directory of the ABI file
    :type dir: str
    :return: A dictionary of the ABIs for the contracts
    """
    path = Path(__file__).parent / dir
    data = json.loads(open(path, "r+").read())
    return data
