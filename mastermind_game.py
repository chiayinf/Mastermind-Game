'''
   CS5001
   Spring 2021
   Chiayin Fan
   Project: A python-turtule built mastermind game
'''
import turtle as t
import time
from Point import Point
from Marble import Marble
from GameControl import *
from count_bulls_and_cows import *

# Global parameter
screen = t.Screen()
printer = t.Turtle()
# Constant for the canvas to draw the background of the game
MARBLE_X_BUTTOM, MARBLE_Y_BUTTOM, MARBLE_DELTA_X = -280, -320, 45
ROW_MARKER_X, ROW_MARKER_Y, ROW_MARKER_DELTA_Y = -290, 378, 56
# Record the player's name
PLAYER_NAME = screen.textinput("CS5001 MasterMind", "Your name:")
# Colors for marbles
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
# Create a secret when a new game start, the code won't be changed
SECRET_CODE = [secret_code()]
# Constant for the canvas to draw the pegs
HINTBUTTON_X_Y = [20, 335]
# Constant for the canvas to draw the guess from player
LINE_X, LINE_Y, DELTA_LINE_Y, DELTA_LINE_X = -250, 310, -56, 70
# Constant for the canvas to draw the pegs from each guess, the relative positions of the 4 pegs
HINT_POSITION = [[0, 0], [20, 0], [0, -13], [20, -13]]
# Record all the guess uinput from the player
game = [Game([], [LINE_X, LINE_Y])]
# Colored guess buttons objects that allows a player to choose one color at a time for a guess
GUESS_BUTTOM = [Marble(Point(MARBLE_X_BUTTOM, MARBLE_Y_BUTTOM), "red"),
                Marble(Point(MARBLE_X_BUTTOM + MARBLE_DELTA_X, MARBLE_Y_BUTTOM), "blue"),
                Marble(Point(MARBLE_X_BUTTOM + 2 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM), "green"),
                Marble(Point(MARBLE_X_BUTTOM + 3 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM), "yellow"),
                Marble(Point(MARBLE_X_BUTTOM + 4 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM), "purple"),
                Marble(Point(MARBLE_X_BUTTOM + 5 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM), "black")]


def set_background():
    '''
    function: set_background, build up the assign window for the game
    parameter: None
    '''
    t.setup(635, 1000)
    t.penup()
    return


def raw_rectangle(start_x, start_y, color, width, length):
    '''
    function: raw_rectangle, draw a rectangle in assigned position with assigned color, width and length
    parameter: start_x: start x position of the turtle
               start_y: start y position of the turtle
               color: the color of the rectangle
               width: the width of the rectangle
    '''
    # Choose the assigned color
    t.color(color)
    # Pen up and go to the assigned position
    t.penup()
    t.goto(start_x, start_y)
    # Pen down and draw the rectangle with assigned width and length
    t.pendown()
    for _ in range(2):
        t.right(90)
        t.forward(length)
        t.right(90)
        t.forward(width)
    return


def draw_the_background():
    '''
    function: draw_the_background, draw the background
    parameter: None
    '''
    # Adjust the speend of the turtle
    t.speed(0)
    # Adjust the pensize
    t.pensize(5)
    # Draw 3 rectangles on the canvas
    raw_rectangle(90, 380, 'black', 400, 595)
    raw_rectangle(300, -225, 'black', 610, 150)
    raw_rectangle(300, 380, 'blue', 200, 595)
    t.penup()
    # Draw all the circles for player's guess
    y_guess = 365
    for i in range(10):
        draw_circle(ROW_MARKER_X, ROW_MARKER_Y-(i+1)*ROW_MARKER_DELTA_Y, 9, 'black')
        y_guess -= 55
        x_guess = -250
        for j in range(4):
            draw_circle(x_guess, y_guess, 20, 'black')
            x_guess += 70
        x_guess = 60
        y_guess += 25
        # Draw all the pegs
        for j in range(2):
            x_guess -= 40
            for k in range(2):
                draw_circle(x_guess, y_guess, 5, 'black')
                x_guess += 20
            y_guess -= 13


def insert_gif(x, y, gif_name):
    '''
    function: insert_gif, insert assigned gif to assigned location
    parameter: x: the x coordinate of the gif
               y: the y coordinate of the gif
    '''
    printer = t.Turtle()
    screen.addshape(gif_name)
    # Insert assigned gif to assigned location
    printer.shape(gif_name)
    printer.penup()
    printer.goto(x, y)
    return


def leader_board(winnerlist):
    '''
    function: leader_board, show the recorded leaderboard.txt on the canvas
    parameter: winnerlist: a list included score and winnername pairs
    '''
    printer.hideturtle()
    printer.penup()
    printer.goto(120, 290)
    # Write down 'Leaders:' on canvas
    printer.write("Leaders:\n", align="left", font=("times", 18, "bold"))
    name_x, name_y = 120, 270
    # Write down score and name on assigned position
    for score, name in winnerlist:
        printer.goto(name_x, name_y)
        printer.write(score + ': ' + name, align="left", font=("times", 16, "normal"))
        name_y -= 20


