my_list = ['a',  'b' , 'c', 'd']
# my_list.reverse()
# print(my_list)
#
# reversed = my_list[::-1]
# print(reversed)




# len_of_my_list = len(my_list)
#
# for i in range(len_of_my_list-1,0,-1):
#     # which would generate indexs in reverse orfer ie 3 2 1 0
#     # print(i)
#
#     print("index",i)
#     # print("last item",my_list[i])
#     item = my_list.pop(i)
#     print(item)
#     # take the last element and insert it in first index
#     my_list.insert(abs(i-len_of_my_list), item)
#
#
# print(my_list)
#
# he = len_of_my_list - 1
# for i in range(0, len_of_my_list):
#     temp = my_list.pop(i)
#     print(he)
#     last = my_list.pop(he-1 - i)
#     my_list.insert()
#
#     print (temp, last)


# he = len_of_my_list - 1
#
# for i in range(0, len_of_my_list):
#     print(i)
#     if (len(my_list) - 1 -i) - i <= 0:
#         break
#     f = my_list.pop(i)
#     print("im popping" , len(my_list) - 1 -i, my_list)
#     l = my_list.pop(len(my_list) - 1 -i)
#     my_list.insert(i, l)
#     my_list.insert(len(my_list) - i, f)
#     print('---------', my_list)
# print(my_list)
#


# def reverse(seq):
#     """Reverses elements of a list."""
#     for i in range(len(seq)//2):
#         x = seq[i]
#         y = seq[-i-1]
#         seq[i] = y
#         seq[-i-1] = x
#
# l = ['a', 'b', 'c', 'd', 'e']
# reverse(l)
# print(l)


list = [1,2,3,4,5,6,7]
length = len(list)
for index in range(0, int(length/2)):
    r_index = index + 1
    list[index], list[-r_index] = list[-r_index], list[index]
print(list)