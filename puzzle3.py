def battery_check(line):
    test_bat = line
    print(test_bat)

    big_num = 0
    second_big_num = 0

    for i in range (len(test_bat)):

        if second_big_num > big_num:
            big_num, second_big_num = second_big_num, big_num

        current = int(test_bat[i])

        if current > second_big_num:
            # print(int(test_bat[i]))
            second_big_num = current

    joltage = str(big_num) + str(second_big_num)
    joltage_int = int(joltage)

    print(f"I think it's {joltage_int}")

    return joltage_int

    

def main():
    indiv_joltages = []
    max_joltage = 0

    with open("puzzle3_battery_joltages.txt", "r") as file:
        lines = [line.strip() for line in file]

    for line in lines:
        indiv_joltages.append(battery_check(line))

    print(indiv_joltages)

    for j in indiv_joltages:
        max_joltage = max_joltage + indiv_joltages[j]

    print(max_joltage)

main()