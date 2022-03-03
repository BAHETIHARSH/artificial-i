import json
strarr = '["z:0","A:-1"]'
lister = strarr.split(',')

dis = json.loads(strarr)
ans_dict = {}
for i in dis:
    list = i.split(":")
    ans_dict[list[0]] = ans_dict.get(list[0],0)+int(list[1])

print(ans_dict)
