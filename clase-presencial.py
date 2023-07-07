global numero_1
numero_1 = 20

def suma (arg1, arg2):
    numero_1 = arg2/arg1
    print(numero_1)

print(numero_1)
suma(1,1)
print(numero_1)

#################################

word = input("Say Something: ")

back= ""
for i in range(len(word)):
    back= word[i]+back

print(back)

################################

word= input("Say Something: ")

a= list(word)
a.reverse()

print(str(a))

