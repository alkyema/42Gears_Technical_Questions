a = "company--HR----Recuitment----payroll--Engineering----Backend----Frontend"
# a = "company--HR----Recuitment----payroll--Engineering----Backend----Frontend"

s = a.split("-")


lis = []
count = 0
json_dict = {}
json_dict[s[0]] = {} 
cur = ""
for i in range(len(s)):
    if s[i] != "":
        # print(s[i])
        if count == 1:
            cur = s[i]
            json_dict[s[0]][s[i]] = {}
            # print(json_dict,s[i])
            count = 0
        if count == 3:
            json_dict[s[0]][cur][s[i]] = {}
            # print(json_dict)
            count = 0
    else:
        count +=1
    pass



print(json_dict)