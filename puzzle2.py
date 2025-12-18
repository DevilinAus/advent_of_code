with open("puzzle2_gift_shop_ids.txt", "r") as file:
    ids_raw = file.read()

ids_array = ids_raw.split(",")

# print(ids_array)

#NOTE CHECK THE LAST ENTRY IN THE ARRAY '187-382\n'] COULD CAUSE ISSUES.


invalid_ids = []
cycle = 0

ranges_array = []

def build_ranges_array():

    for item in ids_array:
        ranges = item.split("-")
        first_num = int(ranges[0])
        last_num = int(ranges[1])
        ranges_array.append((first_num, last_num))


def expand_ranges(item):
    start_num = item[0]
    end_num = item[1]

    current_num = start_num
    expanded_array = []

    for j in range(start_num, end_num+1):
        
        expanded_array.append(current_num)
        current_num += 1

    return expanded_array

def test_numbers(variable):

    for number in variable:
        number_str = str(number)
        number_length = len(number_str)
        if number_length % 2 == 0:
            print(cycle)

            section_one = number_str[0:number_length//2]
            section_two = number_str[(number_length//2):]

            print(f"S1: {section_one}")
            print(f"S2: {section_two}")

            # print(f"working on range: {first_num}-{last_num}") 
            # cycle += 1

            if section_one == section_two:
                invalid_ids.append(number)

def main():        
    #run once to build.        
    build_ranges_array()

    for item in ranges_array:
        test_numbers(expand_ranges(item))
        
    sum_of_invalids = 0
        
    for item in invalid_ids:
        sum_of_invalids = sum_of_invalids + item

    print(f"Sum of invalids is: {sum_of_invalids}")

main()

