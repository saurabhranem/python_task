# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ]
#
#
# #  re sort the elements in the matrix
# ls =[]
# for row in matrix :
#     for item in row:
#         # iterate over each individual element
#         ls.append(item)
#
#
#
# input= 8 # ie the end user gives input
#
# resorted = ls.sort()
#
# # resorted elements are
# print(resorted)
# print(resorted.pop(input))
#
#
#
# # ls =[1,2,3,4,5]


shares_of_week = [7,1,5,3,6,4] # theses are shares recorded in a week
lowest_share = min(shares_of_week)

# get index of the lowest share
ix = shares_of_week.index(lowest_share)

shares_of_rest_of_the_week = shares_of_week[ix:]

max_share_val =max(shares_of_rest_of_the_week)

highest_share = shares_of_rest_of_the_week.index(max_share_val)
print("shares can be sold on day {}, at price {}".format(highest_share,max_share_val))
print("You gain a profit of {}".format(max_share_val-lowest_share) )