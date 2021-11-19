"""
Il ROT-13 è un semplice cifrario monoalfabetico, 
in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
"""


alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("Menu di selezione:")
print("** 1) se vuoi cifrare un testo")
print("** 2) se vuoi decifrare un testo")

selezione = input("selezione? ")
print()

if int(selezione) not in [1, 2]:
    print("Attenzione la scelta eseguita non corrisponde a nessuna azione.")
else:
    if selezione == '1':
        print("Si è scelto di CODIFICARE un testo.")
        print()
        testo = input("Inserisci il testo: ")
        nuovo_testo = ""

        for i in range(0, len(testo)):
            ch = testo[i].lower()
            if ch != ' ':
                index = alfabeto.index(ch)
                total = index + 13

                if total <= 25:
                    ch = alfabeto[total]
                    nuovo_testo += ch
                else:
                    rest = total - 25
                    ch = alfabeto[rest - 1]
                    nuovo_testo += ch
            else:
                nuovo_testo += ' '

        print("Codifica eseguita:")
        print()
        print("Originale: ")
        print(testo)
        print()
        print("Codificato:")
        print(nuovo_testo)
    else:
        print("Si è scelto di DECODIFICARE un testo.")
        print()
        testo = input("Inserisci il testo: ")
        nuovo_testo = ""

        for i in range(0, len(testo)):
            ch = testo[i].lower()
            if ch != ' ':
                index = alfabeto.index(ch)
                total = index - 13

                if total <= 25:
                    ch = alfabeto[total]
                    nuovo_testo += ch
                else:
                    rest = total - 25
                    ch = alfabeto[rest - 1]
                    nuovo_testo += ch
            else:
                nuovo_testo += ' '

        print("Codifica eseguita:")
        print()
        print("Originale: ")
        print(testo)
        print()
        print("Codificato:")
        print(nuovo_testo)

