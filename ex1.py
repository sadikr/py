
myList = ["Synerzip",1,2,"Python","List",3,12,"Mylist",33,"444"]

# Remove an item from the list if it is an int.
def removeIntFromList(): 
    print "\n", myList	    
    for item in myList[:]: # myList[:] is called slicing. An alternative way to create copy of an array.
	if type(item) is int:
            myList.remove(item)
    	    
    print "\nAfter removing int items", myList	
    print "\n"

# Print  all the items from the list which are String.	
def printIfString():
    print "\nStrings in list are"
    print "\n-------------------"
    for item in myList:
        if type(item) is str:
            print item
    print "\n"

# Print  all the items from the list which are int.	
def printIfInteger():
    print "\nInteger in list are"
    print "\n-------------------"
    for item in myList:
        if type(item) is int:
            print item
    print "\n"

# function calls.
removeIntFromList()

printIfString()

printIfInteger()
