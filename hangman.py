def calculate_love_score(name1,name2):
    x=0
    y=0
    TR=("true")
    LV=("love")
    for letter in TR:
        if name1 == letter:
            x+=1
        if name2 == letter:
            y+=1
    print(x+y)
    for letter in LV:
        if name1 == letter:
            x+=1
        if name2 == letter:
            y+=1
    print(x+y)
calculate_love_score("Angela Yu","Jack Bauer")