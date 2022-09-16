a, b, c = map(int, input("Enter a b c: ").split())

if a + b > c and b + c > a and c + a > b:
    print("YES")
else:
    print("NO")
