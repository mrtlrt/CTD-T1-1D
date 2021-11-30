import tkinter as tk
import random

countries_and_cities = {
		
	"Australia": ["Melbourne", "Sydney", "Brisbane", "Perth"],
	"Belgium": ["Brussels", "Beaumont", "Beringen", "Bree"],
	"Canada": ["Alberta", "British Columbia", "Manitoba", "Ontario"],
	"Denmark": ["Cophenhagen", "Aarhus", "Odense", "Aalborg"],
	"Egypt": ["Arish", "Badr", "Cairo", "Dahab"],
	"France": ["Paris", "Marseille", "Lyon", "Toulouse"],
	"Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
	"Hungary": ["Budapest", "Debrecen", "Szeged", "Miskolc"],
	"India": ["Chennai", "Bangalore", "Delhi", "Hyderabad"],
	"Japan": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
	"South Korea": ["Seoul", "Busan", "Incheon", "Daegu"],
	"Laos": ["Vientiane", "Savannakhet", "Pakse", "Phonsavan"],
	"Malaysia": ["George Town", "Kuala Lumpur", "Johor Bahru", "Shah Alam"],
	"New Zealand": ["Auckland", "Christchurch", "Wellington", "Hamilton"],
	"Poland": ["Warsaw", "Krakow", "Gdansk", "Sopot"],
	"Russia": ["Moscow", "Saint Petersburg", "Sochi", "Kazan"]

	}

countries_and_capitals = {

    "Australia": "Canberra", 
    "Belgium": "Brussels", 
    "Canada": "Ottawa", 
    "Denmark": "Copenhagen", 
    "Egypt": "Cairo", 
    "France": "Paris", 
    "Germany": "Berlin", 
    "Hungary": "Budapest", 
    "India": "New Delhi", 
    "Japan": "Tokyo", 
    "South Korea": "Seoul", 
    "Laos": "Vientiane", 
    "Malaysia": "Kuala Lumpur", 
    "New Zealand": "Wellington", 
    "Poland": "Warsaw", 
    "Russia": "Moscow"
    
    }

#todo: function to randomly pick 3 keys from a dictionary, then pick one key from those three keys for any length of that dictionary (no hardcoded values; should work on dictionaries with 1 or 8 or 9999 entries) - takes in DICT 1, returns one STRING chosen country, one LIST OF three STRINGS country options
def place_picker():

    import random
    countries_and_capitals = {"Australia": "Canberra", "Belgium": "Brussels", "Canada": "Ottawa", "Denmark": "Copenhagen", "Egypt": "Cairo", "France": "Paris", "Germany": "Berlin", "Hungary": "Budapest", "India": "New Delhi", "Japan": "Tokyo", "South Korea": "Seoul", "Laos": "Vientiane", "Malaysia": "Kuala Lumpur", "New Zealand": "Wellington", "Poland": "Warsaw", "Russia": "Moscow"}
    

    country1, capital1 = random.choice(list(countries_and_capitals.items()))
    country2, capital2 = random.choice(list(countries_and_capitals.items()))
    country3, capital3 = random.choice(list(countries_and_capitals.items()))

    random_countries_and_capitals = {country1:capital1, country2:capital2, country3:capital3}

    final_random_country, final_random_capital = random.choice(list(random_countries_and_capitals.items()))

    return (final_random_country, final_random_capital)
#todo: function to randomly choose a city from the 1st dictionary with a specified country - takes in DICT 1 and one STRING chosen country, returns one STRING chosen city
def random_city(countries_and_cities, chosen_country):
    city_random_choice = random.choice(list(countries_and_cities[chosen_country]))
    return city_random_choice
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
    rules = tk.Toplevel(screen)
    rules.title("Rules")
    rules.withdraw()
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
        rules.deiconify()
        welcome.withdraw()

    def quit():
        global quitgame
        quitgame = True
        screen.destroy()
        
    start = tk.Button(welcome, text="Play Game!", width=15, height=3, bg="black", fg="white", command=lambda:[start_game()])
    start.grid(row=3, column=0, padx=20, pady=10)

    exit = tk.Button(welcome, text="exit", command=quit)
    exit.grid(row=99, column=99)

    #* Rules Window

    def openrules():
        rules.deiconify()

    def closerules():
        rules.withdraw()

    rule = tk.Label(rules, text="Welcome to Around the World!\n\nIn this game, you will be given a city name; guess the country it belongs to and earn points, get it wrong and lose lives.\nAfter choosing the country it belongs to, tell us if it is its capital or not to earn bonus points!)")
    rule.grid(row=0, column=0, padx=10, pady=20)

    exitrules = tk.Button(rules, text="Close", command=closerules)
    exitrules.grid(row=1, column=0, padx=10, pady=10)
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
    # add_score = tk.Button(game, text="+1 to score", command=lambda *args:plusscore(score))
    # add_score.grid(row=0, column=1, padx=30, pady=30)
    #debug-

    #debug
    # add_score = tk.Button(game, text="-1 to life", command=lambda *args:minuslife(lives))
    # add_score.grid(row=1, column=1, padx=30, pady=30)
    #debug-

    openrule = tk.Button(game, text="Rules", command=openrules)
    openrule.grid(row=99, column=98)

    exitgame = tk.Button(game, text="Exit", command=quit)
    exitgame.grid(row=99, column=99)

    #* Game Over

    def replay():
        global quitgame
        quitgame = False
        screen.destroy()

    ask_replay = tk.Label(gameover, text="Game Over! Would you like to play again?")
    ask_replay.grid(row=0, column=0, columnspan=2, padx=40, pady=30)

    play_again = tk.Button(gameover, text="Play Again", command=replay)
    play_again.grid(row=1, column=0, padx=10, pady=10)

    exitgameover = tk.Button(gameover, text="Exit", command=quit)
    exitgameover.grid(row=1, column=1)

    screen.mainloop()

quitgame = False

while quitgame == False:
    main()
