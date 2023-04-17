def groupList(lst, glength):
    groups = []
    group = []
    for i in range(len(lst)):
        group.append(lst[i])
        if len(group) == glength:
            groups.append(group)
            group = []
    if len(group) > 0:
        groups.append(group)
    return groups

list = [1, 2, 3, 4, 5, 6, 7, 8]

print(groupList(list, 2))
print(groupList(list, 3))
print(groupList(list, 4))