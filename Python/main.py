number_list = []

for i in range(5):
    user_input = input("Enter an integer: ")
    number_list.append(user_input)

print("Your list: ", number_list)

def contains_duplicate(nums):
    return len(nums) != len(set(nums))



print("Has duplicate: ", contains_duplicate(number_list))
