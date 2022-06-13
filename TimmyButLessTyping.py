# Chores

rsp = 0


laun = 0
bed = 0
dish = 0
weed = 0
lawn = 0
chim = 0
dog = 0
tax = 0
speedrun = 0
clout = 0

def laundry():
    global laun
    global clout
    print("You are doing the laundry")
    print()
    print('What do you do?')
    print('1 Put it all in')
    print('2 Seperate things by color')
    print('3 Try and see if you fit in the laundry machine')
    print('4 Put a phone in there and see what happens')
    rsp = int(input())
    if rsp == 1:
        print("Your mom finds out. You are never seen again")
        print()
        print("The End")
    elif rsp == 2:
        print("Congrats, you're normal")
        print()
        laun = 1
        chorelist()
    elif rsp == 3:
        print("The door locks and water starts splashing everywhere. You then start being hurtled in circles.")
        print('What do you do?')
        print('1 Panic')
        print('2 Vlog')
        print('3 Enjoy the ride')
        print('4 Drink the water')
        rsp = int(input())
        print('You "Went to sleep for a long time"')
        print()
        print('the end')
    elif rsp == 4:
        print("You happened to retreive recording. You post the video on (insert social media here) and go viral")
        print()
        laun = 1
        clout = 1
        chorelist()
    else:
        print("Bro can you not read? Let's try this again")
        laundry()

def makeBed():
    global bed
    print("You are making your bed")
    print()
    print('What do you do?')
    print('1 Throw the blanket over and call it a day')
    print('2 Re-tuck everything in')
    print('3 Have a nice jump on the bed')
    print('4 Go to bed, chores are for losers')
    rsp = int(input())
    if rsp == 1:
        print("Your mom wasn't to pleased with that and grounded your (insert profanity here)")
        print("How are you supposed to Live, Laugh, Love now?")
        print()
        print('end')
    elif rsp == 2:
        print("Congrats, you're normal")
        print()
        bed = 1
        chorelist()
    elif rsp == 3:
        print('One little Timmy jumping on the bed')
        print('Timmy fell off and bonked his head')
        print('Momma called the doctor and the doctor said')
        print('"Looks like Timmy here got a cervical fracture and will have to undergo imediate surgery"')
        print()
        print('end')
    elif rsp == 4:
        print("Good work lazy bones, now you've done it")
        print("Now you're never waking up")
    else:
        print("Bro can you not read? Let's try this again")
        makeBed()

def doingDishes():
    global dog
    global bed
    global speedrun
    global dish
    print("You are doing the dishes")
    print()
    print('What do you do?')
    print('1 Just rinse the dishes off')
    print('2 Take your time with it')
    print('3 Clean the dishes at an elevated pace')
    print('4 "Feed the dog"')
    rsp = int(input())
    if rsp == 1:
        print("You contracted bad food poisoning")
        print()
        print('end')
    elif rsp == 2:
        print("Congrats, you're normal")
        print()
        dish = 1
        chorelist()
    elif rsp == 3:
        print('Due to trying to be fast and the soap foam')
        print('You have stuck your hand into a sink full of knives')
        print()
        print('end')
    elif rsp == 4:
        print('Well now the dishes are "clean" and the dog is fed')
        print('No one will notice')
        speedrun = 1
        dog = 1
        dish = 1
        chorelist()
    else:
        print("Bro can you not read? Let's try this again")
        doingDishes()

def pullWeed():
    global weed
    print("You are pulling weeds")
    print()
    print('What do you do?')
    print('1 Burn the weeds')
    print('2 Eat the weeds')
    print('3 Sell the weeds')
    print('4 Dispose of the weeds like a normal human being')
    rsp = int(input())
    if rsp == 1:
        print("Turns out some of those weeds were poison ivy")
        print("Now you're itchy on the inside")
        print()
        print('end')
    elif rsp == 2:
        print("Turns out some of those weeds were poison ivy")
        print("Now you're itchy on the inside")
        print()
        print('end')
    elif rsp == 3:
        print("The local law inforcement didn't enjoy that one")
        print()
        print('end')
    elif rsp == 4:
        print("Congrats, you're normal")
        print()
        weed = 1
        chorelist()
    else:
        print("Bro can you not read? Let's try this again")
        pullWeed()

def mowLawn():
    global lawn
    print("You are mowing the law")
    print()
    print('What do you do?')
    print('1 Mow in a spiral')
    print('2 Mow in rows/collumns')
    print('3 Lower the deck and sign your work')
    print("4 Screw the lawn mower's motor strap that bad boy to your bike")
    rsp = int(input())
    if rsp == 1:
        print("Congrats, you're normal")
        print()
        lawn = 1
        chorelist()
    elif rsp == 2:
        print("Congrats, you're normal")
        print()
        lawn = 1
        chorelist()
    elif rsp == 3:
        print('"ThIS iS aGAinSt hoA RuLes"')
        print('Get fined a college tuition, nerd')
        print()
        print('end')
    elif rsp == 4:
        print('You drove your new "mini bike" into a tree, radical dude')
        print()
        print('end')
    else:
        print("Bro can you not read? Let's try this again")
        mowLawn()

