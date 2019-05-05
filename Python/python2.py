a = 234
b = "asdf"

print(a)
print(b)

str1 = "Hello World"
print(str1[0])
print(str1[1])

print(str1[1:7])
print(str1[:3])
print(str1[3:])


print("The result is {} from patient {}".format(a, b))
print(f"The result is {a} from patient {b}")

myNumber = int(input("Please enter your age:"))
print(myNumber + 5)
print(type(myNumber))


weight = 75.5
print(type(weight))

if myNumber > 200:
    print("you're quite old")
    print("Try to eat healthier food")
else:
    print("you're young")

myList = ["Andreas", 54, 56.8, 8, False]
print(myList)
print(myList[1])
print(myList[2:4])


tinyDict = {"name":"Andreas",
            "age":"60",
            "dept":"Digital Healthcare"}
print(tinyDict["age"])

counter = 0
while counter < myNumber:
    print(f"Counting... {counter}")
    counter = counter + 1

print(counter)

for curElement in myList:
    print(f"Current element: {curElement}")

def plus(a, b):
    print("Inside function")
    result = a + b
    return result

print(plus(5, 4))
print(plus(a = 2, b = 3))
print(plus(b = 5, a = 3))