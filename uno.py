import random as rd
#player and bot arrays and winner
player = []
bot = []
winner = 0 # winner  1 is player and 2 is bot winner
#cards
cards = ["y6","b9","y2","b7","g6","g7","r0","yd","r8","br","r5","rr","gd","r1","wc","b6","b6","y8","rs","g4","r9","bd","g1","y1","y7","d4","r6","y3","y5","y5","r2","g5","g0","b3","wc","r1","gr","d4","r4","rs","r2","r3","b1","br","y1","b4","g2","r7","y7","bd","y8","b9","ys","b5","y9","gd","b3","gr","rd","y4","rd","ys","bs","g9","b5","r5","y2","g5","wc","d4","g4","rr","y3","d4","b8","y6","r8","gs","y0","yr","g2","g3","y9","b1","y4","g8","g6","gs","r7","b7","yr","r9","r3","g8","b4","r6","wc","bs","b0","b2","g9","g3","b2","r4","g7","b8","g1","yd"]
#current_card and player_select cards
cc = ''
ps = ''
#Number of cards left in deck
NOC = 107
#WILD CARD COLOR PICKING FUNCTION
def colorpick():
    color = input("Enter your preferred color: ")
    return color[0]+'z'
#REMOVE FROM DECK FUNCTION
def remfromdeck(card):
    global cards
    cards.remove(card)
    global NOC
    NOC -= 1
#BOTPLAY FUNCTION
def BP():
    global bot
    global cc
    bc = ''
    bp = 0
    for i in bot:
        if(i[0] is cc[0] and bp<=2):
            bp = 2
            bc = i
        elif i[1] is cc[1] and bp <= 1:
            bp = 1
            bc = i
        elif bp==0 and (i[0] is 'd' or i[0] is 'w'):
            bc = i
            bp = -1
    if bp == 0:
        PCB()
        return 0
    if(bc[0] is 'd'):
        bot.remove(bc[:])
        PCP()
        PCP()
        PCP()
        PCP()
        for i in bot:
            if i[0] is 'y' or i[0] is 'r' or i[0] is 'g' or i[0] is 'b':
                cc = i[0]+'z'
                break
        print("Bot played Draw4 with color "+cc[0]+", So it will play again...")
        BP()
        return 0
    elif(bc[0] is 'w'):
        bot.remove(bc[:])
        for i in bot:
            if i[0] is 'y' or i[0] is 'r' or i[0] is 'g' or i[0] is 'b':
                cc = i[0]+'z'
                break
        print("Bot played Wild with color "+cc[0])
    elif bc[1] is 'd':
        bot.remove(bc[:])
        PCP()
        PCP()
        cc = bc
        print("Bot played "+bc+", So it will play again...")
        BP()
        return 0
    elif bc[1] is 'r' or bc[1] is 's':
        bot.remove(bc[:])
        cc = bc
        print("Bot played "+bc+", So it will play again...")
        BP()
        return 0
    else:
        bot.remove(bc[:])
        cc = bc
        print("Bot played "+bc)
    print("Bot has "+str(len(bot))+" cards")

#PLAYER CARD VALIDATION FUNCTION
def VPS():
    global player
    global cc
    global ps
    flag = 0
    if(ps[0] is 'd' or ps[0] is 'w' or ps[1] is 'd'):
        flag = 0
    elif(ps[0] is not cc[0] and ps[1] is not cc[1]):
        flag = 1
    else:
        flag = 0
    return flag
#PLAYER CARD DISPLAY AND SELECT FUNCTION
def PS():
    global cc
    global winner
    global ps
    global player
    flag = 0
    print("\nCurrent card on deck is "+cc)
    print("Your cards are: ",end='')
    for i in player:
        print(i+" ",end='')
    ps = input("\nWhat would you like to pick: ")
    try:
        if ps[0] is 'p':
            #if player doesnt have the card,he will pick.. validate this too
            PCP()
            #BP()
            return 0
        elif ps[0] is 'b' and ps[1] is 'p' and ps[2] is 'q':
            winner = 1
            return 0
    except IndexError:
        ()
    while((ps in player)!=True):
        ps = input("Choose a card from your deck: ")
    flag = VPS()
    if flag == 0:
        if(ps[0] is 'd'):
            PCB()
            PCB()
            PCB()
            PCB()
            cc = colorpick()
            player.remove(ps[:])
            print("Your chance again")
            PS()
        elif(ps[1] is 'd'):
            PCB()
            PCB()
            cc = ps[:]
            player.remove(ps[:])
            PS()
        elif(ps[0] is 'w'):
            cc = colorpick()
            player.remove(ps[:])
        elif(ps[1] is 'r' or ps[1] is 's'):
            cc = ps[:]
            print("r played")
            player.remove(ps[:])
            PS()
        else:
            cc = ps[:]
            player.remove(ps[:])
    elif flag == 1:
        PS()
#PICK CARD BOT AND PLAYER FUNCTION
def PCB():
    global cards
    global bot
    global NOC
    bot.append(cards[rd.randint(0,NOC)])
    remfromdeck(bot[-1])
def PCP():
    global cards
    global player
    global NOC
    player.append(cards[rd.randint(0,NOC)])
    remfromdeck(player[-1][:])
#MAIN FUNCTION
def main():
    global cards
    global winner
    global NOC
    global cc
    global player
    global bot
    global ps
    rd.shuffle(cards)
    for i in range(7):
        player.append(cards[rd.randint(0,NOC)])
        remfromdeck(player[i][:])
        bot.append(cards[rd.randint(0,NOC)])
        remfromdeck(bot[i][:])
    player.sort()
    bot.sort()
    cc = cards[rd.randint(0,NOC)]
    remfromdeck(cc[:])
    while (winner != 1 and winner != 2):
        PS()
        BP()
        if len(player) == 0:
            winner = 1
        elif len(bot) == 0:
            winner = 2
    if winner==1:
        print("\nYay, You won!")
    elif winner==2:
        print("\nBoo, You lost!")

if __name__ == "__main__":
    main()