def draw_circle(circle_x, circle_y, radius, color):
    '''
   function: draw_circle, draw a colored circle on assigned position
   parameter: circle_x: x_coordinate for a circle
              circle_y: y_coordinate for a circle
              radius: radius of the circle
              color: color of the circle
   '''
    t.pensize(1)
    t.color(color)
    t.goto(circle_x, circle_y)
    t.pendown()
    t.circle(radius)
    t.penup()
    return


def write_msg(score, name):
    '''
    function: write_msg, add new record(score and name)
    parameter: score: the player's score
               name: the player's name
    '''
    # Open the leaderboard.txt in append mode
    with open("leaderboard.txt", "a") as outfile:
        # Add new record(score and name)
        outfile.write(str(score) + ' ' + name + '\n')
    return


def read_msg():
    '''
    function: read_msg, read the text on leaderboard.txt, if there is no such file, create one.
    parameter: None
    return: ranking: a sorted ranking list
    '''
    try:
        # Open the leaderboard.txt in read mode
        with open("leaderboard.txt", "r") as inFile:
            ranking = []
            # Append name and score to the ranking list
            for each in inFile:
                score, name = each.split(' ')
                ranking.append([score, name[:-1]])
            # Sort the ranking list so lower score comes first
            ranking.sort()
            # If there are more than 10 records, remove worse records. Only save the top ten record
            if len(ranking) > 3:
                ranking = ranking[:3]
            return ranking
    # Handle special case when leaderboard.txt doesn't exist
    except FileNotFoundError:
        # Pop up the error message gif
        pop_disappear_gif('leaderboard_error.gif')
        # Create a new txt called leaderboard.txt
        with open("leaderboard.txt", "a") as inFile:
            return []
    # Handle special case when leaderboard.txt is open
    except OSError:
        # Pop up the error message gif
        insert_gif(0, 0, 'file_error.gif')
        # The gif stays 2 seconds and close the app
        time.sleep(2)
        quit()
    except ValueError:
        # Pop up the error message gif
        insert_gif(0, 0, 'file_error.gif')
        # The gif stays 2 seconds and close the app
        time.sleep(2)
        quit()
    return


def draw_marbles():
    '''
    function: draw_marbles, draw colored guess buttons that allows a player to choose one color
              at a time for a guess
    parameter: None
    '''
    for i in range(len(GUESS_BUTTOM)):
        GUESS_BUTTOM[i].draw()
    return


def build_background():
    '''
    function: build_background, insert gif to assigned location
    parameter: None
    '''
    set_background()
    # Show the score and name of leaderboard area
    draw_the_background()
    winnerlist = read_msg()
    leader_board(winnerlist)
    return


def insert_special_buttin_gif():
    '''
    function: insert_special_buttin_gif, nsert the special function button gif to assigned position
    parameter: None
    '''
    insert_gif(200, -300, 'quit.gif')
    insert_gif(70, -300, 'xbutton.gif')
    insert_gif(5, -300, 'checkbutton.gif')
    return


def check_times(game):
    '''
    function: check_times, check how many rounds the player has, if more than 10, tell the player gameover.
    parameter: game: a list record how many rounds the player has
    '''
    # If player has played 10 rounds, tell the player his is lose and ask does she/he wants to play again.
    if len(game) == 11:
        # The Lose.gif pops up
        pop_disappear_gif('Lose.gif')
        screen.textinput("Secret code was", str(SECRET_CODE[-1]) + '\nEnter anything to close the answer window!')
        ask_play_again()


def remove_marble_mark():
    '''
    function: remove_marble_mark, remove the color the guess choose and fill in the marble with original color .
    parameter: None
    '''
    for i in range(len(game[-1].guess)):
        # If the x button is clicked, removed the guess record and the correspond color on the canvas
        game[-1].color_choice[-1].draw_empty()
        # Update the game record
        game[-1].color_choice.pop()
        game[-1].position[0] -= 70
        game[-1].guess.pop()


def remove_color_guess(game):
    '''
    function: remove_color_guess, remove all colors on canvas(except default buttons)
    param game: game, a list to record player's choices
    '''
    for i in range(len(game)):
        # Remove color of row marker
        Marble(Point(ROW_MARKER_X, ROW_MARKER_Y - (i + 1) * ROW_MARKER_DELTA_Y), "white", 9).draw()
        # Remove color of pegs
        for _ in range(len(HINT_POSITION)):
            Marble(Point(HINTBUTTON_X_Y[0] + HINT_POSITION[_][0], HINTBUTTON_X_Y[1] + HINT_POSITION[_][1] - 56 * i),
                   'white', 5).draw()
        # Remove color of player's choices
        for j in range(4):
            Marble(Point(LINE_X + j * DELTA_LINE_X, LINE_Y + i * DELTA_LINE_Y), 'white').draw()


