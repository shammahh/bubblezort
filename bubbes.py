

def bubbles(arr):
    for numCompare in range(len(arr) - 1, 0, -1):
        for i in range(numCompare):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
numbers = [8, 345, 74, 243, 64, 65, 224, 1,12, 4]
nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
###      0   1   2   3   4    5   6   7   8
print(bubbles(numbers))
print(bubbles(nums))
print(bubbles(words))