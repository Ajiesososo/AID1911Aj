# {'name':[xxx,xxxxx]}
perso = {}

f = open('talk.txt', 'r')
n = 0
for each_line in f:
    n += 1
    # 不是空行的情况下
    if each_line != '\n':
        # solit(':',1) ：已第一个冒号为分割点
        # 将名字取出来
        name = each_line.split('：', 1)
        print(name)
        if name not in perso:  # 判断字典中是否存在相同的人名
            # 字典添加数据：字典名[键] = 数据
            perso[name] = [each_line]
            print(perso)
        else:
            perso[name].append(each_line)

# f.close()
#
# for name in person:
#     with open(name + '.txt', 'w') as fw:
#         fw.writelines(person[name])
