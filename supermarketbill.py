from datetime import datetime
name = input("Enter Customer Name: ")
Phnumber = input("Enter Customer Number: ")
# List of items in supermarket
lists = '''
rice        Rs 50/kg
sugar       Rs 40/kg
oil         Rs 170/liter
bengal Gram Rs 150/kg
gram Masala Rs 30
salt        Rs 20/kg
curd        Rs 90/kg
panner      Rs 100/kg
ground Nuts Rs 70/kg
milk        Rs 40/liter
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []  # Items List
qlist = []  # Quantity List
plist = []  # Price List

# Rates per Items
items = {
    'rice': 50,
    'sugar': 40,
    'oil': 170,
    'bengal Gram': 150,
    'gram Masala': 30,
    'salt': 20,
    'curd': 90,
    'panner': 100,
    'ground Nuts': 70,
    'milk': 40
}

Option = int(input("For list of items press 1:"))
if Option == 1:
    print(lists)

for i in range(len(items)):
    input1 = int(input("Press 1 for Buy and 2 for Exit:"))
    if input1 == 2:
        break
    if input1 == 1:
        item = input("Enter Your Item: ")
        quantity = int(input("Enter quantity: "))
        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, items[item], price))  # Corrected here
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            # Calculate GST and final amount
            gst = (totalprice * 5) / 100
            finalamount = gst + totalprice

        else:
            print("Sorry, entered item not found.")
else:
    print("You entered a wrong number.")

# Ask if the user wants to print the bill
inp = input("Print The Bill Yes Or No: ")
if inp == 'yes':  # Removed .lower()
    if finalamount != 0:
        print(25*"=","Gaurav Supermarket",25*"=")
        print(28*" ","Adilabad")
        print("Name:",name,30*" ","Date ",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'Quantity',2*" ",'Price',2*" ")
        for i in range(len(pricelist)):
            print(i,8*' ',5*' ', ilist[i],8*' ' ,qlist[i],8*" ",plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print(50*" ","Gst Amount:",'Rs',gst)
        print(50*" ",'FinalAmount:','Rs',finalamount)
        print(75*"-")
        print(25*" ","Thanks For Visiting")
        print(75*"-")
        
        
        
        
        
        