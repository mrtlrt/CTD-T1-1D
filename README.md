# Around the World with Team 4E

## Description

#### Scenario

A game aimed at the 10-14 year old cousins of one of our
group members, who has only been able to meet them online due
to travel restrictions enforced by COVID-19 (they live overseas).
The game is hence a pub-quiz style game meant for said cousins
to compete with each other and learn in the process, an idea taken from their competitive nature and general interest in geography.

#### Game Format

The game is presented as a sequentially generated series of
multiple-choice questions, where the player is given the name of
a city and three options; each the name of a country. The player
is then expected to pick the country the given city is in to earn
points. Should the player get the question correct, they will then
earn a chance to score a bonus point by telling the game if the
city given is said country's capital or not. A correct answer in
this bonus section earns an additional point, while a wrong
answer will see the point earned in the question removed. Players
may only get 5 main questions (capital questions excluded) wrong
before their score is then recorded and placed into a database
for future reference.

## Documentation

The game utilises the random and Tkinter libraries, for 
question generation and GUI generation respectively. The os
library is also utilised to check the program's local directory
for scorefile creation and updating.

##### main()

The main function containing the game's runtime; used for
restarting the program to allow players to play another
round without having to exit and reopen the game.

##### screen: tk.Tk()

The root window of the program, it is mainly used to instantiate
the program and keep it alive in the background while the game
runs. Is not used to display anything and is hidden throughout
the program's runtime.

##### game: tk.Toplevel(screen)

A toplevel widget containing the bulk of the game - code for
questions and answers reference and update this widget, as
well as the trackers for the player's lives, score and name.

##### welcome: tk.Toplevel(screen)

Another toplevel widget, this contains the welcome screen of
the game where the player enters their name; the play game
button in this widget is what reveals the **game** widget and
begins the game proper.

##### rules: tk.Toplevel(screen)

A simple toplevel widget containing basic instructions for
the player regarding gameplay - can be summoned during 
gameplay as and when needed.

##### gameover: tk.Toplevel(screen)

The final toplevel widget, this asks the player if they wish
to play the game again or exit the program altogether, as
well as displays highscores recorded in the local scores.txt.

##### start_game()

A function called in **welcome** when the play game button
is pressed, it calls the program to record the player's entered
name, closes the **welcome** widget, opens the **game** and
**rules** widgets, as well as populates the **game** widget
with the first question and options.

##### quit()

A function which can be called in all widgets by a quit button
except for **rules**, this function kills the root **screen**
window, killing all widgets, as well as killing off the main()
loop, terminating the entire game.

##### openrules()/closerules()

Functions which simply open and close the **rules** widget as
and when desired.

##### create_options()

The key function of the **game** widget, this function ties
together the functions used to generate the question city
as well as the answer countries, then updating the lower-level
widgets in **game** accordingly, updating the gamestate.

##### plusscore()/minusscore()

Updates the score counters used by the game as well as those
displayed to the player in the **game** widget.

##### minuslife()

Updates the life counters used by the game as well as those
displayed to the player in the **game** widget. Is also the
function that triggers the endgame sequence by means of an
internal check of the life counter: if it hits 0, **game**
is closed and **gameover** is brought up, ending gameplay.

##### test_answer(idx)

This function takes in the position index of the option
chosen by the player during the game for the main questions;
it then adds a point and starts the bonus question if the player 
was correct, or removes a life and starts the next question
if the player was not.

##### create_capital()

Updates the **game** widget to show the bonus question given if
the player got the main question correct.

##### test_capital(idx)

Similar to test_answer(), this function utilises the same logic
but for the bonus questions; with a point added for a correct
answer and a point deducted for a wrong one, then the generation
of the next main question irregardless of whether the player
got the bonus question right or wrong.

##### build_scorefile()

The first of two functions called right before the **gameover**
widget is pulled up, this function reads the local scores.txt
file and stores it into memory; after which it looks through
the data gathered, looking for the current player's name and
updates it if the player's name is not in the data or the
player has set a new highscore. The modified data is then
used to overwrite the scores.txt file for the game to process
next time around.

##### build_highscore()

The second function linked to **gameover**, this function reads
the now modified local scores.txt and updates the highscore
list depending on the data read, in descending order.