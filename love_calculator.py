def calculate_love_score(name1,name2):
    x=0
    y=0
    TR=("true")
    LV=("love")
    for letter in TR:
        for position in name1:
            if position == letter:
                x+=1
        for position in name2:
            if position == letter:
                x+=1

    for letter in LV:
        for position in name1:
            if position == letter:
                y+=1
        for position in name2:
            if position == letter:
                y+=1

    print(10*x+y)
calculate_love_score("Angela Yu","Jack Bauer")