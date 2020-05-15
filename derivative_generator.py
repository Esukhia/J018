'''
Takes a dir named "<project>-suggestions-unicode"
and generates following derivatives for Gregory:
- suggestions in wylie
- diplomatic in unicode
- diplomatic in wylie
'''
from pathlib import Path
from pyewts import pyewts
import re

# "<project>-<type>-<format>"
# "J018-diplomatic-unicode"

project = 'J018'
types = ['suggestions', 'diplomatic']
formats = ['unicode', 'wylie']


def derive(project, type, format):
    print(f'Deriving {project}-{type}-{format}...')
    path = Path(f'{project}-suggestions-unicode')
    for file in path.iterdir():
        text = file.read_text(encoding='utf-8')

        text = re.sub('\((.+?),.+?\)','\g<1>', text) if type == 'diplomatic' else text
        new_text = pyewts().toWylie(text) if format == 'wylie' else text
        new_path = Path(f'{project}-{type}-{format}')
        new_path.mkdir(parents=True, exist_ok=True)
        new_path = new_path / file.name
        new_path.touch()
        new_path.write_text(new_text, encoding='utf-8')

# suggestions in wylie
derive(project, types[0], formats[1])
# diplomatic in unicode
derive(project, types[1], formats[0])
# diplomatic in wylie
derive(project, types[1], formats[1])
