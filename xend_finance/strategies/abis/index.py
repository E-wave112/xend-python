import json
from pathlib import Path

# write a reusable function to get the json files
path = Path(__file__).parent / "./V2XAuto/xvAutoUSDTV2.json"
busd = json.loads(open(path,'r+').read())

def test_busd():
    return busd
print(test_busd())