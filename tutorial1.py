# 2020/03/19 複習
'''
##########################################
print('列印中文測試')

list = [11, 12, 55] + [4, 1, 2]  # list相加= 串在一起[11, 12, 55, 4, 1, 2]
print(list)

ironman_groups_list = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security"]
ironman_groups_tuple = tuple(ironman_groups_list)  # tuple = tuple 不可變動的list

# 新增一個元素 List用中括號、Dictionary用大括號，Tuple則是使用小括號 python 三種容器型態
ironman_groups_list.insert(5, "自我挑戰組")
print(ironman_groups_list)
print(ironman_groups_tuple)
# ironman_groups_tuple.insert(5, "自我挑戰組")

##########################################
'''



#2020/03/23
'''
##########################################
participated_group = "Big Data"
current_ttl_articles = 4
is_participating = True

# 建立 dictionary
my_status = {
    "group": participated_group,
    "ttl_articles": current_ttl_articles,
    "is_participating": is_participating
}

# 利用鍵值選擇元素
print(my_status[0])
print(my_status["ttl_articles"])
print(my_status["is_participating"])

##########################################
'''

'''
##########################################
#string 的slice
test = 'opqrstuvwsyzabcdefghijk'
        #a  a  a  a  a  a  a  a
print(test[1:23:3])# 結尾位置不算
##########################################
'''
'''
##########################################
text = u'測試'
print(type(text)) # 顯示 "<class 'str'>"
print(len(text)) # 顯示 2

print('元'.encode('UTF-8').decode('UTF-8'))
##########################################
'''

"""
##########################################
#兩個雙引號連接會變成一行
strTest = " abc\
def\
ghi\
jkl\
mn\
opq\
rst\
uvw\
xyz\
"
#三個雙引號可自動換行 = 三個單引號
strTest1 = '''abc
def
ghi
jkl 
mno
pqr
stu
vwx
yz
'''

strTest2 = '''
abc
def
ghi
'''
print(strTest)
print(strTest1)
print(strTest2)
##########################################
"""

'''
##########################################
#print(list.__doc__)

namesList = ['Justin', 'caterpillar', 'openhome']
index = [0,1,2]
for name in range(len(namesList)):
    print('{0},{1}'.format(name,namesList[name]))

#print(zip(namesList))


##########################################
str = 'abcdefg'
str[-1]
print('it was so' + 'c' + 'oc'*7 + 'l')


#name = raw_input('What is your name?')



a = 'hello world'
print(a.format())


test_list1 = ('a','b','c')
test_list2 = ['x','y','z']
test_tuple = tuple(test_list2)
# test_list2 可以修改，tuple() 函数不是改变值的类型，而是返回改变类型后的值，原值不会被改变
test_list2[2] = '这是修改的'
# 下面这行报错，元组不可修改
# test_list1[2]='这是修改的'
print(test_list1)
print(test_list2)
print(test_tuple)
#########################################

def changeme(mylist):
    print("values in the function before change:", mylist)
    mylist = [50,40,30,20,10]
    print("values in the function after change:", mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print("values out side the function", mylist)
##################################################

# total = 0
# def sum_data(arg1, arg2):
#     print("inside before chanxge", total)
#     total = arg1 + arg2
#     #print("inside after change", total)
# sum_data(10,20)
# print("outside after function", total)
#####################################################

def myrange(n):
    x = 0
    while True:
         yield x
         x += 1
         if x == n:
             break

# for i in myrange(10):
#     print(i, end='')
# print()


g = myrange(2)
print(next(g))
print(next(g))



def func(n):
    yield n*2


gen = func(5)
print(next(gen))
print(next(gen))
'''
