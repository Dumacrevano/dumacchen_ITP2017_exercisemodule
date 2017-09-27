import time
from random import randint
def main():
    print("greetings")
    time.sleep(2)

    characters = ["Lamin","Arva","Dean","Samuel"]
    moves = ["Punch","Kick","Shoot","stab"]
    movesattk = [10, 15, 20, 25]

    def submain():
        characters = ["Lamin", "Arva", "Dean", "Samuel"]

        for n in range(0, len(characters)):
            print(n, ".", characters[n])

        p1 = characters.pop(int(input("Choose your character")))
        enemy = characters.pop(randint(0, len(characters)-1))

        print("Your character :", p1, "\nEnemy :", enemy)
        print("Battle")
        time.sleep(3)

        p1attk = 0
        enemyattk = 0
        rnd = 0
        while rnd < 4 :
            print("Your Turn")
            time.sleep(2)
            for n in range(0, len(moves)):
                print(n, ".", moves[n])
            x = int(input("Choose your move:"))
            p1attk = p1attk + randint(movesattk[x], movesattk[x]+5)
            print("Enemy's Turn")
            time.sleep(2)
            y = int(randint(0,len(moves)-1))
            enemyattk = enemyattk + randint(movesattk[y],movesattk[y]+5)
            rnd+=1
        print("Your Attack :", p1attk, "\nEnemy Attack :", enemyattk)
        if(p1attk > enemyattk):
            print("Congratulations,",p1, "won")
        elif(p1attk == enemyattk):
            print("Tie, Both of you died")
        else:
            print("You died,", enemy, "won")

    submain()
    x = input("Do you want to play again?(Y = yes, N = no)")
    if(x.upper() == "Y"):
        submain()
    else :
        print("Game Over")