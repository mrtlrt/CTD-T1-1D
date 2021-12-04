import tkinter as tk
import random

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
    answer_country = "foobar"
    option_list = ["foobar", "foobar", "foobar"]
    question_city = "foobar"

    countries_cities = {
            
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

    countries_capitals = {

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
        score_count.configure(text=f"Score: {score}")
        life_count.configure(text=f"Lives: {lives}")
        create_options()
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

    rule = tk.Label(rules, text="Welcome to Around the World!\n\nIn this game, you will be given a city name; guess the country it belongs to and earn points, get it wrong and lose lives.\n\n\nBonus: For every correct answer, tell us if it is a capital city to double or lose your point!)")
    rule.grid(row=0, column=0, padx=10, pady=20)

    exitrules = tk.Button(rules, text="Close", command=closerules)
    exitrules.grid(row=1, column=0, padx=10, pady=10)
    #* Game start

    def create_options():

        nonlocal option_list
        nonlocal answer_country
        nonlocal question_city

        option_list = random.sample(sorted(countries_cities), 3)
        answer_country = random.choice(option_list)
        question_city = random.choice(countries_cities[answer_country])
        given_city.configure(text=f"City: {question_city}")
        guess_0.configure(text=f"{option_list[0]}", command=lambda *args:[test_answer(0)])
        guess_1.configure(text=f"{option_list[1]}", command=lambda *args:[test_answer(1)])
        guess_2.configure(text=f"{option_list[2]}", command=lambda *args:[test_answer(2)])
        
    def plusscore():

        nonlocal score

        score += 1
        score_count.configure(text=f"Score: {score}")

    def minusscore():

        nonlocal score

        score -= 1
        score_count.configure(text=f"Score: {score}")

    def minuslife():

        nonlocal lives

        lives -= 1

        if lives <= 0:
            build_scorefile(name, score)
            build_highscore()
            game.withdraw()
            gameover.deiconify()

        life_count.configure(text=f"Lives: {lives}")

    def test_answer(idx):

        if answer_country == option_list[idx]:
            plusscore()
            create_capital()
        else:
            minuslife()
            create_options()

    def create_capital():

        given_city.configure(text=f"Is {question_city} the capital of {answer_country}?")
        guess_0.configure(text="Yes", command=lambda *args:[test_capital(0)])
        guess_1.configure(text="Pass", command=lambda *args:[test_capital(1)])
        guess_2.configure(text="No", command=lambda *args:[test_capital(2)])

    def test_capital(idx):

        if question_city == countries_capitals[answer_country]:
            is_capital = True
        else:
            is_capital = False

        if (is_capital == True and idx == 0) or (is_capital == False and idx == 2):
            plusscore()
        elif (is_capital == False and idx == 0) or  (is_capital == True and idx == 2):
            minusscore()
        else:
            pass

        create_options()

    life_count = tk.Label(game, text=f"Lives: foobar")
    life_count.grid(row=97, column=0, padx=2, pady=2)

    score_count = tk.Label(game, text=f"Score: foobar")
    score_count.grid(row=98, column=0, padx=2, pady=2)

    player_name = tk.Label(game, text=f"Name: foobar")
    player_name.grid(row=99, column=0, padx=2, pady=2)

    given_city = tk.Label(game, text=f"City: foobar")
    given_city.grid(row=0, column=2, padx=60, pady=30)

    guess_0 = tk.Button(game, text=f"foobar")
    guess_0.grid(row=1, column=1, padx=10, pady=20)

    guess_1 = tk.Button(game, text=f"foobar")
    guess_1.grid(row=1, column=2, padx=10, pady=20)

    guess_2 = tk.Button(game, text=f"foobar")
    guess_2.grid(row=1, column=3, padx=10, pady=20)

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
    
    def build_scorefile(name, score):

        file_dict = {}
        dict_string = ""
        
        with open("scores.txt",'r') as file:

            read = file.read()
            parse_read = read.strip()
            read_list = parse_read.split("\n")

            if parse_read != "":
                for player in read_list:
                    key, value = player.split()
                    file_dict[key] = value

            if name not in file_dict:
                file_dict[name] = score
            
            file.close()

        with open("scores.txt",'w') as wfile:

            for key in file_dict:
                if (name == key) and (int(file_dict[key]) < score):
                    file_dict[key] = score
                dict_string = dict_string + key + " " + str(file_dict[key]) + "\n"

            wfile.write(dict_string)
            wfile.close()

    def build_highscore():

        hs_dict = {}
        highscores = []

        with open("scores.txt",'r') as file:

            read = file.read()
            parse_read = read.strip()
            read_list = parse_read.split("\n")

            if parse_read != "":
                for player in read_list:
                    key, value = player.split()
                    hs_dict[key] = value

            file.close()
        
        scorelist = sorted(hs_dict.values(), reverse=True)

        if len(scorelist) < 3:
            num_scores = len(scorelist)
        else:
            num_scores = 3

        for i in range(num_scores):
            for n in hs_dict:
                if hs_dict[n] == scorelist[i]:
                    highscores.append(f"{n}: {scorelist[i]}")

        if num_scores > 0:
            highscore_0.configure(text=highscores[0])
        
        if num_scores > 1:
            highscore_1.configure(text=highscores[1])
        
        if num_scores > 2:
            highscore_2.configure(text=highscores[2])

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

    highscore_title = tk.Label(gameover, text="Highscores", relief="ridge")
    highscore_title.grid(row=2, column=0, columnspan=2, padx=20, pady=50)

    highscore_0 = tk.Label(gameover, text="")
    highscore_0.grid(row=97, column=0, columnspan=2)

    highscore_1 = tk.Label(gameover, text="")
    highscore_1.grid(row=98, column=0, columnspan=2)

    highscore_2 = tk.Label(gameover, text="")
    highscore_2.grid(row=99, column=0, columnspan=2)

    screen.mainloop()

quitgame = False

while quitgame == False:
    main()