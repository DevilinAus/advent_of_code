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

def setup_number(all_number_array):

    for number in all_number_array:
        number_str = str(number)
        number_length = len(number_str)

        #call next function
        section_number(number_str, number_length)
        
def section_number(number_str, number_length):

    for digit_count in range (1, number_length):
        section = number_str[0:digit_count]

        test_section_against_number(number_str, number_length, section)

def test_section_against_number(number_str, number_length, section):

    #think section = 9 | full number is 99
    
    #test if it can even be valid, a section of 3 can't fill a number of 7 long perfectly. 
    if number_length % len(section) != 0:
        return False

    print(f"it'll fit {section} into {number_str}")
    status = True
    for chunk in range (0, number_length//len(section)):
        print(f"testing {section} against {number_str[chunk*len(section):chunk*len(section)+len(section)] }")
        if section != number_str[chunk*len(section):chunk*len(section)+len(section)]:
            return False
    
    if int(number_str) not in invalid_ids:
        invalid_ids.append(int(number_str))     

    return True
            

def main():        
    #run once to build.        
    build_ranges_array()

    for item in ranges_array:
        if setup_number(expand_ranges(item)):
            pass
            
            
        
    #delete me.    
    print(invalid_ids)

    sum_of_invalids = 0
        
    for item in invalid_ids:
        sum_of_invalids = sum_of_invalids + item

    print(f"Sum of invalids is: {sum_of_invalids}")

main()

