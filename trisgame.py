import os

# Variabili globali del gioco
player1 = ''
player2 = ''
board_coords = ''
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ']


# cancelliamo lo schermo
def clear_screen():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


# resettiamo la tabella di gioco
def reset_board():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ', ' ']


# funzione di aggiornamento della tabella per ogni nuova coordinata
def write_new_board(carattere, coord):
    index = 0
    coords = {'a1':0, 'a2':3, 'a3':6, 'b1':1, 'b2':4, 'b3':7, 'c1':2, 'c2':5, 'c3':8}

    # Verificare se esiste la coordina inserita
    if coord in coords:
        index = coords[coord]
        if board[index] == ' ': # Verifico che la casella sia vuota
            board[index] = carattere

            print(f"""
                a   b   c
              -------------
            1 | {board[0]} | {board[1]} | {board[2]} |
              -------------
            2 | {board[3]} | {board[4]} | {board[5]} |
              -------------
            3 | {board[6]} | {board[7]} | {board[8]} |
              -------------
            """)
            return 'OK' # set tutto ok
        else:
            return 'COORD1' # se la casella non è vuota
    else:
        return 'COORD2' # se la coordinata inserita non esiste es: 'd45'

# una funzione per visualizzare la tabella corrente senza nessuna modifica
def write_current_board():
    print(f"""
                a   b   c
              -------------
            1 | {board[0]} | {board[1]} | {board[2]} |
              -------------
            2 | {board[3]} | {board[4]} | {board[5]} |
              -------------
            3 | {board[6]} | {board[7]} | {board[8]} |
              -------------
            """)
    
# funzione per verificare se c'è un vincitore
def winnner(counter, player1, player2):
    if counter < 8: # nel caso si siano superate il massimo di mosse che sono 9 possibili
        # controlliamo tutte le possibili combinazioni per ogni simbolo 'X' o 'O'
        #Esempio del primo if controlla la riga 1 della tabella:
        #  a  b  c
        #1[X][X][X]
        if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            print(f"Il vincitore è {player2}")
            return True
        elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            print(f"Il vincitore è {player1}")
            return True
        elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
            print(f"Congratulazioni {player2} ai vinto!")
            return True
        elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
            print(f"Congratulazioni {player2} ai vinto!")
            return True
        else:
            return False
    else:
        # Nel caso si sia superato il numero massimo di mosse - tutte le caselle sono piene e nessuno ha vinto
        print("Nessun Vincitore...")
        return True

# funzione di partenza che mostra una semplice descrizoine e aiuto su come inserire le coordinate
def game_start():
    clear_screen()
    print("*** Benvenuti nel gioco del TRIS ***")
    print("""
        a   b   c
      -------------
    1 |   |   |   |
      -------------
    2 |   |   |   |
      -------------
    3 |   |   |   |
      -------------
    """)
    print("Per inserire 'X' o 'O' usare le coordinate della tabella di gioco.")
    print("Esempio: 'a1' - 'b3' - 'c2'")
    value = input("Premere INVIO per continuare quando siete pronti...")

# funzione che inizializza i dati di gioco chiedendo ai giocatori loro nomi
def game_init():
    clear_screen()
    print("*** Benvenuti nel gioco del TRIS ***")
    print("""
        a   b   c
      -------------
    1 |   |   |   |
      -------------
    2 |   |   |   |
      -------------
    3 |   |   |   |
      -------------
    """)
    print("Per inserire 'X' o 'O' usare le coordinate della tabella di gioco.")
    print("Esempio: 'a1' - 'b3' - 'c2'")
    value = input("Premere INVIO per continuare...")

# funzione principale - loop del gioco
def game_loop():
    counter = 0
    # per gestire lo stato attuale del loop di gioco
    # lo scopo principale di questa variabile è di suddividere un singolo loop in più livelli
    # a seconda dello stato viene eseguito il codice per quello stato.
    STATE = 200 
    LAST_STATE = 200 # gestisce lo stato precedente del loop

    
    while True:
        print("*** Gioco del TRIS ***")
        print()

        if STATE == 200: # loop del giocatore 1
            print(f"{player1} inserisci le coordinate della casella dove mettere la X.")
            board_coords = input("? ")
            clear_screen()
            risultato1 = write_new_board('X', board_coords)
            if risultato1 == 'OK':
                LAST_STATE = 200
                STATE = 300
            elif risultato1 == 'COORD1':
                clear_screen()
                print(f"* La casella scelta è già occupata *")
                print()
            elif risultato1 == 'COORD2':
                clear_screen()
                print(f"* La coordinata {board_coords} non è valida *")
                print()
        
        elif STATE == 250: # loop del giocatore 2
            print(f"{player2} inserisci le coordinate della casella dove mettere la O.")
            board_coords = input("? ")
            risultato2 = write_new_board('O', board_coords)
            if risultato2 == 'OK':
                LAST_STATE = 250
                STATE = 300
            elif risultato2 == 'COORD1':
                clear_screen()
                print(f"* La casella scelta è già occupata *")
                print()
            elif risultato2 == 'COORD2':
                clear_screen()
                print(f"* La coordinata {board_coords} non è valida *")
                print()
        
        elif STATE == 300: # vediamo se c'è un vincitore
            if not winnner(counter, player1, player2):
                counter += 1           
                clear_screen()
                write_current_board()
                # last_state serve per verificare quale giocvatore è stato l'ultimo a fare la sua mossa
                if LAST_STATE == 200: # se l'ultimo era giocatore 1
                    STATE = 250 # allora tocca a giocatore 2
                else:
                    STATE = 200 # altrimenti tocca a giocatore 1
            else:
                break


    print("Ciao\n")



game_start()
game_init()
game_loop()

