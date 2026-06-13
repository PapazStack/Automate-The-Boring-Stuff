# Practice Program 1 Chapter 6

def makeList(someList):
    new_list = ''
    if len(someList) == 1:
        new_list = someList[0]
    elif len(someList) == 0:
        print('There is no list available')
    else:
        for item in someList:
            if item == someList[-1]:
                new_list = new_list + 'and ' + item
            else:
                new_list = new_list + item + ', '
    print(new_list.capitalize())
    
    
    

        

items = ['apples', 'bananas', 'tofu', 'cats']
makeList(items)
