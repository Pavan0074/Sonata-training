def plgame(pl1, pl2):
    if (pl1 == pl2):
        print('tie game')
    elif (pl1 == 'rock' and pl2 == 'scissors') or (pl2 == 'paper' and pl1 == 'scissors') or (
            pl1 == 'paper' and pl2 == 'rock'):
        print('pl1 wins')
    elif (pl1 == 'rock' and pl2 == 'paper') or (pl1 == 'paper' and pl2 == 'scissors') or (
            pl1 == 'scissors' and pl2 == 'rock'):
        print('pl2 wins')
    else:
        print('provide valid input')


print('possible inputs : rock ,paper , scissors')
pl1 = input('enter your pl1 choice')
pl2 = input('enter your pl2 choice')
var = plgame(pl1, pl2)

