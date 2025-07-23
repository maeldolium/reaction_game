import msvcrt
import time
import random

# print("Appuie sur une touche")
# touche = msvcrt.getch()

# print("Tu as appuyé sur :", touche)


def reaction_game():
    while True:

        # Début du jeu
        print("\nPrépare toi... Le signal peut apparaître à tout moment.")
        print("Appuie sur une touche dès qu'il apparaît.")
        print("\n")
        print("----")
        print("\n")

        # Mise en place du délai
        delai = random.uniform(1, 5)
        start_time = time.perf_counter()

        # Détection faux départ
        while time.perf_counter() - start_time < delai:
            if msvcrt.kbhit(): # touche a été pressée
                msvcrt.getch() # on le vide
                print("Faux départ ! Essaie encore.")
                break
        else:

            time.sleep(delai) # Pause pendant le temps aléatoire

            # Anti-spam
            while msvcrt.kbhit():
                msvcrt.getch()  # vide toutes les touches pressées avant

            print("> APPUI VITE !")
            debut = time.perf_counter()

            while not msvcrt.kbhit():
                pass

            msvcrt.getch()

            # touche = msvcrt.getch()
            fin = time.perf_counter()

            duree_ms = (fin - debut) * 1000
            print(f"Temps de réaction: {int(duree_ms)} ms")
            break


reaction_game()
