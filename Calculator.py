import math
while True:
    def addition(x, y):
        ans = x + y
        return ans

    def subtraction(x, y):
        ans = x - y
        return ans

    def multiplication(x, y):
        ans = x * y
        return ans

    def division(x, y):
        try:
            ans = x / y
            return ans
        except ZeroDivisionError:
            print("Do not divide by zero!!")
        except:
            print("Unknown Error")

    def pythag(x, y):
        ans = (x ** 2) + (y ** 2)
        ans = math.sqrt(ans)
        ans = round(ans, 3)
        return ans

    func = input("What operator do you want to use?\nA. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Pythagoreans Theorem\n")
    func = func.upper()
    x = float(input("What is value A? "))
    y = float(input("What is value B? "))


    if func == "A":
        print(addition(x, y))
    elif func == "B":
        print(subtraction(x, y))
    elif func == "C":
        print(multiplication(x, y))
    elif func == "D":
        print(division(x, y))
    elif func == "E":
        print(pythag(x, y))