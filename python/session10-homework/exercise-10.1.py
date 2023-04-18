numLst = [1, 2, 3, 4, 5]
# point a
def fun_list_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + fun_list_sum(lst[1:])

print (fun_list_sum(numLst))

#point b using lambda

fun_list_sum_lambda = lambda lst: 0 if len(lst) == 0 else lst[0] + fun_list_sum_lambda(lst[1:])

lst = [1, 2, 3, 4, 5, 6, 7]
sum_lst = fun_list_sum_lambda(lst)
print(sum_lst)  # Output: 15
