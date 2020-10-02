# Python program to find the inique numbers in an array out
# of which two numbers occur exactly once and are distinct.
# You need to find the other two numbers and print them in ascending order.

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input().split(' ')[:n]))
    xors = 0
    for i in range(0, n):
        xors = xors ^ arr[i]
    xors = xors & ~(xors - 1)
    x = 0
    y = 0
    for i in range(0, n):
        if arr[i] & xors > 0:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    if x > y:
        swap(x, y)
    print("The distinct numbers are ", x, " and ", y)
