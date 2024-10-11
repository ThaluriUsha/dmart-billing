print("********WELCOME TO SMART POINT***********")
bag=0
thislist=[]
qty=[]
gitems=["sugar","gram flour","apples","onions","potatoes"]
gprice=[44,70,100,60,30]
kitems=["Veg Cutter","Grater","Blender","Bottles","Knife","Pan","Scissors"]
kprice=[50,80,400,150,80,300,50]
citems=["Shirt","Sneakers","Tees","Kurtis","Napkins","Jeans","Pants"]
cprice=[699,700,450,999,30,1399,499]
while(1):
    print("what you want to do?")
    ch=int(input("1.Go shopping\n2.Verify purchase\n3.Billing\n"))
    if(ch==1):
        print("which section you want to shop")
        ch1=int(input("1.Groceries\n2.Kitchen\n3.Clothing\n"))
        if(ch1==1):
           
            print("****welcome to groceries section******")            
            
            while(1):
                ch3=int(input("1.Add to cart\n2.Remove from Cart\n3.Exit Groceries section\n"))
                if(ch3==1):
                    print("what you want to buy?")
                    print("1.  Sugar              44Rs/kg")
                    print("2.  Gram flour         70Rs/kg")
                    print("3.  Apples             100Rs/kg")
                    print("4.  Onions              60Rs/kg")
                    print("5.  potatoes            30Rs/kg")
                    ch2=int(input("enter the item to buy(eg. for Sugar enter 1):\n"))
                    thislist.append(gitems[ch2-1])
                    qty=int(input("enter no of kgs:\n"))
                    bag+=gprice[ch2-1]*qty
                    print("Total bag value:",bag,"Rs \nitems:",thislist)
                elif(ch3==2):
                    if bag!=0:
                        rmv=int(input("Which item you want to remove\n"))
                        if gitems[rmv-1] in thislist:
                            thislist.remove(gitems[rmv-1])
                            bag-=gprice[rmv-1]*qty 
                            print("Total bag value:",bag,"Rs \nitems:",thislist)
                        else:
                            print("item is not present in cart")
                    else:
                        print("bag is empty")
                elif(ch3==3):
                    break
                else:
                    print("invalid choice")
        elif(ch1==2):
    
            print("******Welcome to Kitchen Section********")
            
            
            while(1):
                ch3=int(input("1.Add to cart\n2.Remove from Cart\n3.Exit Kitchen section\n"))
                if(ch3==1):
                    print("what you want to buy?")
                    print("1.  Veg Cutter            50Rs/piece")
                    print("2.  Grater                80Rs/piece")
                    print("3.  Blender               400Rs/piece")
                    print("4.  Bottles               150Rs/piece")
                    print("5.  Knife                 80Rs/piece")
                    print("6.  Pan                   300Rs/piece") 
                    print("7.  Scissors              50Rs/piece")
                    
                    ch2=int(input("enter the item to buy(eg. for Scissors enter 7):\n"))
                    thislist.append(kitems[ch2-1])
                    qty=int(input("enter no of item:\n"))
                    bag+=kprice[ch2-1]*qty
                    print("Total bag value:",bag,"Rs \nitems:",thislist)
                elif(ch3==2):
                    if bag!=0:
                        rmv=int(input("Which item you want to remove\n"))
                        if kitems[rmv-1] in thislist:
                            thislist.remove(kitems[rmv-1])
                            bag-=kprice[rmv-1]*qty 
                            print("Total bag value:",bag,"Rs \nitems:",thislist)
                        else:
                            print("item is not present in cart")
                    else:
                        print("bag is empty")
                else:
                    break
        elif(ch1==3):
            print("*********welcome to clothing section**** ")           
            while(1):
                ch3=int(input("1.Add to cart\n2.Remove from Cart\n3.Exit Clothing section\n"))
                if(ch3==1):
                    print("what you want to buy?")
                    print("1.   Shirts                 699Rs/piece")
                    print("2.   Sneakers               700Rs/piece")
                    print("3.   Tees                   450s/piece")
                    print("4.   Kurtis                 999Rs/piece")
                    print("5.   Napkins               30s/piece")
                    print("6.   Jeans                 1399Rs/piece")
                    print("7.   Pants                 499Rs/piece")
                    
                    ch2=int(input("enter the item to buy(eg. for Tees enter 3):\n"))
                    thislist.append(citems[ch2-1])
                    qty=int(input("enter no of item:\n"))
                    bag+=cprice[ch2-1]*qty
                    print("Total bag value:",bag,"Rs \nitems:",thislist)
                elif(ch3==2):
                    if bag!=0:
                        rmv=int(input("Which item you want to remove\n"))
                        if citems[rmv-1] in thislist:
                            thislist.remove(citems[rmv-1])
                            bag-=cprice[rmv-1]*qty 
                            print("Total bag value:",bag,"Rs \nitems:",thislist)
                        else:
                            print("item is not present in cart")
                    else:
                        print("bag is empty")
                else:
                    break
        else:
            print("invalid choice")
    elif(ch==2):
        if bag==0:
            print("bag is empty!!!Nothing to verify")
        else:
            i=0
            while(i!=len(thislist)):
                if(thislist[i] in gitems or thislist[i] in citems or thislist[i] in kitems):
                    print("**********************")
                    print("\n",thislist[i]," is in stock")
                    i+=1
            print("**************************")
    elif(ch==3):
        if bag == 0:
            print("Bag is empty!!! Continue Shopping")
        else:
            name=input("enter name:\n")
            id=input("enter id:\n")
            phone=int(input("enter phone no:\n"))
            adress=input("enter adress")
            print("name: ",name ,"\t\t\t\t\t\t\t\t\t\t\t\tid:" ,id, "\nphone: ",phone,"\t\t\t\t\t\t\t\t\t\t\t\tadress: ",adress)
            print("*****Your SMART POINT Bill *******")
            print("Item\t\t\t\tPrice\t\t\tQty\t\t\tTotal Price")
                     

            for i in range(len(thislist)):
                item = thislist[i]
                qty = qty  
                if item in gitems:
                    index              	      =           gitems.index(item)
                    price_per_kg        =           gprice[index]
                    total_price            =           price_per_kg * qty
                elif item in kitems:
                    index                       =           kitems.index(item)
                    price_per_pcs       =           kprice[index]
                    total_price             =           price_per_pcs * qty
                elif item in citems:
                    index               	       =           citems.index(item)
                    price_per_pcs       =           cprice[index]
                    total_price             =           price_per_pcs * qty

                if item in gitems:
                    unit = "kg"
                else:
                    unit = "piece"
                print(item + "\t\t\t" + str(price_per_kg) + " Rs/" + unit + "\t\t" + str(qty) + "\t\t\t" + str(total_price))
                print("Total Amount: " + str(bag) + " Rs")
                print("*********************************************")
                print("   Thank you ",name," for shopping at SMART POINT")
                print("                 Visit again :)")
                print("*********************************************")
                thislist = []
                bag = 0
                break
else:
    print("invalid choice")
