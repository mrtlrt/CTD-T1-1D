import tkinter as tk
import random

#todo: DICTIONARY 1 where keys = STRINGS country names as on wikipedia, values = LISTS OF STRINGS of major city names - at least 15 countries with 4 cities each.

#todo: DICTIONARY 2 where keys = STRINGS country names as on wikipedia (same as 1st dictionary), values = STRINGS of their capitals

#todo: function to randomly pick 3 keys from a dictionary, then pick one key from those three keys for any length of that dictionary (no hardcoded values; should work on dictionaries with 1 or 8 or 9999 entries) - takes in DICT 1, returns one STRING chosen country, one LIST OF three STRINGS country options

#todo: function to randomly choose a city from the 1st dictionary with a specified country - takes in DICT 1 and one STRING chosen country, returns one STRING chosen city

#todo: function to check whether the city chosen is the capital of the country specified or not - takes in DICT 2 and two STRINGS chosen country and chosen city, if chosen city is capital returns one BOOLEAN TRUE, otherwise FALSE

#todo: function to import a DICTIONARY from an external [scores.txt], then append an INTEGER to a LIST IN THE DICTIONARY where key = STRING player name, values = LIST of INTEGER previous scores - takes in one STRING playername, one INT score, writes to external file [scores.txt]

#todo: function to read a DICTIONARY from an external [scores.txt], then with the player name as a key, retrive the values of their highscores and check if the latest score is a highscore - takes in one STRING playername, one INT score, returns 1 LIST OF 3 INT SORTED highscores and if score is highscore returns one BOOLEAN TRUE, otherwise FALSE

def main():

    screen = tk.Tk()
    screen.title("root: do not close")
    screen.withdraw()
    game = tk.Toplevel(screen)
    game.title("Around the World with Team 4E")
    game.withdraw()
    welcome = tk.Toplevel(screen)
    welcome.title("Welcome")
    gameover = tk.Toplevel(screen)
    gameover.title("Game Over!")
    gameover.withdraw()

    lives = 5
    score = 0
    name = "foobar"

    #* Welcome popup

    title = tk.Label(welcome, text="Around the World with Team 4E")
    title.grid(row=0, column=0, padx=20, pady=5)

    askname = tk.Label(welcome, text="Enter Player Name:")
    askname.grid(row=1, column=0, padx=20, pady=10)

    get_name = tk.StringVar(value="Player")
    nameblank = tk.Entry(welcome, width=60, textvariable=get_name)
    nameblank.grid(row=2, column=0, padx=20, pady=1)

    def start_game():
        nonlocal name
        name = get_name.get()
        player_name.configure(text=f"Name: {name}")
        #debug print(name)
        game.deiconify()
        welcome.withdraw()

    def quit():
        global quitgame
        quitgame = True
        screen.destroy()
        
    start = tk.Button(welcome, text="Play Game!", width=15, height=3, bg="black", fg="white", command=lambda:[start_game()])
    start.grid(row=3, column=0, padx=20, pady=10)

    exit = tk.Button(welcome, text="exit", command=quit)
    exit.grid(row=99, column=99)

    #* Game start

    def plusscore(i):
        nonlocal score
        score = i + 1
        #debug
        #print(score)
        #debug-
        score_count.configure(text=f"Score: {score}")

    def minuslife(i):
        nonlocal lives
        lives = i - 1
        if lives <= 0:
            game.withdraw()
            gameover.deiconify()
        life_count.configure(text=f"Lives: {lives}")

    life_count = tk.Label(game, text=f"Lives: {lives}")
    life_count.grid(row=0, column=0, padx=2, pady=2)

    score_count = tk.Label(game, text=f"Score: {score}")
    score_count.grid(row=1, column=0, padx=2, pady=2)

    player_name = tk.Label(game, text=f"Name: Error")
    player_name.grid(row=2, column=0, padx=2, pady=2)

    #debug
    add_score = tk.Button(game, text="+1 to score", command=lambda *args:plusscore(score))
    add_score.grid(row=0, column=1, padx=30, pady=30)
    #debug-

    #debug
    add_score = tk.Button(game, text="-1 to life", command=lambda *args:minuslife(lives))
    add_score.grid(row=1, column=1, padx=30, pady=30)
    #debug-

    exit = tk.Button(game, text="exit", command=quit)
    exit.grid(row=99, column=99)

    #* Game Over

    def replay():
        global quitgame
        quitgame = False
        screen.destroy()

    ask_replay = tk.Label(gameover, text="Game Over! Would you like to play again?")
    ask_replay.grid(row=0, column=0, columnspan=2, padx=40, pady=30)

    play_again = tk.Button(gameover, text="Play Again", command=replay)
    play_again.grid(row=1, column=0, padx=10, pady=10)

    exit = tk.Button(gameover, text="Exit", command=quit)
    exit.grid(row=1, column=1)

    screen.mainloop()

quitgame = False

while quitgame == False:
    main()