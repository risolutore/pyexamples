"""
Cerca tutti i file PDF in un percorso specificato
"""

from os import PathLike
from pathlib import Path
import os

print("Cerca file pdf nel sistema.")
print()
user_path = input("Inserire un percorso valido: ")

pt = Path(user_path)

counter = 0

if pt.exists():
    for child in pt.iterdir():
        if child.is_file():
            fname, fextension = os.path.splitext(child)
            if fextension == '.pdf':
                counter += 1
                print(child)
    print()    
    print(f"Totale file trovati: {counter}")
else:
    print()
    print(f"Attenzione! '{user_path}' non è un percorso valido...")



