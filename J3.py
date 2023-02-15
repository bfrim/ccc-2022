instructions = list(input())
letters = ""
loop = 0

for i in range(len(instructions)):
    if instructions[i] == "+" or instructions[i] == "-":
        integer = instructions[i + 1]

        if instructions[i] == "+":
            indication = "tighten"
        else:
            indication = "loosen"

        print(letters, indication, integer)
        letters = ""
        loop += 1
    else:
        if loop == 0:
            letters = "{}{}".format(letters, instructions[i])
        else:
            loop = 0
