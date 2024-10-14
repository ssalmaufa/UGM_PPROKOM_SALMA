mylist = [1,2,3,4,5]
mylistnew = [77,99,66,88]
mylist.extend(mylistnew)
print('1.', mylist)
mylist.sort()
print('2.', mylist)
mylist.reverse()
print('3.', mylist)
print('4.', mylist.index(5))
mylist.remove(99)
print('5.', mylist)

salinan = mylist.copy()
mylist.clear()
print('6.',mylist)
print('7', salinan)