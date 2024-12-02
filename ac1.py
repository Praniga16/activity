from functools import reduce
def odd(x):
    return x%2==1
def even(x):
    return x%2==0
a_list=[1,2,3,4,5,6]
s_list=list(filter(odd,a_list))
t_list=list(filter(even,a_list))
print("LIST :",a_list)
print("ODD LIST:",s_list,"EVEN LIST:",t_list)
def sum1(x,y):
    return x+y
so_list=reduce(sum1,s_list)
te_list=reduce(sum1,t_list)
result=list(map(int,[so_list,te_list]))
print("SUM OF ODD AND EVEN NUMBERS:",result)
