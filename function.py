# def add(a,b):
#     return a+b

# print(add(3,5))
# ////////////


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(3,4))


#lambda arrguments: expression

# add = lambda x: x+10
# print(add(5))


# def add(a,b):
#     if a > 5:
#         b = b-2
#     return a+b

# add = lambda x,y: x+y
# print(add(5,6))


# function add(...args){

# }

var a = [1,2,3]
var b = ['c','f','d']
var c = [...a,...b]