def sweepChimney():
    global chim
    print("You are sweeping the chimney")
    print()
    print('What do you do?')
    print('1 Wait for the wind to die down before starting')
    print('2 Hire a professional')
    print("3 Wind's not important, start anyways")
    print('4 Ignore it, know one will know')
    rsp = int(input())
    if rsp == 1:
        print("Congrats, you're actually smart")
        print()
        chim = 1
        chorelist()
    elif rsp == 2:
        print('That was an extremely good call, however it did "cost an arm and a leg"')
        print()
        chim = 1
        chorelist()
    elif rsp == 3:
        print("Turns out Mary Poppins wasn't actually that inaccurate")
        print("Your 50lbs self got launched")
        print()
        print('end')
    elif rsp == 4:
        print('One cold winter in the very near future,')
        print('due to heavy carbon build up, an extremely large fire')
        print()
        print('end')
    else:
        print("Bro can you not read? Let's try this again")
        sweepChimney()

def feedDog():
    global dog
    print("You are feeding the dog (40lbs)")
    print()
    print('What do you do?')
    print('1 One scoop (1 cup)')
    print('2 Two scoops (2 cups)')
    print("3 Three scoops (3 cups)")
    print("4 Put the dog on a diet (no cups)")

    rsp = int(input())
    if rsp == 1:
        print("Too little food, but ok")
        print()
        dog = 1
        chorelist()
    elif rsp == 2:
        print('An actually decent amount of food, good job')
        print() 
        dog = 1
        chorelist()
    elif rsp == 3:
        print("Too much food, but ok")
        print() 
        dog = 1
        chorelist()
    elif rsp == 4:
        print("You are devoured, the dog's gotta eat")
        print()
        print("end")
    else:
        print("Bro can you not read? Let's try this again")
        feedDog()

def doTaxes():
    global tax
    print("You are doing taxes")
    print()
    print('What do you do?')
    print('1 Round up')
    print('2 Round down')
    print("3 Screw taxes")
    print('4 Verify your tax info on redit')
    rsp = int(input())
    if rsp == 1:
        print("Congrats, you've obtained a tax return")
        print('Hooray for adulting')
        print()
        tax = 1
        chorelist()
    elif rsp == 2:
        print('*knock knock*')
        print("Who's there?")
        print("The IRS")
        print("Shi-")
        print()
        print('end')
    elif rsp == 3:
        print('*knock knock*')
        print("Who's there?")
        print("The IRS")
        print("Shi-")
        print()
        print('end')
    elif rsp == 4:
        print('Congrats, you now have 13 new credit cards under your name')
        print('You will never finacially recover')
        print()
        print('end')
    else:
        doTaxes()

def chorelist():
    if laun == 1 and bed == 1 and dish == 1 and weed == 1 and lawn == 1 and chim == 1 and dog == 1 and tax == 1:
        print('Congrats, you have survived your chores')
        print("You diserve a metal")
        print()
        print()
        print()
        print()
        print("To bad I don't have one for you")
        if clout == 1:
            print('Maybe one of your followers has one')
        if speedrun == 1:
            print('Also nice time save bro')
        print("Well, later nerd")
    else:
        print('Pick a chore to do:')
    if laun == 0:
        print('1 Do the laundry')
    if bed == 0:
        print('2 Make your bed')
    if dish == 0:
        print('3 Do the dishes')
    if weed == 0:
        print('4 Pull weeds')
    if lawn == 0:    
        print('5 Mow the lawn')
    if chim == 0:    
        print('6 Sweep the chimney')
    if dog == 0:
        print('7 Feed the dog')
    if tax ==  0:
        print('8 File the taxes')
    rsp = int(input())
    if rsp == 1:
        if laun == 1:
            print('You have already done the laundry')
            print()
            chorelist()
        else:
            laundry()
    elif rsp == 2:
        if bed == 1:
            print('You have already made your bed')
            print()
            chorelist()
        else:
            makeBed()
    elif rsp == 3:
        if dish == 1:
            print('You have already done the dishes')
            print()
            chorelist()
        else:
            doingDishes()
    elif rsp == 4:
        if weed == 1:
            print('You have already pulled weeds')
            print()
            chorelist()
        else:
            pullWeed()
    elif rsp == 5:
        if lawn == 1:
            print('You have already mowed the lawn')
            print()
            chorelist()
        else:
            mowLawn()
    elif rsp == 6:
        if chim == 1:
            print('You have already swept the chimney')
            print()
            chorelist()
        else:
            sweepChimney()
    elif rsp == 7:
        if dog == 1:
            print('You have already fed the dog')
            print()
            chorelist()
        else:
            feedDog()
    elif rsp == 8:
        if tax == 1:
            print('You have already filed the taxes')
            print()
            chorelist()
        else:
            doTaxes()
    else:
        print("Bro can you not read? Let's try this again")
        chorelist()

print()
print("WARNING: TONED DOWN DARK HUMOR AND POSSIBLE SPELLING/GRAMMAR ERRORS AHEAD")
print("Your name is Timmy. You like cheese and you are 5 years old")
print('Your mother hands you a "small" list of chores to do')
print()
chorelist()
