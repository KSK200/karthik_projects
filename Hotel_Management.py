from datetime import date
from datetime import datetime
from termcolor import colored,cprint

class Hotel:
    
    def SouthIndianDishesList(self):
        print("")
        print("[South Indian Dish List]")
        print("")
        print("Item                Amount")
        print("----                ------")
        print("1.Idli               30Rs")
        print("2.Sambar vada        60Rs")
        print("3.Upama              25Rs")
        print("4.Masala Upama       30Rs")
        print("5.Puri Sagu          40Rs")
        print("6.Plain Dosa         50Rs")
        print("7.Masala Dosa        60Rs")
        print("8.Onion Dosa         55Rs")

    
    def SnackSItemsList(self):
        print("")
        print("[Snack items list]")
        print("")
        print("Item                   Amount")
        print("----                   ------")
        print("1.Panipuri              30Rs")
        print("2.Masala Puri           25Rs")
        print("3.Shev Puri             35Rs")
        print("4.Dahi Puri             40RS")
        print("5.Gobi Manchuri         60RS")
        print("6.Pav Bhaji             50RS")

    def  Bevarages(self):
        print("")
        print("[Bevarge items list]")
        print("")
        print("Item                   Amount")
        print("----                   ------")
        print("1.Tea                   10Rs")
        print("2.Coffee                10Rs")       
        print("3.Badam Milk            15Rs")
        print("4.Milk                  15Rs")

    def details(self,name,pno):
        self.name=name
        self.pno=pno
        print(name," visit again to Shivsagar Hotel")
        print("")

    def order_items(self,item_name,no_of_items):
        self.item_name=item_name
        self.no_of_items=no_of_items
        price=0
        if(self.item_name=="idli"):
            price=self.no_of_items*30
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="sambar vada" or self.item_name=="sambarvada"):
            price=self.no_of_items*60
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="upama"):
            price=self.no_of_items*25
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="maasla upama"):
            price=self.no_of_items*30
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="puri sagu"):
            price=self.no_of_items*40
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="plain dosa"):
            price=self.no_of_items*50
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")

        elif(self.item_name=="masala dosa"):
            price=self.no_of_items*60
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="onion dosa"):
            price=self.no_of_items*55
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")

        elif(self.item_name=="panipuri"):
            price=self.no_of_items*30
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="shev puri"):
            price=self.no_of_items*40
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")

        elif(self.item_name=="masala puri"):
            price=self.no_of_items*25
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="dahi puri"):
            price=self.no_of_items*40
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")

        elif(self.item_name=="pav bhaji"):
            price=self.no_of_items*50
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="gobi manchuri"):
            price=self.no_of_items*60
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="tea"):
            price=self.no_of_items*10
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
                
        elif(self.item_name=="coffee"):
            price=self.no_of_items*10
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")

        elif(self.item_name=="badam milk"):
            price=self.no_of_items*15
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        elif(self.item_name=="milk"):
            price=self.no_of_items*15
            print("")
            print("Your purchase!!")
            print("")
            print("Item name=",item_name)
            print("Number of Items=",no_of_items)
            print("Total Amount=",price)
            print("")
        
        else:
            print(self.item_name," is invalid item that you entered plz refer the menu and enter")

h=Hotel()
item_name=""
No_of_items=0

print("")
print("--------------------------------")
print(colored('Hello welcome To Shivsagar Hotel','yellow'))
print("--------------------------------")
print("")

name=input("Enter your Name: ")
phone_no=int(input("Enter your Phone Number: "))


choice=0

while(choice!=4):
    print("")
    print("<Choose the option>")
    print("")
    print("1.Menu\n2.Order\n3.exit")
    print("")
    choice=int(input("Your option:"))

    if(choice==1):
        h.SouthIndianDishesList()
        h.SnackSItemsList()
        h.Bevarages()
    
    elif(choice==2):
        item_name=input("Enter The Item name: ").lower()
        No_of_items=int(input("How much do you want to purchase mention the item count: "))
        h.order_items(item_name,No_of_items)
        print("")
        today = date.today()    
        print("Bill Date:", today)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Bill Time =", current_time)
        
    elif(choice==3):
        print("Thank you visit Again!!")
        h.details(name,phone_no)
        exit()
    
    else:
        print(choice," is a invalid choice")

