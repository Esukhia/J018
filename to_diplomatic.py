'''
Takes a dir named "<project>-suggestions-unicode"
and generates following derivatives for Gregory:
- suggestions in wylie
- diplomatic in unicode
- diplomatic in wylie
'''
from pathlib import Path
from pyewts import pyewts

# "<project>-<type>-<format>"
# "J018-diplomatic-unicode"

project = 'J018'
types = ['suggestions', 'diplomatic']
formats = ['unicode', 'wylie']


def derive(project, type, format):
    path = Path(f'{project}-suggestions-unicode')
    for file in path.iterdir():
        text = file.read_text(encoding='utf-8')
        new_text = pyewts().toWylie(text) if format == 'wylie' else text
        new_path = Path(f'{project}-{type}-{format}')
        new_path.mkdir(parents=True, exist_ok=True)
        new_path = new_path / file.name
        new_path.touch()
        new_path.write_text(new_text, encoding='utf-8')

# suggestions in wylie
derive(project, types[0], formats[1])
# diplomatic in unicode
# diplomatic in wylie
