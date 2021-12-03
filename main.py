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

#todo: function to randomly choose a city from the 1st dictionary with a specified country - takes in DICT 1 and one STRING chosen country, returns one STRING chosen city

#todo: function to check whether the city chosen is the capital of the country specified or not - takes in DICT 2 and two STRINGS chosen country and chosen city, if chosen city is capital returns one BOOLEAN TRUE, otherwise FALSE

#todo: function to import a DICTIONARY from an external [scores.txt], then append an INTEGER to a LIST IN THE DICTIONARY where key = STRING player name, values = LIST of INTEGER previous scores - takes in one STRING playername, one INT score, writes to external file [scores.txt]

#todo: function to read a DICTIONARY from an external [scores.txt], then with the player name as a key, retrive the values of their highscores and check if the latest score is a highscore - takes in one STRING playername, one INT score, returns 1 LIST OF 3 INT SORTED highscores and if score is highscore returns one BOOLEAN TRUE, otherwise FALSE

def pick_3_cities(countries_and_cities):
    check_list = []
    length_dict = len(countries_and_cities)
    ran_int = 0
    
    country_to_choose = random.choice(list(countries_and_cities))
    length_choices = len(country_to_choose)
    ran_int = random.sample(range(length_choices), 3)

    for i in range(len(ran_int)):
        check_list.append(countries_and_cities[country_to_choose][i])
        
        
    return country_to_choose, check_list

def random_1_capital(countries_and_cities, country):
    capital = random.choice(countries_and_cities[country])
    return capital

def check_if_capital(countries_and_capitals, country, city):
    if(countries_and_capitals[country] == city):
        return True
    else:
        return False

def write_to_txt(name, score):
    scores_dict = {}
    dict_string = ""
    
    #Reads file and places values into dictionary
    file = open("scores.txt",'r+')
    for player in file:
        key, value = player.split()
        scores_dict[key] = value
    file.close()
    
    #Opens and clears file, then places new list of values inside
    fileW = open("scores.txt",'w')
    for key in scores_dict:
        if(name == key):
            scores_dict[key] = score
        dict_string = dict_string + key + " " + str(scores_dict[key]) + "\n"
    fileW.write(dict_string)
    file.close()

#Instead of reading a bunch of Highscores, why not just take the highest score out of everyone
def read_highscore():
    scores_dict = {}
    file = open("scores.txt",'r+')
    for player in file:
        key, value = player.split()
        scores_dict[key] = value
    file.close()
    
    max_key = max(scores_dict, key=scores_dict.get)
    return max_key

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
    chosen_city = "foobar"
    country_list = ["foobar", "foobar", "foobar"]

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
    life_count.grid(row=97, column=0, padx=2, pady=2)

    score_count = tk.Label(game, text=f"Score: {score}")
    score_count.grid(row=98, column=0, padx=2, pady=2)

    player_name = tk.Label(game, text=f"Name: {name}")
    player_name.grid(row=99, column=0, padx=2, pady=2)

    given_city = tk.Label(game, text=f"City: {chosen_city}") #todo obtain from random city choice
    given_city.grid(row=0, column=2, padx=60, pady=30)

    guess_1 = tk.Button(game, text=f"{country_list[0]}") #todo obtain from country list
    guess_1.grid(row=1, column=1, padx=10, pady=20)

    guess_2 = tk.Button(game, text=f"{country_list[1]}")
    guess_2.grid(row=1, column=2, padx=10, pady=20)

    guess_3 = tk.Button(game, text=f"{country_list[2]}")
    guess_3.grid(row=1, column=3, padx=10, pady=20)

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