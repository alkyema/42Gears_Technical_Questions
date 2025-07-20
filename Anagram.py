# s = "ab#ba#@b#a@#b@#c#c@#!!##!!#!!"
# s = "one#two#three#four#five"
# s = "Hello#oHell#lloHe#world#dlrow#WORLd#abc#bca#ABC"
# s = "#abc##cab###bca####123#321#231###!!@@##@@!!"
s = "tar#rat#art#car#arc#cra#abc#bca#cab#xyz#zxy"

a = s.split("#")

for i in range(len(a)-1,-1,-1):
    if a[i] == "":
        a.pop(i)


word = {}

c = 0

for i in range(len(a)):

    if c>0 and a[i] in word[c-1]:

        continue

    lis = []
    lis.append(a[i])
    for j in range(i+1, len(a)):

        count = 0
        b = list(x for x in a[i])
        
        for k in b:
            if k in a[j]:
                count +=1
        if count == len(b) and len(lis[0]) == len(a[j]):

            lis.append(a[j])

    if len(lis) == 1:
        continue
    else:
        word[c] = lis
        c +=1
    

for i,j in word.items():
    
    for k in range(len(j)):    
        for l in range(k+1,len(j)):

            if j[l]<j[k]:
                temp = j[l]
                j[l] = j[k]
                j[k] = temp

    word[i] = j
    
    
arranged_word = {}


for i in range(len(word.keys())):

    for j in range(i+1,len(word.keys())):
        if word[j][0] < word[i][0]:
            temp = word[i]
            word[i] = word[j]
            word[j] = temp

for i,j in word.items():
    print(j)