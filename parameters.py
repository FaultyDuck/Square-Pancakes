# parameters
def talk():
    print("hello")

talk()

def add(num1, num2):
    sum = num1 + num2
    print(sum)

add(5,5)

print("what") #print and return is different
#print prints the output but result returns back the result to whatever you called it from

def plus(n1, n2):
    sun = n1 + n2
    return sun

total = plus(6,6)
print(total)

def again(str1, str2):
    sting = str1 +" "+ str2
    return sting

ting = again("Apple", "Sauce")
print(ting)


sc1 = [3, 2, 20, 1, 0]
def lict(sc1): #dont forget to add "lict" in the function below
    us = sum(sc1)
    return us

sc2 = lict(sc1)
print(sc2)

#another way of adding lists
sc3 = [7, 10, 3, 0, 1] #define variable
def livt(sc3):
    sum = 0 #start from 0 and adding on to it from the loop using the for loop
    for num in sc3: #this for loop to add shit into the "sum" starting from 0 and into the list
        sum += num
    return sum #return the sum to finalize the product

tot = livt(sc3)
print(tot)