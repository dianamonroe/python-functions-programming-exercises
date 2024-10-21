# Your code goes here:


def render_person(name, birth, eyes, age, gender):
    string = f'{name} is a {age} years old {gender} born in {birth} with {eyes} eyes'
    return string

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))

#more on how to concatenate parameters within a string  https://www.codeinu.net/language/python/c99077-how-to-insert-a-variable-into-a-string-without-breaking-up-the-string-in-python

name = "Dan"
age = 21
#you need to have that "f" before the string
name_and_age = f"My name is {name}, and I am {age} years old."
print(name_and_age)