def create_new_game(game):
    '''
    function: create_new_game, renew all record in game
    param game: game, a list to record player's choices
    '''
    # Remove the record in game
    for i in range(len(game)):
        game.pop()
    # Create a new secret code for the new game
    SECRET_CODE.append(secret_code())
    # Create the default setting for first round
    game.append(Game([], [LINE_X, LINE_Y + len(game) * DELTA_LINE_Y]))
    draw_marbles()
    # Remove the old leaderoard and update new informations
    printer.clear()
    winnerlist = read_msg()
    leader_board(winnerlist)


def ask_play_again():
    '''
    function: ask_play_again, ask whether the player wants to play again
    parameter: None
    '''
    # Pop uo to ask whether the player wants to play again
    play_again = screen.textinput("Do you want to play again?", \
                                  "Enter Y to start a new game. \nEnter anything else to leave the app!")
    # If yes, restart all the setting
    if play_again == "Y":
        remove_color_guess(game)
        create_new_game(game)
    # If not, leave the app
    else:
        quit()


def pop_disappear_gif(gif_name):
    '''
    function: pop_disappear_gif, pop up an assigned gif and remove it in 2 seconds
    :param gif_name: the name of the gif
    '''
    t.showturtle()
    screen.addshape(gif_name)
    t.goto(0, 0)
    t.shape(gif_name)
    # The gif stays 2 seconds and is removed from canvas
    time.sleep(2)
    t.hideturtle()


def get_click(x, y):
    '''
   function: get_click, trace player's movement to control the game flow
   parameter: x: x coordinate of the click
              y: y coordinate of the click
   '''
    # Build up all the special button objects
    marble_check = Marble(Point(MARBLE_X_BUTTOM + 6.31 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM - 3), "black", 25)
    marble_x = Marble(Point(MARBLE_X_BUTTOM + 7.8 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM - 3), "green", 25)
    marble_quit = Marble(Point(MARBLE_X_BUTTOM + 10.5 * MARBLE_DELTA_X, MARBLE_Y_BUTTOM - 24), "yellow", 50)
    # Index which is the current line
    Marble(Point(ROW_MARKER_X, ROW_MARKER_Y - len(game) * ROW_MARKER_DELTA_Y), "orange", 9).draw()
    # If the player click the quit button, quit gif pops up and the app close in 2 seconds
    if marble_quit.clicked_in_region(x, y):
        insert_gif(0, 0, 'quitmsg.gif')
        time.sleep(2)
        quit()
    # If the player click the x button, all the guess colors in the round would be removed.
    elif marble_x.clicked_in_region(x, y):
        remove_marble_mark()
        # Re-fill in the marbles in the bottom
        draw_marbles()
    # If there are less then 4 guess, check which color the player chooses.
    elif len(game[-1].guess) < 4:
        # Loop through all marble areas to check the correspond color
        for i in range(len(GUESS_BUTTOM)):
            # If the click is in assigned area and the color is not chosen
            if GUESS_BUTTOM[i].clicked_in_region(x, y) and GUESS_BUTTOM[i].color not in game[-1].guess:
                color_index = i
                # Add the color to the list
                game[-1].color_choice.append(
                    Marble(Point(game[-1].position[0], game[-1].position[1]), COLORS[color_index]))
                # Mark the color on the canvas
                game[-1].color_choice[-1].draw()
                # Record the color on game to trace what the player already has
                game[-1].guess.append(COLORS[color_index])
                # Removed the color on selected so the player won't choose it again
                GUESS_BUTTOM[color_index].draw_empty()
                # Update the position of the next guess
                game[-1].position[0] += 70
                break
    # If the player click the check button and 4 colors are chosen
    elif marble_check.clicked_in_region(x, y) and len(game[-1].guess) == 4:
        # Calculate the number of black and red pegs for this guess
        red, black = count_bulls_and_cows(SECRET_CODE[-1], game[-1].guess)
        hint_list = ['red'] * red + ['black'] * black
        # Update the position to correspond peg locations
        game[-1].position = [HINTBUTTON_X_Y[0], HINTBUTTON_X_Y[1] - (len(game) - 1) * 56]
        # Fill in the right color to pegs
        for i in range(len(hint_list)):
            Marble(Point(game[-1].position[0] + HINT_POSITION[i][0], game[-1].position[1] + HINT_POSITION[i][1]), \
                   hint_list[i], 5).draw()
        # If all the colors and positions are correct
        if hint_list == ['black', 'black', 'black', 'black']:
            # The winner.gif pops up
            pop_disappear_gif('winner.gif')
            # Record the score and the player's name to txt file
            write_msg(len(game), PLAYER_NAME)
            ask_play_again()
        # If player has wrong answer
        else:
            # Create a new GameControl object to trace the game
            game.append(Game([], [LINE_X, LINE_Y + len(game) * DELTA_LINE_Y]))
            # Check whether the player plays more than 10 rounds
            check_times(game)
            # Re-fill the color of the marbles
            draw_marbles()


def main():
    # Draw the background
    build_background()
    insert_special_buttin_gif()
    # Draw the marbles
    draw_marbles()
    # Trace the position that the player clicks and update the information
    screen.onclick(get_click)
    t.done()


if __name__ == "__main__":
    main()
