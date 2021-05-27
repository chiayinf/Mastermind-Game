'''
   CS5001
   Spring 2021
   Chiayin Fan
   Project: A python-turtule built mastermind game
'''


def count_bulls_and_cows(secret_code, guess):
    '''
    function: count_bulls_and_cows: count how many black and red pegs the player has
    parameters: secret_code: 4 colors secret code list
                guess: 4 colors player guess list
    return: a 2-tuple (a tuple with two elements) \
            containing the number of bulls and cows by comparing with the secret code.
    '''
    # Red pegs meant a correct color but out of position, black pegs meant a correct color in the correct position.
    red, black = 0, 0
    # Loop through the secret code to check the correctness
    for i in range(len(secret_code)):
        # If the color and the position are correct, get one black peg
        if secret_code[i] == guess[i]:
            black += 1
        # If the color is correct but the position is not, get one red peg
        elif secret_code[i] in guess:
            red += 1
    return (red, black)


def write_msg(score, name):
    '''
    function: write_msg, add new record(score and name)
    parameter: score: the player's score
               name: the player's name
    '''
    # Open the leaderboard.txt in append mode
    with open("leaderboard_test.txt", "a") as outfile:
        # Add new record(score and name)
        outfile.write(str(score) + ' ' + name + '\n')


def read_msg():
    '''
    function: read_msg, read the text on leaderboard_test.txt,
              the same as read_msg in mastermind_game without turtle part
    parameter: None
    return: ranking: a sorted ranking list
    '''
    try:
        # Open the leaderboard.txt in read mode
        with open("leaderboard_test.txt", "r") as inFile:
            ranking = []
            # Append name and score to the ranking list
            for each in inFile:
                score, name = each.split(' ')
                ranking.append([score, name[:-1]])
            # Sort the ranking list so lower score comes first
            ranking.sort()
            # If there are more than 10 records, remove worse records. Only save the top ten record
            if len(ranking) > 10:
                ranking = ranking[:10]
        return ranking
    except OSError:
        print('An error happens')
