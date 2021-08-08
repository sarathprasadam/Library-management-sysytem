import datetime
import json
class lms:  
  
    fp=open('booklist.json','r')
    book_str=fp.read()
    book_dict=json.loads(book_str)
    fp.close()
    book_id=len(book_dict)

    fp=open('memberlist.json','r')
    member_str=fp.read()
    members_dict=json.loads(member_str)
    fp.close()


    fp=open('adminlist.json','r')
    admin_str=fp.read()
    adminstr=json.loads(admin_str)
    fp.close()
    


    @classmethod
    def register(cls):
        print("----NEW USER REGISTRATION----")
        a=True
        while(a==True):
            name=input("Name= ")
            if len(name)!=0:
                a=False
        b=True
        while(b==True):
            email=input("Email Id= ")
            if len(email)!=0:
                b=False
        if email in cls.members_dict.keys():
            print("Email is already registered. Login and enjoy book reading. ")
            
        else:
            c=True
            while(c==True):
                password=input("Enter password ")
                if len(password)!=0:
                    c=False
            dobtest=True
            while(dobtest==True):
                dobis=input("Enter Date of birth in format DATE/MONTH/YEAR  ")
                if '/' in dobis:
                    doblistis=dobis.split('/')
                else:
                    doblistis=dobis.split('-')
                
                try:
                    dobbis= datetime.date(int(doblistis[2]),int(doblistis[1]),int(doblistis[0]))                                              
                    dobtest=False
                except:
                    print("Invalied Date")           
            
            dob=str(dobbis)               
            s=0
            while(s!=10):
                s=0
                k=input("Mobile number= ")
                if len(k)==0:
                    print("Enter any value")
                else:                    
                    for i in k:
                        if ord(i) not in range(48,58):
                            print("Character not allowed in no")
                            break
                    else:
                        k=int(k)
                        m=k
                        while(m!=0):
                            m=m//10            
                            s+=1
                        if s!=10:
                            print("Enter number correctly")
            mobile_no=k
            book_borrowed={}
            borrowed_history={}
            print("Details provided")
            print("Name= ",name)
            print("Email= ",email)
            print("mobile_no= ",mobile_no) 
            print("DOB= ",dob)       
            print("Do you want to add this user. if yes then prss 1")
            reg=input()
            if reg=='1':         
                cls.members_dict[email]={'name':name,'mobile_no':mobile_no,'pasd':password,'dob':dob,
                                                  'book_borrowed':book_borrowed,'history':borrowed_history}
                print("Registered successfully")
                dump_data1=json.dumps(cls.members_dict)
                fp=open('memberlist.json','w+')
                fp.write(dump_data1)
                fp.close()

            else:
                print("Registration cancelled")

    @classmethod
    def admin(cls):
        print("-------ADMIN PAGE-------")
        adm1=input("ENTER username ")
        adm2=input("Enter password ")
        if adm1 not in cls.adminstr.keys():
            print("INVALIED username")
        else:
            if cls.adminstr[adm1]==adm2:
                print("admin logged in successfully")
                m=True
                while(m==True):                    
                    print("-----ADMIN FUNCTIONS-----")
                    mkmkmk=input("press ENTER to continue")
                    print("Press 1 to create new admin")
                    print("Press 2 to add more book to library")
                    print("Press 3 to edit book detail")
                    print("Press 4 to delete book")
                    print("Press 5 to list all borrowers")
                    print("Press 6 to issue a book")
                    print("Press 7 to return a book")
                    print("Press 8 to view book details and borrowing history")
                    print("Press 9 to log out ")

                    adminp=input()
                    if adminp not in ['1','2','3','4','5','6','7','8','9']:
                        print("Invalied input")                        
                    elif adminp=='1':
                        print("--------NEW ADMIN CREATION PAGE---------")
                        z=True
                        while(z==True):
                            ad1=input("Enter user name ")
                            if ad1 in cls.adminstr.keys():
                                print("User name already exist")
                            elif ad1=='':
                                print("Username cant be empty")
                            else:
                                z=False
                        pwdchk=True
                        while(pwdchk==True):
                            ad2=input("Enter password ")
                            if ad2!='':
                                pwdchk=False
                            else:
                                print("Password cant be empty")
                        cls.adminstr[ad1]=ad2
                        print("admin added successfully")
                        dump_data2=json.dumps(cls.adminstr)
                        fp=open('adminlist.json','w+')
                        fp.write(dump_data2)
                        fp.close()                       
                        

                    elif adminp=='2':
                        print("------ADDING NEW BOOK----------")                        
                        print("ENTER THE BOOK DETAILS")
                        bt=input("Book name ")
                        for i in cls.book_dict.keys():
                            test=cls.book_dict[i]['name']
                            if test.lower()==bt.lower():
                                ctt=True
                                while(ctt==True):
                                    ct=input("Enter no of copies ")
                                    if len(ct)==0:
                                        print("Enter any value")
                                    else:

                                        for lll in ct:
                                            if ord(lll) not in range(48,58):
                                                print("Character not allowed in no of copies")
                                                break
                                        else:
                                            ct=int(ct)
                                            ctt=False

                                x=cls.book_dict[i]['copies']
                                cls.book_dict[i]['copies']+=ct
                                print("Book already exist. No of copies updated to",cls.book_dict[i]['copies'])                               
                                break
                        else:
                            ctt=True
                            while(ctt==True):
                                ct=input("Enter no of copies: ")
                                if len(ct)==0:
                                    print("enter any value")
                                else:                                    
                                    for i in ct:
                                        if ord(i) not in range(48,58):
                                            print("Character not allowed in no of copies")
                                            break
                                    else:
                                        ct=int(ct)
                                        ctt=False                            
                            at=input("Author name ")
                            ktt=True
                            while(ktt==True):
                                pt=input("total pages ")
                                if len(pt)==0:
                                    print("Enter any value")
                                else:
                                    for i in pt:
                                        if ord(i) not in range(48,58):
                                            print("Character not allowed in total pages")
                                            break
                                    else:
                                        pt=int(pt)
                                        ktt=False                             
                            isb=True
                            while(isb==True):
                                istt=True
                                while(istt==True):
                                    it=input("ISBN no ")
                                    if len(it)==0:
                                        print("Enter any value")
                                    else:
                                        for i in it:
                                            if ord(i) not in range(48,58):
                                                print("Character not allowed in ISBN")
                                                break
                                        else:
                                            istt=False
                                            if len(it)==13:
                                                isb=False
                                                it=int(it)
                                            else:
                                                print("ISBN consist of 13 digits")
                            ytc=True
                            while(ytc==True):
                                ytcb=True
                                while(ytcb==True):                            
                                    yt=input("Published year ")
                                    if len(yt)==0:
                                        print("Enter any value")
                                    else:
                                        for i in yt:
                                            if ord(i) not in range(48,58):
                                                print("Character not allowed in year")
                                                break
                                        else:
                                            ytcb=False
                                            if len(yt)==4:
                                                ytc=False
                                                yt=int(yt)
                                            else:
                                                print("Enter year in 4 digit format")
                            print("Detail of new book as provided")
                            print("Name: ",bt)
                            print("Author: ",at)
                            print("Copies: ",ct)
                            print("Total pages: ",pt)
                            print("ISBN: ",it)
                            print("Published year: ",yt)
                            bkadd=input("Do you want to add this book. If yes press 1 ")
                            if bkadd=='1':
                                cls.book_id+=1
                                bokidd=str(cls.book_id)                                                    
                                cls.book_dict[bokidd]={'name':bt,'copies':ct,'author':at,
                                                        'pages':pt,'ISBN':it,'PUBLISHED_YEAR':yt,
                                                        'borowwer':[]}
                                print("book added successfully")
                                
                            else:
                                print("Book adding process cancelled")
                            
                    elif adminp=='3':
                        print("--------EDITING BOOKS DETAIL----")                        
                        eb=True
                        while(eb==True):
                            ktt=True
                            while(ktt==True):
                                id1=input("enter book id ")
                                if len(id1)==0:
                                    print("Enter any value")
                                else:
                                    for i in id1:
                                        if ord(i) not in range(48,58):
                                            print("Character not allowed in bookid")
                                            break
                                    else:
                                        #id1=int(id1)
                                        ktt=False                               
                            if id1 not in cls.book_dict.keys():
                                print("Enter correct book id")
                            else:
                                eb=False
                                edt=True                                
                                while(edt==True): 
                                    print("Press 1 to edit book name")   
                                    print("Press 2 to edit Author name")
                                    print("Press 3  to edit Total pages")
                                    print("Press 4 to edit No of copies")
                                    print("Press 5 to edit ISBN")
                                    print("Press 6 to edit Published year")
                                    print("------------------------------")
                                    inph=input()
                                    if inph not in ['1','2','3','4','5','6']:
                                        print("Invalied input")
                                    elif inph=='1':
                                        bni=input("Enter book name ")
                                        cls.book_dict[id1]['name']=bni
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False 
                                        else:
                                            print("Book edited successfully")
  
                                    elif inph=='2':
                                        ani=input("Enter Author name ")
                                        cls.book_dict[id1]['author']=ani
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False  
                                        else:
                                            print("Book edited successfully")                                     

                                    elif inph=='3':
                                        ktt=True
                                        while(ktt==True):
                                            pni=input("Enter Total pages ")
                                            if len(pni)==0:
                                                print("Enter any value")
                                            else:
                                                for i in pni:
                                                    if ord(i) not in range(48,58):
                                                        print("Character not allowed in total pages")
                                                        break
                                                else:
                                                    pni=int(pni)
                                                    ktt=False                                         
                                        cls.book_dict[id1]['pages']=pni
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False 
                                        else:
                                            print("Book edited successfully")  

                                    elif inph=='4':
                                        ctt=True
                                        while(ctt==True):
                                            cni=input("Enter no of copies ")
                                            if len(cni)==0:
                                                print("Enter value")
                                            else:                                                
                                                for i in cni:
                                                    if ord(i) not in range(48,58):
                                                        print("Character not allowed in no of copies")
                                                        break
                                                else:
                                                    cni=int(cni)
                                                    ctt=False                                                                             
                                        cls.book_dict[id1]['copies']=cni
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False 
                                        else:
                                            print("Book edited successfully")

                                    elif inph=='5':
                                        isb=True
                                        while(isb==True):
                                            istt=True
                                            while(istt==True):
                                                it=input("ISBN no ")
                                                if len(it)==0:
                                                    print("Enter value")
                                                else:
                                                    for i in it:
                                                        if ord(i) not in range(48,58):
                                                            print("Character not allowed in ISBN")
                                                            break
                                                    else:
                                                        istt=False
                                                        if len(it)==13:
                                                            isb=False
                                                            it=int(it)
                                                        else:
                                                            print("ISBN consist of 13 digits")                                                                        
                                        cls.book_dict[id1]['ISBN']=it
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False
                                        else:
                                            print("Book edited successfully")

                                    elif inph=='6':
                                        ytc=True
                                        while(ytc==True):
                                            ytcb=True
                                            while(ytcb==True):                            
                                                yt=input("Published year ")
                                                if len(yt)==0:
                                                    print("Enter value")
                                                else:
                                                    for i in yt:
                                                        if ord(i) not in range(48,58):
                                                            print("Character not allowed in year")
                                                            break
                                                    else:
                                                        ytcb=False
                                                        if len(yt)==4:
                                                            yt=int(yt)                                                               
                                                            ytc=False                                                                   
                                                                                                                        
                                                        else:
                                                            print("Enter year in 4 digit format and year must be less than 2022")                                                                           
                                        cls.book_dict[id1]['PUBLISHED_YEAR']=yt
                                        print("do you want to edit anything else? if yes press 1")
                                        hhh=input()
                                        if hhh!='1':
                                            edt=False 
                                        else:
                                            print("Book edited successfully")
                    elif adminp=='4':                      
                        
                        print("---DELETE BOOK---")
                        eb=True
                        while(eb==True):
                            ktt=True
                            while(ktt==True):
                                id1=input("enter book id ")
                                if len(id1)==0:
                                    print("Enter value")
                                else:
                                    for i in id1:
                                        if ord(i) not in range(48,58):
                                            print("Character not allowed in bookid")
                                            break
                                    else:
                                        #id1=int(id1)
                                        ktt=False                                 
                            if id1 not in cls.book_dict.keys():
                                print("Enter correct book id")
                            else:
                                eb=False
                                print("Do you want to delete the book '",cls.book_dict[id1]['name'],"' ?")                                
                                w=input("If yes then type 1: ")
                                if w=='1':                                    
                                    lt=len(cls.book_dict[id1]['borowwer'])
                                    if lt==0:
                                        print('ID: ',id1,'Book name: ',cls.book_dict[id1]['name'],'is deleted successfully')
                                        cls.book_dict.pop(id1)  
                                        
                                  
                                    else:
                                        print("Can't delete book.Book is borrowed by",lt,'no of peoples')
                                        
                                else:
                                    print("The book is not deleted")
                                    
                    elif adminp=='5':                        
                        print("LIST OF ALL BORROWERS")
                        for i in cls.members_dict.keys():
                            print("NAME: ",cls.members_dict[i]['name'])
                            print("DOB: ",cls.members_dict[i]['dob'])
                            print("CONTACT NUMBER: ",cls.members_dict[i]['mobile_no'])
                            print("EMAIL ID: ",i)
                            
                            print("----LIST OF CURRENTLY LENTED BOOK---- ")
                            for h in cls.members_dict[i]['book_borrowed'].keys():
                                print('bookid: ',h,'book name: ', cls.book_dict[h]['name'])
                            print("-------HISTORY OF BOOK LENTED-------")

                            for t in cls.members_dict[i]['history'].keys():
                                for p in cls.members_dict[i]['history'][t]:
                                    if p[1]!='':
                                        print('bookid: ',t,'book_name: ',cls.book_dict[t]['name'],'Issued on: ',
                                            p[0],'Returned on: ', p[1])
                                   
                            
                            print("--------------------------------------------")
                            
                    elif adminp=='6':                      
                        
                        print("-----BOOK ISSUE---")
                        dtt=datetime.date.today()
                        ad6=True
                        while(ad6==True):
                            bid=input("Enter email id ")
                            if bid not in cls.members_dict.keys():
                                print("No such email id exist")
                            else:
                                if len(cls.members_dict[bid]['book_borrowed'].keys())<3:                           
                            
                                    ad6=False
                                    ad7=True
                                    while(ad7==True):
                                        ktt=True
                                        while(ktt==True):
                                            bkid=input("enter book id ")
                                            if len(bkid)==0:
                                                print("Enter value")
                                            else:
                                                for i in bkid:
                                                    if ord(i) not in range(48,58):
                                                        print("Character not allowed in bookid")
                                                        break
                                                else:
                                                    #bkid=int(bkid)
                                                    ktt=False                                             
                                        if bkid not in cls.book_dict.keys():
                                            print("Enter correct book id")
                                        else:
                                            ad7=False
                                            no=cls.book_dict[bkid]['copies']
                                            if no==0:
                                                print("No copies remaining")
                                                

                                            else:
                                                if bkid in cls.members_dict[bid]['book_borrowed'].keys():
                                                    print("The book is already borrowed. Can't borrow 2 copies")
                                                    

                                                else:
                                                    datetest=True
                                                    dtisbck=dtt-datetime.timedelta(days=7)                                                    
                                                    while(datetest==True):
                                                        print("Enter ISSUE date in format DATE/MONTH/YEAR  Issue date cannot be less than ",dtisbck)
                                                        dtis=input()
                                                        if '/' in dtis:
                                                            dtlistis=dtis.split('/')
                                                        else:
                                                            dtlistis=dtis.split('-')
                                                        
                                                        try:
                                                            datis= datetime.date(int(dtlistis[2]),int(dtlistis[1]),int(dtlistis[0]))                                                
                                                            if datis>dtt:
                                                                print("Issue date cannot be greater than todays date") 
                                                            elif datis<dtisbck:
                                                                print("Issue date cannot be less than ",dtisbckchk)
                                                            else:
                                                                datetest=False
                                                        except:
                                                            print("Invalied Date")
                                                    cls.book_dict[bkid]['copies']=no-1
                                                    cls.book_dict[bkid]['borowwer'].append(bid)
                                                    cls.members_dict[bid]['book_borrowed'][bkid]=str(datis)
                                                    if bkid not in cls.members_dict[bid]['history'].keys():
                                                        cls.members_dict[bid]['history'][bkid]=[[str(datis),'']]
                                                    else:
                                                        cls.members_dict[bid]['history'][bkid].append([str(dtt),''])
                                                    print("Book successfully issued")                                                  
                                                    
                                                    

                                else:
                                    print("You have exceeded the borrowing limit")
                                    ad6=False
                                    

                    elif adminp=='7':
                        
                        print("------BOOK RETURN----")
                        tpr1=datetime.date.today()                         
                        kkk=True
                        while(kkk==True):
                            emo=input("Enter email id ")
                            if emo not in cls.members_dict.keys():
                                print("No such email id exist")

                            else:
                                kkk=False
                                print("List of book borrowed")
                                for i in cls.members_dict[emo]['book_borrowed'].keys():
                                    print('book id: ',i,'book_name: ',cls.book_dict[i]['name'])
                                if cls.members_dict[emo]['book_borrowed']: 
                                    hmh=True
                                    while(hmh==True):
                                        bkkkk=True
                                        while(bkkkk==True):
                                            bkkid=input("Enter book id of book you wish to return ")
                                            if len(bkkid)==0:
                                                print("Enter value")
                                            else:
                                                for i in bkkid:
                                                        if ord(i) not in range(48,58):
                                                            print("Character not allowed in book ID")
                                                            break
                                                else:
                                                    #bkkid=int(bkkid)
                                                    bkkkk=False 

                                        if bkkid not in cls.members_dict[emo]['book_borrowed'].keys():
                                            print("Wrong book id")
                                        else:
                                            hmh=False
                                            fppp=cls.members_dict[emo]['book_borrowed'][bkkid]
                                            if '-' in fppp:
                                                fppk=fppp.split('-')
                                            elif '/' in fppp:
                                                fppk=fppp.split('/')
                                            fntd=datetime.date(int(fppk[0]),int(fppk[1]),int(fppk[2]))                                           
                                            
                                            datetest=True
                                            while(datetest==True):
                                                dt=input("Enter Return date in format DATE/MONTH/YEAR  ")
                                                if '/' in dt:
                                                    dtlist=dt.split('/')
                                                else:
                                                    dtlist=dt.split('-')
                                                
                                                try:
                                                    dat= datetime.date(int(dtlist[2]),int(dtlist[1]),int(dtlist[0]))                                                
                                                    if dat<fntd:
                                                        print("Return date cannot be less than issued date") 
                                                    elif dat>tpr1:
                                                        print("Return date cannot be greater than todays date")
                                                    else:                                                        
                                                        datetest=False
                                                except:
                                                    print("Invalied Date")
                                                
                                            finetst=dat-fntd
                                            datestr=str(finetst)
                                            if 'day' in datestr:
                                                pp=int(datestr.split(" ")[0])
                                                testdate=pp    
                                            else:
                                                pp=int(datestr.split(":")[0])
                                                testdate=pp
                                            if testdate>15:
                                                print("Fine of 100 charged")
                                            oo=cls.book_dict[bkkid]['copies']
                                            cls.book_dict[bkkid]['copies']=oo+1
                                            cls.book_dict[bkkid]['borowwer'].remove(emo)
                                            cls.members_dict[emo]['book_borrowed'].pop(bkkid)
                                            #cls.members_dict[emo]['history'][bkkid][1]=dat
                                            cls.members_dict[emo]['history'][bkkid][-1][1]=str(dat) 
                                            print("BOOK returned successfully")
                                else:
                                    print("User has not borrowed any book")



                    elif adminp=='8':
                        print('----------BOOK DETAIL-------------')
                        print("enter the book id")
                        ktt=True
                        while(ktt==True):
                            idbt=input("enter book id ")
                            if len(idbt)==0:
                                print("Enter value")
                            else:
                                for i in idbt:
                                    if ord(i) not in range(48,58):
                                        print("Character not allowed in bookid")
                                        break
                                else:
                                    #idbt=int(idbt)
                                    ktt=False   
                        
                        if idbt not in cls.book_dict.keys():
                            print("Invalied book ID")
                        else:
                            print("Book name: ",cls.book_dict[idbt]['name'])
                            print("Author: ",cls.book_dict[idbt]['author'])
                            print("Copies",cls.book_dict[idbt]['copies'])
                            print("Pages: ",cls.book_dict[idbt]['pages'])
                            print("Published Year: ",cls.book_dict[idbt]['PUBLISHED_YEAR'])
                            print("ISBN: ",cls.book_dict[idbt]['ISBN'])
                            print("List of current borrowers")
                            for i in cls.book_dict[idbt]['borowwer']:
                                print("Name: ",cls.members_dict[i]['name'],"Email Id: ",i,
                                    "Issued on: ",cls.members_dict[i]['book_borrowed'][idbt])
                            print("----------------------------------------------------------")
                            print("List of Previous Borrowers")
                            for i in cls.members_dict:
                                if idbt in cls.members_dict[i]['history'].keys():
                                    for s in cls.members_dict[i]['history'][idbt]:
                                        if s[1]!='':
                                            print("Name: ",cls.members_dict[i]['name'],"Email Id: ",i,
                                                "Issued on: ",s[0],"Returned On: ",s[1])

                            
                    elif adminp=='9':
                        m=False
                        dump_data3=json.dumps(cls.book_dict)
                        fp=open('booklist.json','w+')
                        fp.write(dump_data3)
                        fp.close()

                        dump_data4=json.dumps(cls.members_dict)
                        dp=open('memberlist.json','w+')
                        dp.write(dump_data4)
                        dp.close()

                        
                            


                
            else:
                print("Incorrect password")

    @classmethod
    def login(cls):
        print(".............LOGIN PAGE.........")
        lgn1=input("Enter your email ID ")
        lgn2=input("Enter your password ")
        if lgn1 not in cls.members_dict.keys():
            print("Email id doesnot exist")
        else:
            if cls.members_dict[lgn1]['pasd']==lgn2:
                print("LOGINED SUCCESSFULLY")
                d=True
                while(d==True):
                    mkmkmk=input("press ENTER to continue")
                    print("Press 1 to view currently borrowed books")
                    print("Press 2 to view detail of borrowed books")
                    print("Press 3 to view borrowing history")
                    print("Press any other number to logout")                    
                    inp1=input()
                    if inp1 not in ['1','2','3']:
                        print("Logged out successfully")
                        d=False
                    elif inp1=='1':                        
                        print("---LIST OF BOOK BORROWED---")
                        mpk=datetime.date.today()                        
                        for i in cls.members_dict[lgn1]['book_borrowed'].keys():
                            hpkm=cls.members_dict[lgn1]['book_borrowed'][i]
                            if '-' in hpkm:
                                hpkk=hpkm.split('-')
                            elif '/' in fppp:
                                hpkk=hpkm.split('/')                            
                            hpk=datetime.date(int(hpkk[0]),int(hpkk[1]),int(hpkk[2]))
                            fstm=mpk-hpk
                            datest=str(fstm)
                            if 'day' in datest:
                                ppp=int(datest.split(" ")[0])
                                testdat=ppp    
                            else:
                                ppp=int(datest.split(":")[0])
                                testdat=ppp
                            dtrem=15-testdat
                            print('bookid: ',i,'book name: ', cls.book_dict[i]['name'],'Days remaining: ',dtrem)
                        print("----------------------------")
                        

                    elif inp1=='2':                        
                        print('----DETAILS OF BORROWED BOOKS----')
                        for i in cls.members_dict[lgn1]['book_borrowed'].keys():
                            print("Book id: ",i)
                            print("Book name: ",cls.book_dict[i]['name'])
                            print("Author: ",cls.book_dict[i]['author'])
                            print("ISBN: ",cls.book_dict[i]['ISBN'])
                            print("Pages: ",cls.book_dict[i]['pages'])
                            print("Published Year: ",cls.book_dict[i]['PUBLISHED_YEAR'])
                            print("-----------------------------------------")
                        
                    elif inp1=='3':                        
                        print("-----BORROWING HISTORY-----")
                        for i in cls.members_dict[lgn1]['history'].keys():
                            for p in cls.members_dict[lgn1]['history'][i]:
                                if p[1]!='':
                                        print('bookid: ',i,'book_name: ',cls.book_dict[i]['name'],'Issued on: ',
                                            p[0],'Returned on: ', p[1])


                              
                        print("-------------------------------------------")
                        


                
            else:
                print("Incorrect password")
def main():
    foo = lms()
    foo.lms()

if __name__ == "__main__":
    main()