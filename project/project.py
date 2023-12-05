# 1. You need to add 3 more players for your stat comparison program.
# 2. You need to be able to print the names of the players once the comparison has been made. example: lebron is the better scorer compared to Kobe.
# 3. You need to write the function instructions for assists and rebounds. 


# this funciton wuill compare player overall career stats for scoring, rebounds, amd assists.
Lebron = ['28.9 ppg', ' 7.5 rpg','7.3apg']
Kobe = ['25.3 ppg', '5.2 rpg','4.7 apg']

Yao = ['19.0 ppg', ' 9.2 rpg', '1.8 apg']
Patrick = ['21.0 ppg', ' 9.8 apg',  '1.9 apg']
players=["LeBron James",  "Kobe Bryant"]

def playerComparison_scoring(playerA, playerB):
    print('points')
    if playerA > playerB:
        print('player a is better a scoring')
    elif playerA < playerB:
        print('player b is better at scoring.')
    elif playerA == playerB:
        print('they score the same')
        
def playerComparison_rebounds(playerA, playerB):
    print('rebounds')
def playerComparison_assists(playerA,playerB):   
    print('assists')

print('Welcome to the stat comparions program. This will compare two player career stats in ppg, rpg, apg')
playerA= input("please enter a players name: ")
playerB = input('please enter another players name: ')
statComp= input('what state would you like to compare? points, assists, and rebounds')

if playerA==players[0]:
    compare1=Lebron
elif playerA==players[1]:
    compare1=Kobe

if playerB==players[0]:
    compare2=Lebron
elif playerB==players[1]:
    compare2=Kobe

if playerA==players[0]:
      compare1=Yao 
elif playerA==players[1]:
      compare1=Patrick 

if playerB==players[0] :
     compare2=Patrick 
elif playerB==players[1]:
     compare2=Patrick

if statComp == 'points' :
    playerComparison_scoring(compare1[0],compare2[0])
elif statComp =='assists' :
    playerComparison_assists ()
if statComp == 'rebounds' :
    playerComparison_rebounds ()

if statComp == 'points':
    playerComparison_scoring(compare1[0],compare2[0])
elif statComp =='assists':
    playerComparison_assists()
elif statComp == 'rebounds':
    playerComparison_rebounds()

def playerTeam():
    if userAnswer == 'LeBron James':
        print('LeBron James, Los Angeles Lakers, jersey number 23')
        print('championships= 4, MVP=4')
    elif userAnswer =='Kobe Bryant':
        print('Kobe Bryant, Los Angeles Lakers, jersey number 24, 8')
    if userAnswer == 'Allen Iverson':
        print('Allen Iverson, 76sixer, jersey number 3')
    if userAnswer == 'Yao Ming':
        print('Yao Ming, Houston Rockets, jersey number 11')
    if userAnswer == 'Patrick Ewing':
        print('Patrick Ewing, New York Nicks, jersey number 33')
   
 



