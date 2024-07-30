from pathlib import Path


guia = Path(Path.cwd(),  'Europa')

for txt in Path(guia).glob('**/*.txt'):
    print(txt)
