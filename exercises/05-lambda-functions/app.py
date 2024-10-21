# Your function here
def multiply(a,b):
    return a * b

multiply2 = lambda a, b : a * b
#así está mal!!! multiply = lambda a : a * b (le falta el argumento "b")


is_odd = lambda a : a % 2 != 0
#para comprobalor:
print(is_odd(2))