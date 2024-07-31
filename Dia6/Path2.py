from pathlib import Path


guia = Path(Path.cwd(),  'Europa')

for txt in Path(guia).glob('**/*.txt'):
    print(txt)


# ejercicio 1

from pathlib import Path

ruta_base = Path.home()

# ej 2
from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")

# ej 3
from pathlib import Path

ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")