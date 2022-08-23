from datetime import datetime,date
import mysql.connector
import sys
class TollTax:
    def __init__(self):
        pass
    def LoginAccount(self):
        self.username=input("Enter Your UserName: ")
        self.pasw=input("Enter Your Password: ")
        print()
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        myc.execute("select * from logintable where username='"+self.username+"'")
        rs=myc.fetchall()
        for row in rs:
            self.password1=row[1]
                
        if(int(self.pasw)!=int(self.password1)):
            print("Password Entered Is Wrong!!!")
            sys.exit()
        else:
            print("You have Successfully login")
            
        mydb.close()
    def paythetax(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        self.id1=input("Enter the Vehicle ID:")
        self.name=input("Enter the Vehicle Owner Name:")
        self.vehiclenumber=input("Enter the Vehicle Number:")
        self.vehicletype=int(input("Enter the Vehicle Type\n1. Car/Jeep/Van\n2. Light Commercial Vehicles(LCV)\n3.Bus/Truck\n4.Upto 3 Axle Vehicle\n5.4 to 6 Axle\n6.HCM/EME\n7. 7 or more Axle :"))
        print()
        self.passtype=int(input("Enter your preferred option\n1. Single Journey(press 1)\n2.Return Journey(press 2) \n3.Monthly Pass(press 3):"))
        print()
        today=date.today()
        now = datetime.now()
        dates= today.strftime("%d-%m-%y")
        time=now.strftime("%H:%M:%S")
        str1=str(dates)
        str2=str(time)
        self.passtype1="Single Journey"
        if self.passtype==1:
            self.passtype1="Single Journey"
            if self.vehicletype==1:
                self.vehicletype1="Car/Jeep/Van"
                self.tolltax="105"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs105")
            elif self.vehicletype==2:
                self.vehicletype1="Light Commercial Vehicles(LCV)"
                self.tolltax="180"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs180")
            elif self.vehicletype==3:
                self.vehicletype1="Bus/Truck"
                self.tolltax="360"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs360")
            elif self.vehicletype==4:
                self.vehicletype1="Upto 3 Axle Vehicle"
                self.tolltax="580"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs580")
            elif self.vehicletype==5:
                self.vehicletype1="4 to 6 Axle"
                self.tolltax="580"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"',,'"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs580")
            elif vehicletype==6:
                self.vehicletype1="HCM/EME"
                self.tolltax="580"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs580")
            elif self.vehicletype==7:
                self.vehicletype1="7 or more Axle"
                self.tolltax="580"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype1+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs580")
            else:
                print("Enter Valid Option")
                
        elif(self.passtype==2):
            self.passtype2="Return Journey"
            if self.vehicletype==1:
                self.vehicletype1="Car/Jeep/Van"
                self.tolltax="180"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs180")
            elif self.vehicletype==2:
                self.vehicletype1="Light Commercial Vehicles(LCV)"
                self.tolltax="270"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs270")
            elif self.vehicletype==3:
                self.vehicletype1="Bus/Truck"
                self.tolltax="540"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs540")
            elif self.vehicletype==4:
                self.vehicletype1="Upto 3 Axle Vehicle"
                self.tolltax="870"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs870")
            elif self.vehicletype==5:
                self.vehicletype1="4 to 6 Axle"
                self.tolltax="870"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs870")
            elif self.vehicletype==6:
                self.vehicletype1="HCM/EME"
                self.tolltax="870"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs870")
            elif self.vehicletype==7:
                self.vehicletype1="7 or more Axle"
                self.tolltax="870"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype2+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs870")
            else:
                print("Enter Valid Option")
        elif(self.passtype==3):
            self.passtype3="Monthly Pass"
            if self.vehicletype==1:
                self.vehicletype1="Car/Jeep/Van"
                self.tolltax="3100"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs3100")
            elif self.vehicletype==2:
                self.vehicletype1="Light Commercial Vehicles(LCV)"
                self.tolltax="5425"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,tolltax,passtype,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs5425")
            elif self.vehicletype==3:
                self.vehicletype1="Bus/Truck"
                self.tolltax="10845"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs10845")
            elif self.vehicletype==4:
                self.vehicletype1="Upto 3 Axle Vehicle"
                self.tolltax="17430"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs17430")
            elif self.vehicletype==5:
                self.vehicletype1="4 to 6 Axle"
                self.tolltax="17430"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltaxdate1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs17430")
            elif self.vehicletype==6:
                self.vehicletype1="HCM/EME"
                self.tolltax="17430"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs17430")
            elif self.vehicletype==7:
                self.vehicletype1="7 or more Axle"
                self.tolltax="17430"
                status=myc.execute("Insert into usertax(userid,name,vehiclenumber,vehicletype,passtype,tolltax,date1,time1)"+
                   "values('"+self.id1+"','"+self.name+"','"+self.vehiclenumber+"','"+self.vehicletype1+"','"+self.passtype3+"','"+self.tolltax+"','"+str1+"','"+str2+"')")
                mydb.commit()
                mydb.close()
                print("You Have to Pay Rs17430")
            else:
                print("Enter Valid Option")
        print("----------------------------")
        print("|     Happy And            |")
        print("|     Safe  Journey        |")
        print("----------------------------")
        mydb.close()
    def display(self):
        item_id=input("Enter Vehicle id to search: ")
        print()
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        try:
            myc.execute("select * from usertax where userid='"+item_id+"'")
            rs=myc.fetchall()
            for row in rs:
                print("Vehicle ID------> ",row[0])
                print("Name------------> ",row[1])
                print("Vehicle Number--> ",row[2])
                print("Vehicle Type----> ",row[3])
                print("Toll Tax--------> ",row[4])
                print("Time------------> ",row[5])
                print("Date------------> ",row[6])
                print("Pass Type-------> ",row[7])
        except:
            print("Unable to fetch data")
        mydb.close()

    def collection(self):
        print()
        self.lis=[]
        self.n=0
        self.total_tax=[]
        self.total=0
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        try:
            self.date=input("Enter the date to search to get the total: ")
            for i in range(0,9):
                myc.execute("select * from usertax where date1='"+self.date+"'")
                rs=myc.fetchall()
            for i in rs:
                self.lis.append(i[6])
            for j in range(0,len(self.lis)):
                if(self.lis[j]==self.date):
                    myc.execute("select * from usertax where date1='"+self.lis[j]+"'")
                    rs=myc.fetchall()
            for i in rs:
                self.total_tax.append(i[4])
            for n in range(0,len(self.total_tax)):
                           self.total=self.total+self.total_tax[n]
            print("The total collection of the day: ",self.total)
        except:
            print("Unable to fetch data")
        mydb.close()

    def modify(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        self.vehicleid=input("Enter your vehicle ID:")
        print("_________________________________________________________________________________")
        print("| Type                            Single Journey   Return Journey   Monthly Pass|")
        print("|1.Car/Jeep/Van                        105            155             3100      |")
        print("|2.Light Commercial Vehicles(LCV)      180            270             5425      |")
        print("|3.Bus/Truck                           360            540             10845     |")
        print("|4.Upto 3 Axle                         580            870             17430     |")
        print("|5. 4 to 6Axle                         580            870             17430     |")
        print("|6.HCM/EME                             580            870             17430     |")
        print("|7. 7 or more Axle                     580            870             17430     |")
        print("_________________________________________________________________________________")
        print()
        self.passtype=input("Enter your pass type:")
        self.typeofvehicle=input("Enter your vehicle type:")
        self.amount1=input("Enter Toll Tax Amount:")
        try:
            myc.execute("update usertax set passtype='"+self.passtype+"',vehicletype='"+self.typeofvehicle+"',tolltax='"+self.amount1+"' where userid='"+self.vehicleid+"'")
            mydb.commit()
            print("Record Updated Succesfully")
        except:
            mydb.rollback()
            print("Unable to update record")
        mydb.close()
    def number_vehicle(self):
        self.lis=[]
        self.total=[]
        self.lcv=0
        self.hcm=0
        self.cjv=0
        self.axle=0
        self.bt=0
        self.axle1=0
        self.axle2=0
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        self.date=input("Enter the date to search to get the total: ")
        for i in range(0,9):
            myc.execute("select * from usertax where date1='"+self.date+"'")
            rs=myc.fetchall()
        for i in rs:
            self.lis.append(i[6])
        for j in range(0,len(self.lis)):
            if(self.lis[j]==self.date):
                myc.execute("select * from usertax where date1='"+self.lis[j]+"'")
                rs=myc.fetchall()
        for i in rs:
            self.total.append(i[3])
        for t in range(0,len(self.total)):
            if(self.total[t]=="Light Commercial Vehicles(LCV)"):
                self.lcv+=1
            elif(self.total[t]=="HCM/EME"):
                self.hcm+=1
            elif(self.total[t]=="Car/Jeep/Van"):
                self.cjv+=1
            elif(self.total[t]=="7 or more Axle"):
                self.axle+=1
            elif(self.total[t]=="Bus/Truck"):
                self.bt+=1
            elif(self.total[t]=="4 to 6 Axle"):
                self.axle1+=1
            elif(self.total[t]=="Upto 3 Axle Vehicle"):
                self.axle2+=1

        print("Light Commercial Vehicles(LCV): ",self.lcv)
        print("HCM/EME                       : ",self.hcm)
        print("Car/Jeep/Van                  : ",self.cjv)
        print("7 or more Axle                : ",self.axle)
        print("Bus/Truck                     : ",self.bt)
        print("4 to 6 Axle                   : ",self.axle1)
        print("Upto 3 Axle Vehicle           : ",self.axle2)
        print()
        print("Total number of Vehicle passed in a day:",self.lcv+self.hcm+self.cjv+self.axle+self.bt+self.axle1+self.axle2)
    def pass_type(self):
        self.lis=[]
        self.total=[]
        self.single=0
        self.monthly=0
        self.returnj=0
        mydb = mysql.connector.connect(host="localhost",user="root",password="varaddeshmukh",database="logintax")
        myc=mydb.cursor()
        self.date=input("Enter the date to search to get the total: ")
        for i in range(0,15):
            myc.execute("select * from usertax where date1='"+self.date+"'")
            rs=myc.fetchall()
        for i in rs:
            self.lis.append(i[6])
        for j in range(0,len(self.lis)):
            if(self.lis[j]==self.date):
                myc.execute("select * from usertax where date1='"+self.lis[j]+"'")
                rs=myc.fetchall()
        for i in rs:
            self.total.append(i[7])
        for t in range(0,len(self.total)):
            if(self.total[t]=="Single Journey"):
                self.single+=1
            elif(self.total[t]=="Return Journey"):
                self.returnj+=1
            elif(self.total[t]=="Monthly Pass"):
                self.monthly+=1

        print("Single Journey   : ",self.single)
        print("Return Journey   : ",self.returnj)
        print("Monthly Pass    : ",self.monthly)
    
n1=TollTax()
n1.LoginAccount()
while(True):
    print()
    print("--------------Welcome to Toll Plaza------------")
    print("1.Pay the Tax")
    print("2.Display Vehicle Details")
    print("3.Display the collection(According to the date)")
    print("4.Modify the  Details")
    print("5.Number of vehicle passed in a day")
    print("6.Details regarding pass type") 
    print("0.Exit")
    print()
    choice=int(input("Enter your choice:"))
    if choice==1:
        n1.paythetax()
        
    elif choice==2:
        n1.display()

    elif choice==3:
        n1.collection()

    elif choice==4:
        n1.modify()
    elif choice==5:
        n1.number_vehicle()
    elif choice==6:
        n1.pass_type()
        
    elif choice==0:
        sys.exit()

    else:
        print("Enter valid option")

