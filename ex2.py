'''
 Given a list of strings, return the count of:
 1) number of strings where the string length is 2 or more 
 2) first and last chars of the string are the same

 Example:
 Input: ["test", "test1", "t", "synerzip", "Python", "is", "an", "object", "oriented", "language"]
 Output: (9, 2)
'''

myList =  ["test", "test1", "t", "synerzip", "Python", "is", "an", "object", "oriented", "language"]
i = j = 0
for item in myList:
    if len(item) >= 2 :
        i = i + 1
    if item[0] is item[-1] :
        j = j + 1

print "Count of strings which has more than two chars %d and where the first and last char is same %d" % (i,j)