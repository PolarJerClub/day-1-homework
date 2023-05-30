# Question 1:

age_1 = int(input("Type age: "))
age_2 = int(input("Type another age:"))

print(abs(age_1) + abs(age_2))


# Question 2:

noun = input("Gimme a noun! ")
verb = input("Gimme a verb! ")
adjective = input("Gimme an adjective! ")

print(f"How many times do I have to tell this {adjective.upper()} {noun} we are not {verb} today!")


# Question 3:

age = int(input("Tell me your age: "))

if age < 18:
    print("kids")
elif age <= 65:
    print("adults")
else:
    print("seniors")


# Question 4:

num = int(input("Watch me square this number: "))

print(num**2)


# Question 5:

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

words = [word1, word2, word3, word4, word5]

for word in words:
    if len(word) > 5:
        print("True")
    else:
        print("False")