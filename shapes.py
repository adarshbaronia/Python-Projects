#which shape would you like to create
#shape app
def right_triangle():
    h=int(input("Enter the HEight of Triangle: "))
    for i in range(1,h+1):
        print(i*' *')
        
#which shape would you like to create
#shape app
def equilateral_triangle():
    h=int(input("Enter the HEight of Triangle: "))
    for i in range(1,h+1):
        print( " "* (h-i+1) + i*" *")
        
#which shape would you like to create
#shape app
def square():
    h=int(input("Enter the side of Square: "))
    for i in range(1,h+1):
        print(h*" *")

#which shape would you like to create
#shape app
def diamond():
    h=int(input("Enter the side of diamond: "))
    for i in range(1,h+1):
        print((h-i+1) * " " + i *' *')
        
    for i in range(h+1,0,-1):
        print((h-i+1) * " " + i *' *')
        
def rhombus():
    h=int(input("Enter side length of Rhombus: "))
    for i in range(2,h+2):
        print((i)*" " + (h) * " *")

def xmas_tree():
    h=int(input("Enter height of tree: "))
    for i in range(1,h+1):
        for j in range(i+1):
            print(" "*(h-i+1)+((i)*" *")+(i*" *")+" "*(h-i-1))
            #print(j*(" "))    
        
    for i in range(h+1):
        print(h*" "+(h-i)*" "+i*" *")
        print(h*" "+(h-i)*" "+i*" *")