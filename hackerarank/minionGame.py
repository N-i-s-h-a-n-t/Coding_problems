# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# Sample Input

# BANANA
# Sample Output

# Stuart 12

def minion_game(string):
    player = dict()
    player['Stuart'] = 0
    player['Kevin'] = 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            player['Kevin'] += len(string) - i
        else:
            player['Stuart'] += len(string) - i
    
    if player['Kevin'] > player['Stuart']:
        print('Kevin '+str(player['Kevin']))
    elif player['Kevin'] == player['Stuart']:
        print('Draw')
    else:
        print('Stuart '+str(player['Stuart']))


s = input()
minion_game(s)