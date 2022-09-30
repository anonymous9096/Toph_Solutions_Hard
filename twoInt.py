n = int(input())
if 1 <= n <= 100:
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        if 0 <= x and y <= 100000:
            print(f"Case #{i}:", x + y)

