from typing import List


def two_sum_n_two(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]

def two_sum_n(nums: List[int], target: int) -> List[int]:  
    memory = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in memory:
            return [memory[diff], i]
        memory[n] = i

def main():
    nums = [2,7,11,15]
    target = 9

    print(two_sum_n_two(nums, target))
    print(two_sum_n(nums, target))


if __name__ == "__main__":
    main()
