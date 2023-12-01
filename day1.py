from string import ascii_letters

def check_for_number(text):
    numbers=["one", "two", "three", "four", "five", "six", "seven","eight","nine"]
    for n in numbers:
        if n in text:
            return n
    return ""

def replace_numbers(text):
    str_numbers={"one": "1", "two": "2", "three": "3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    while True:
        found_match=False
        cur=""
        for char in text:
            cur+=char
            n=check_for_number(cur)
            if n:
                text=text.replace(n, str_numbers[n])
        if not found_match:
            break
    return text


data=[]
with open("inputs/day1input.txt") as file:
    for row in file:
        row=row.replace("\n", "")
        data.append(row)
sum=0
strip=dict.fromkeys([ord(char) for char in ascii_letters], "")
for d in data:
    print("\n")
    print(d)
    as_numbers=replace_numbers(d)
    print(as_numbers)
    values=as_numbers.translate(strip)
    print(values)
    print(values[0]+values[-1])
    sum+=(int(values[0]+values[-1]))
print(sum)
