import random as ra
alpha = 0
character = 0
number = 0
char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
sp = ['!','@','#','$','%','^','&','*','(',')']
while True :
    try:
        total = int (input('total no of charactures in pasword:'))
    
        number = int (input('''you have ''' + str(total)+''' characr left
no of numbers in password :'''))
        if  total - number == 0 :
            print('ok! we will procide\n')
            break
        elif (total - number )< 0  : 
            print("sorry ! the value can't be taken \n")
            continue
        else:
            character = int(input('''you have '''+ str(total - number)+''' character left
how many no of special character you require :'''))
            if  total - (number +character) == 0 :
                print('ok! we will procide\n')
                break
            elif (total - (number+character )
                  )< 0  : 
                print("sorry ! the value can't be taken\n ")
                continue
            else:
                alpha = int (input('''you have '''+ str(total - (number + character ))+''' character left
how many no of alphabets you require :'''))
            if  total - (number + character+alpha ) == 0 :
                print('ok! we will procide\n')
                break
            elif  total - (number + character+alpha)< 0 : 
                print("sorry ! the value can't be taken \n")
                continue
            elif number + character+alpha != total :
                op =str(input(f'''the desired lentth of the code is not achived
the desired length :{total}
your length: {number + character+alpha}
if you want to continue type :y if not type :n to recreate it\n'''))
                if op.lower() == 'y':
                    break
                else:
                    continue
            else :
                print('smething went wrong !\n')
                continue
    except ValueError:
            print("Please enter numbers only!\n")
pas = []
if alpha != 0:
    while True :
        pas.append(ra.choice(char))
        if len(pas) < alpha :
            continue
        else :
            break
if number != 0 :
    while True :
        pas.append(str(ra.randint(1,9)))
        if len(pas) < (alpha + number) :
            continue
        else :
            reak
if character != 0 :
    while True :
        pas.append(ra.choice(sp))
        if len(pas) < (alpha + number + character) :
            continue
        else :
            break
final =''
ra.shuffle(pas)
for a in(pas):
    final += a
print (f'''hear is your password :{final}
fill free to try again ''')


