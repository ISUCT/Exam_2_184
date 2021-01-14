a = "5"
try:
    b = int(a)
    print(b+1)
    raise ZeroDivisionError()
except ValueError as err:
    print(f"Value error {err}")
except Exception as err:
    print(f"Common error {err}")


print("Normal continue")

def some_f(lst: tuple):
    lst.append(5)

c = [1,2,3,4]
print(c)
some_f(c)
print(c)

