from string import ascii_lowercase

class Round:
    def __init__(self, red, green, blue):
        self.red=red
        self.green=green
        self.blue=blue

class Game:
    def __init__(self, line):
        self.rounds=[]
        line=line[5:]
        colon_index=line.find(":")
        self.id=int(line[:colon_index])
        line=line[colon_index+2:]
        rounds=line.split(";")
        for r in rounds:
            if r[0]==" ":
                r=r[1:]
            values=r.split(",")
            red=0
            green=0
            blue=0
            for v in values:
                if v[0]==" ":
                    v=v[1:]
                space_index=v.find(" ")
                n=int(v[:space_index])
                if "red" in v:
                    red=n
                elif "green" in v:
                    green=n
                else:
                    blue=n
            self.rounds.append(Round(red, green, blue))

result=0
with open("inputs/day2input.txt") as file:
    for row in file:
        row=row.replace("\n", "")
        game=Game(row)
        red=-1
        green=-1
        blue=-1
        for r in game.rounds:
            if r.red>red:
                red=r.red
            if r.green>green:
                green=r.green
            if r.blue>blue:
                blue=r.blue
        p=red*green*blue
        result+=p
print(result)
