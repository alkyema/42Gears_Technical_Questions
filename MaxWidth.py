words = ["42Gears","provide","secure","management","for","enterprise","devices."]
# words = ["Our","UEM","platform","works","across","Android","iOS","Windows","and","Linux"]

maxwidth = 20

# print(len(words))

s = ""

done = []

count = 0
group = {}

for i in range(len(words)):

    if words[i] in done:
        continue

    s = words[i]
    group[count] = [words[i]]
    done.append(words[i])

    for j in range(i+1,len(words)):

        if len(s+" "+words[j])<maxwidth:
            done.append(words[j])
            s = s + " " + words[j]
            print(len(s),s)
            group[count].append(words[j])
                
        else:
            count += 1
            s = ""
            break
        pass

newlist = []
temp = ""
final = ""
space = 1
for i,j in group.items():
    # print(j)
    for k in j:
        temp += k
    leng = maxwidth - len(temp)
    if len(j) == 1:
        space = leng
        final = j[0]+" "*space
    elif len(j) == 2:
        space = leng
        final = j[0]+" "*space+j[1]
    else:
        space = leng//len(j)
        final = ""
        for k in range(len(j)):
            if k == 0:
                final = j[k]
            else:
                final += " "*space + j[k] 
    newlist.append(final)
    space = 1
    temp = ""
print(group)
print(newlist)