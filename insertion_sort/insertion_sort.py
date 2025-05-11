import random


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        current = arr[i]
        j: int = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1
            print(".", end="", flush=True)
        arr[j + 1] = current
        print(":", end="", flush=True)


for n in range(1, 10):
    print(f"execution {n}:")
    num_list = [random.randint(1, 100) for _ in range(10)]
    print(f"\tBefore: {num_list}")
    insertion_sort(num_list)
    print(f"\n\tAfter:  {num_list}")
