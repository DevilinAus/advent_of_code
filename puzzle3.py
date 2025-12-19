def battery_check(line):

    first_num = 0
    second_num = 0
    best = 0

    digits = []
    for c in line:
        digits.append(int(c))
        
    #-1 since the last number can't be the first number in a two digit sequence.
    for i in range (len(digits) - 1):

        #find the first instance of the largest number
        if digits[i] > first_num:
            first_num = digits[i]

            #second number has to be to the right
            second_num = max(digits[i+1:]) 
    
        best = max(best, first_num * 10 + second_num)

    return best


def main():
    indiv_joltages = []

    with open("puzzle3_battery_joltages.txt", "r") as file:
        lines = [line.strip() for line in file]

    for line in lines:
        indiv_joltages.append(battery_check(line))

    total_joltage = sum(indiv_joltages)

    print(f"Result = {total_joltage}")

main()




