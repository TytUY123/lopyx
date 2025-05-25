try:
    a = int(input("введит первое число: "))
except ValueError:
    print(f"число пиши")

try:
    b = int(input("введит второе число: "))
except ValueError:
    print(f"число пиши")

c = input("теперь операцию(+, -, *, /) ")

if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "*":
    print(a * b)
try:
    if c == "/":
        print(a / b)
except ZeroDivisionError:
    print("На ноль делить нельзя")
