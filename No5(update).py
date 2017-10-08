
import time
import random
def main():
    print("greetings")
    time.sleep(2)
    chara=["lamin","Arva","Dean","Samuel"]
    characters = {"Lamin":{"hp":100,"mp":120}
        ,"Arva":{"hp":90,"mp":130},
                  "Dean":{"hp":70,"mp":160},"Samuel":{"hp":130,"mp":80}}
    moves = {"Punch":20,"Kick":30,"Shoot":40,"stab":45}
    movesattk = [random.randint(5,15), random.randint(15,20), random.randint(20,25), random.randint(25,30)]


    def chara_choosing():

        for chara, chara_stat in characters.items():
            print("character available "+chara+"\nhp:"+str(chara_stat["hp"])+"\nmp:"+str(chara_stat["mp"]))

        p1=characters.pop(str.title(input("choose your character")))
#print(random.choice(list(characters.keys())))
        enemy=characters.pop(random.choice(list(characters.keys())))
        print("your character is")
        print(p1)
        print("your enemy")
        print(enemy)


    #chara_choosing()
        rnd=True
        while rnd:

            print("your turn")
            time.sleep(2)


            print("0.punch\n1.Kick\n2.shoot\n3.stab")
            choose_move=int(input("choose your moves"))
            enemy_move=int(random.randint(0,len(moves)))

            def attack_effect(x,move_m):
                    enemy["hp"]-=movesattk[x]
                    p1["mp"]-=moves[move_m]
                    print("enemy hp reduced by:"+str(movesattk[x])+"\nremaining Hp:"+str(enemy["hp"]))
                    print("your current mp is"+str(p1["mp"]))
            if p1 ["mp"]<=45:
                    print("not enough mana")
                    p1["mp"]+=50
            elif choose_move==0:
                    attack_effect(0,"Punch")
            elif choose_move==1:
                    attack_effect(1,"Kick")
            elif choose_move==2:
                    attack_effect(2,"Shoot")
            elif choose_move==3:
                    attack_effect(3,"stab")
            def enemy_attk_effect(y,move_m):
                    p1["hp"]-=movesattk[y]
                    enemy["mp"]-=moves[move_m]
                    print("your hp reduced by:"+str(movesattk[y])+"\nremaining Hp:"+str(p1["hp"]))
                    print("enemy current mp is"+str(enemy["mp"]))
            if enemy["mp"]<=45:
                print("enemy not enough mana")
                enemy["mp"]+=50
            elif enemy_move==0:
                    enemy_attk_effect(0,"Punch")
            elif enemy_move==1:
                    enemy_attk_effect(1,"Kick")
            elif enemy_move==2:
                    enemy_attk_effect(2,"Shoot")
            elif enemy_move==3:
                    enemy_attk_effect(3,"stab")
            if enemy["hp"]<=0 or p1["hp"]<=0:
                if enemy['hp']<=0:
                    print("you win")
                    rnd=False
                    return rnd
                if p1["hp"]:
                    print("enemy win, you lose")
                    rnd=False
                    return rnd


    chara_choosing()
    inp = str.upper(input("do you want to play again?y/n"))
    if inp == "Y":
        chara_choosing()
    if inp == "N":
        print("See u again")

main()






"""p1 = characters.pop(int(input("Choose your character")))
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
    if x.upper() == "Y":
        submain()
    else:
        print("Game Over")


main()
"""