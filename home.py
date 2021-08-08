
def home1():
    print("------LIBRARY MANAGEMENT SYSTEM-------")
    print("\n")
    k=True
    while(k==True):
        print("1.Press 1 for New User registration")
        print("2.Press 2 for Admin login ")
        print("3.Press 3 for User login")
        print("4.Press 4 to exit from application")
        s=input()
        if s not in ['1','2','3','4']:
            print("Wrong input. Enter correctly")
            print("----------------------------")
        else:            
            n=int(s)
            if n==1:
                from background import lms
                lms.register()                
                #print("Do you want to return to HOME page. If yes then press 1")                
                #h=input()
                #if h!='1':
                  #  break
                                    
            elif n==2:
                from background import lms
                lms.admin()                
                #print("Do you want to return to HOME page. If yes then press 1")
                #h=input()
                #if h!='1':
                   # break
            elif n==3:
                from background import lms
                lms.login()                
                #print("Do you want to return to HOME page. If yes then press 1")
                #h=input()
                #if h!='1':
                   # break
            elif n==4:
                print("Application is closed")
                break
def main():
    foo = home1()
    

if __name__ == "__main__":
    main()