if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        size = int(input())
        arr = [int(x) for x in input().split()]
        minimum = min(arr[0],min(arr[1:]))
        if minimum == arr[0]:
            print("Bob")
        else:
            print("Alice")
