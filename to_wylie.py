'''
Converts all files in a folder to wylie
Saves them in a new folder
'''
from pathlib import Path
from pyewts import pyewts

# "<project>-<type>-<format>"
# "J018-diplomatic-unicode"

project = 'J018'
types = ['diplomatic', 'suggestions']
formats = ['unicode', 'wylie']
type = types[0]

path = Path(f'{project}-{type}-{formats[0]}')

for file in path.iterdir():
    text = file.read_text(encoding='utf-8')
    wylie = pyewts().toWylie(text)

    new_path = Path(f'{project}-{type}-{formats[1]}')
    new_path.mkdir(parents=True, exist_ok=True)
    new_path = new_path / file.name
    new_path.touch()
    new_path.write_text(wylie, encoding='utf-8')
