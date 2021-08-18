import os
def main():
    os.system("clear")
    ang = float(input("Dame el valor del ángulo:"))
    if ang <0 or ang >= 360:
        print("Error, ningun ángulo es superior a 360°")
    elif ang < 90:
        print (f"{ang}° es un ángulo agudo")
    elif ang == 90:
        print (f"{ang}° es un ángulo recto")
    elif ang > 90 and ang < 180:
        print (f"{ang}° es un ángulo obtuso")
    elif ang == 180:
        print (f"{ang}° es un ángulo llano")
    else:         
        print (f"{ang}° es un ángulo cóncavo")

if __name__=='__main__':
    main()
