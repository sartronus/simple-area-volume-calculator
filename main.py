#formula for simple calculations_____________________________________
def add (a,b):
    c=a+b
    print(c)
def sub (a,b):
    c=a-b
    print(c)
def multi (a,b):
    c=a*b
    print(c)
def div (a,b):
    c=a/b
    print(c)
#formula for areas_________________________________________________________
def ar_rect (a,b):
    c=a*b
    print(c)
def ar_sq (a):
    c=a*a
    print(c)
def ar_tri (a,b):
    c=0.5*a*b
    print(c)
def ar_cir (a):
    c=3.14*a*a
    print(c)
def ar_trap (a,b,c):
    c=0.5*(a-b)*c
    print(c)
def ar_eli (a,b):
    c=3.14*a*b
    print(c)

#formula for volume___________________________________________________


def vol_cuboid (a,b,c):
    c=a*b*c
    print(c)
def vol_cube (a):
    c=a*a*a
    print(c)
def vol_cyllender (a,b):
    c=3.14*a*a*b
    print(c)
def vol_prism (a,b):
    c=a*b
    print(c)
def vol_sphere (a):
    c=1.33*3.14*a*a*a
    print(c)
def vol_pyramid (a,b):
    c=0.33*a*b
    print(c)
def vol_rec_pyramid (a,b,c):
    c=0.33*a*b*c
    print(c)
def vol_ellipsoid (a,b,c):
    c=1.33*3.14*a*b*c
    print(c)
def vol_tetrahedron (a):
    c=a*a*a/8.48
    print(c)
#simple______________________________________________________________________

options=""
while options == 1 or 2 or 3:
    options = int(input("Select one of the following options:- \n Press 1 for simple calculations \n Press 2 for finding area \n Press 3 for finding the volume \n >"))
    if options == 1:
        print("you have selected simple calculations")
        options_s=int(input("please select the following options:- \n Press 1 for addition \n Press 2 for subtractions \n Press 3 for multiplications \n Press 4 for division \n >"))
        if options_s ==1:
            print("you have selected addition")
            num1= int(input("enter first number-> "))
            num2= int(input("enter second number-> "))
            print("your answer is")
            (add(num1,num2))
        elif options_s ==2:
            print("you have selected subtraction")
            num1= int(input("enter first number-> "))
            num2= int(input("enter second number-> "))
            print("your answer is")
            (sub(num1, num2))
        elif options_s ==3:
            print("you have selected multiplication")
            num1= int(input("enter first number-> "))
            num2= int(input("enter second number-> "))
            print("your answer is")
            (multi(num1, num2))
        elif options_s ==4:
            print("you have selected division")
            num1= int(input("enter first number-> "))
            num2= int(input("enter second number-> "))
            print("your answer is")
            (div(num1, num2))
        else:
            print("you have chosen wrong option")
#area_______________________________________________________________________________________________________________________
    if options == 2:
        print("you have selected area calculations")
        options_a=int(input("please select the following options:- \n Press 1 for rectangle \n Press 2 for square \n Press 3 for triangle \n Press 4 for circle \n press 5 for trapezoid\n press 6 for Ellipse \n >"))
        if options_a ==1:
            print("you have selected rectangle")
            num1= int(input("enter length-> "))
            num2= int(input("enter width-> "))
            print("your answer is")
            (ar_rect(num1,num2))
        elif options_a ==2:
            print("you have selected square")
            num1= int(input("enter length of one side of square-> "))
            print("your answer is")
            (ar_sq(num1))
        elif options_a ==3:
            print("you have selected triangle")
            num1= int(input("enter base of triangle-> "))
            num2= int(input("enter heightof triangle-> "))
            print("your answer is")
            (ar_tri(num1, num2))
        elif options_a ==4:
            print("you have selected circle")
            num1= int(input("enter radius of circle-> "))
            print("your answer is")
            (ar_cir(num1))
        elif options_a ==5:
            print("you have selected trapezoid")
            num1= int(input("enter base 1 of trapezoid-> "))
            num2= int(input("enter base 2 of trapezoid-> "))
            num3= int(input("enter vertical height of trapezoid-> "))
            print("your answer is")
            (ar_trap(num1,num2,num3))
        elif options_a ==6:
            print("you have selected ellipse")
            num1= int(input("enter radius of major axis-> "))
            num2= int(input("enter radius of minor axis-> "))
            print("your answer is")
            (ar_eli(num1,num2))
        else:
            print("you have selected wrong option")


#volume_________________________________________________________________________________________________________
    if options == 3:
        print("you have selected volume calculations")
        options_v=int(input("please select the following options:- \n Press 1 for cuboid \n Press 2 for cube \n Press 3 for cylinder \n Press 4 for prism \n press 5 for sphere\n press 6 for pyramid \n press 7 for square or rectangular pyramid \n press 8 for ellipsoid\n press 9 for tetrahedron\n >"))
        if options_v ==1:
            print("you have selected cuboid")
            num1= int(input("enter length-> "))
            num2= int(input("enter width-> "))
            num3= int(input("enter height-> "))
            print("your answer is")
            (vol_cuboid(num1,num2,num3))
        elif options_v ==2:
            print("you have selected cube")
            num1= int(input("enter length of edge of one side of cube-> "))
            print("your answer is")
            (vol_cube(num1))
        elif options_v ==3:
            print("you have selected cylinder")
            num1= int(input("enter radius of circular base-> "))
            num2= int(input("enter height of cylinder-> "))
            print("your answer is")
            (vol_cyllender(num1, num2))
        elif options_v ==4:
            print("you have selected prism")
            num1= int(input("enter area of base-> "))
            num2= int(input("enter height of prism-> "))
            print("your answer is")
            (vol_prism(num1,num2))
        elif options_v ==5:
            print("you have selected sphere")
            num1= int(input("enter radius of sphere-> "))
            print("your answer is")
            (vol_sphere(num1))
        elif options_v ==6:
            print("you have selected pyramid")
            num1= int(input("enter area of base-> "))
            num2= int(input("enter height of pyramid-> "))
            print("your answer is")
            (vol_pyramid(num1,num2))
        elif options_v ==7:
            print("you have selected square or rectangular pyramid")
            num1= int(input("enter length of base-> "))
            num2= int(input("enter width of base-> "))
            num3 = int(input("enter height of pyramid-> "))
            print("your answer is")
            (vol_rec_pyramid(num1,num2,num3))
        elif options_v ==8:
            print("you have selected square or rectangular pyramid")
            num1= int(input("enter a-semi axis of an ellipsoid-> "))
            num2= int(input("enter b-semi axis of an ellipsoid-> "))
            num3 = int(input("enter c-semi axis of an ellipsoid-> "))
            print("your answer is")
            (vol_ellipsoid(num1,num2,num3))
        elif options_v == 9:
            print("you have selected sphere")
            num1 = int(input("enter length of edge-> "))
            print("your answer is")
            (vol_tetrahedron(num1))
        else:
            print("you have selected wrong option")