with open('input2.txt') as f:
    inputs = f.readlines()

#part one
xpos = 0
ypos = 0

for line in inputs:
    direction, units = line.split()
    if direction == 'forward':
        xpos += int(units)
    elif direction == 'up':
        ypos -= int(units)
    elif direction == 'down':
        ypos += int(units)
print("Part One:")
print("X: " + str(xpos) + " Y: " + str(ypos) + " Ans: " + str(xpos*ypos))

#part two
xpos = 0
ypos = 0
aim = 0

for line in inputs:
    direction, units = line.split()
    if direction == 'forward':
        xpos += int(units)
        ypos += int(units)*aim
    elif direction == 'up':
        aim -= int(units)
    elif direction == 'down':
        aim += int(units)

print("Part Two:")
print("X: " + str(xpos) + " Y: " + str(ypos) + " Ans: " + str(xpos*ypos))
