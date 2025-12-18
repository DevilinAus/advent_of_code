with open("puzzle1_safe_codes.txt", "r") as file:
    lines = [line.strip() for line in file]

dial_instructions = []
for line in lines:
    dial_instructions.append((line[0],(int(line[1:]))))

# # #overwrite the dial instructions for testing
# dial_instructions = [("R", 100),("R", 25)]

dial_position = 50
zero_count = 0
DIAL_TOTAL_POSITIONS = 100

for instruction in dial_instructions:
    print(f"{instruction[0]} : {instruction[1]}")
    if instruction[0] == 'L':
        dial_position = (dial_position - instruction[1]) % DIAL_TOTAL_POSITIONS
    else: 
        dial_position = (dial_position + instruction[1]) % DIAL_TOTAL_POSITIONS

    print(f"dial posisiton is currently {dial_position}")

    if dial_position == 0:
        zero_count = zero_count + 1

# print(dial_position)
print(zero_count)


