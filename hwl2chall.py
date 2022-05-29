def DrewEx(Exsize):
    for location in range(Exsize):
        for mynewrange in range(location+1):
            if mynewrange == location or Exsize - location - 1 == mynewrange:
                print("#", end='')
            else:
                print(" ",end='')
        for fill in reversed(range(Exsize-location-1)):
            if Exsize - mynewrange == Exsize-fill:
                print("#",end='')
            else:
                print(" ",end='')
        print()

DrewEx(7)



def DrewEx(Exsize):
    myArry = []
    for location in range(Exsize):
        for mynewrange in range(location+1):
            if mynewrange == location or Exsize - location - 1 == mynewrange:
                myArry.insert(mynewrange,"#")
            else:
                myArry.insert(mynewrange, " ")
        for fill in reversed(range(Exsize-location-1)):
            if Exsize - mynewrange == Exsize-fill:
                myArry.insert(Exsize - fill, "#")
            else:
                myArry.insert(Exsize-fill," ")
        print("".join(myArry))
        myArry=[]

DrewEx(7)