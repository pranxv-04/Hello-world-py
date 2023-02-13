s = input("Enter: ")

vowels = list("AEIOUaeiou")

w = s.split()

count0 = 0
count1 = 0

for i in w:
    if i[0] == "the" and i[i+1][0] in vowels:
        count0 += 1
    elif i[0] ==  "a" and i[i+1][0] not in vowels:
        count1 += 1
    else:
        continue

print(count0)
print(count1)


    

    


        


