def contains_duplicate(nums):
    return len(nums) != len(set(nums))

def main(): 
    number_list = []

    for i in range(5):
        user_input = input("Enter an integer: ")
        number_list.append(user_input)

    print("Your list: ", number_list)
    print("List contains duplicate!" if contains_duplicate(number_list) else "There is no duplicate!")


if __name__ == "__main__":
    main()
