```python
if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        size = int(input())
        arr = [int(x) for x in input().split()]
        alice = True
        while arr[0] != 0:
            index = arr.index(min(arr[1:]))
            if index == 0:
                index += 1
            arr[0] -= 1
            temp = arr[index]
            arr[index] = arr[0]
            arr[0] = temp
            alice = not alice
        alice = not alice
        print("Alice" if alice else "Bob")
```
