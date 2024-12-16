def append(x,item): return f'{x}*{item}' #add item to list;split using "*"
def find(x,position):
    pos,curvar,atval = 0,"",False #vars
    for val, i in enumerate(x): #cycle through lists at "*" (sub for .split)
        if i == "*":
            pos += 1
            if pos == int(position):atval = True
        if atval == True:curvar = f"{curvar}{i}"
        if i == "*" and curvar != "*":atval = False
    if curvar=="":curvar="None" #if not found
    return curvar.replace("*","") #get rid of exess "*"




x = append(x="",item="item1") #Example: 'append' usage/create list
x = append(x,item="item2")
x = append(x,item="item3")

print(find(x,position=3)) #Example of 'find' usage


