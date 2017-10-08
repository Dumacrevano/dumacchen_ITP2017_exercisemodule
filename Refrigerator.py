def main():
    topspace = {"Top Space": {}}
    midspace = {"Mid Space": {}}
    bottomspace = {"Bottom Space": {}}
    topspacevolume = 10#taking half is allowed
    midspacevolume = 10
    bottomspacevolume = 10
    print("Welcome to the Refrigerator!")
    while True:
        decide = str.upper(input("Do You Want to Take Out/Put In Things Into the Refrigerator? Y/N "))
        if decide == "Y":
            action = str.upper(input("Choose an Action: PUT/TAKE "))
            if action == "PUT":
                pickspace = str.upper(input("Pick Space TOP/MID/BOTTOM: "))
                itemname = str.title(input("What Do You Want to Put In? "))
                global qty
                qty=int(input("how many item?"))
                global itemvolume
                itemvolume = int(input("total volume of Item: "))
                global item_1_Vol
                item_1_Vol=itemvolume/qty
                if pickspace == "TOP":
                    if topspacevolume-itemvolume > -1:
                        topspace["Top Space"][itemname] = [itemvolume]
                        print(str(qty),itemname,"is in the Fridge.")
                        topspacevolume = topspacevolume - itemvolume
                        print("Available Space is in the Top is ", topspacevolume)
                    else:
                        print("Not Enough Space in the Top, Check Middle and Bottom Space")
                if pickspace == "MID":
                    if midspacevolume-itemvolume > -1:
                        midspace["Mid Space"][itemname] = [itemvolume]
                        print(str(qty),itemname,"is in the Fridge")
                        midspacevolume = midspacevolume - itemvolume
                        print("Available Space in the Middle is ", midspacevolume)
                    else:
                        print("Not Enough Space in the Middle, Check Top and Bottom.")
                if pickspace == "BOTTOM":
                    if bottomspacevolume-itemvolume > -1:
                        bottomspace["Bottom Space"][itemname] = [itemvolume]
                        print(str(qty),itemname,"is in t he Fridge")
                        bottomspacevolume = bottomspacevolume - itemvolume
                        print("Available Space in the Bottom is ", bottomspacevolume)
                    else:
                        print("Not Enough Space in the Bottom, Check Top and Middle.")

            if action == "TAKE":
                print(topspace, "\n", midspace, "\n", bottomspace)
                pickspace = str.upper(input("Pick space TOP/MID/BOTTOM: "))
                itemname = str.title(input("What Do You Want to Take Out?"))
                qty_taken=int(input("how many do you want to take"))

                if pickspace == "TOP":
                    topspace["Top Space"][itemname]: [itemvolume]
                    topspacevolume = topspacevolume +(item_1_Vol)*qty_taken
                    itemvolume-=(item_1_Vol*qty_taken)
                    print(str(qty_taken),itemname, "is out of the Fridge.")
                    print("Available Space in the Top is ", topspacevolume,"\n"+itemname,"in fridge is:",itemvolume,qty-qty_taken)
                    if itemvolume<=0:
                        del topspace["Top Space"][itemname]
                        print(topspace)
                if pickspace == "MID":
                    midspace["Mid Space"][itemname]: [itemvolume]
                    midspacevolume = midspacevolume + (item_1_Vol) * qty_taken
                    itemvolume -= (item_1_Vol * qty_taken)
                    print(str(qty_taken), itemname, "is out of the Fridge.")
                    print("Available Space in the Top is ", midspacevolume, "\n" + itemname, "in fridge is:",
                          itemvolume, qty - qty_taken)
                    if itemvolume <= 0:
                        del topspace["Mid Space"][itemname]
                        print(topspace)
                if pickspace == "BOTTOM":
                    bottomspace["Bottom Space"][itemname]: [itemvolume]
                    bottomspace = bottomspace + (item_1_Vol) * qty_taken
                    itemvolume -= (item_1_Vol * qty_taken)
                    print(str(qty_taken), itemname, "is out of the Fridge.")
                    print("Available Space in the Top is ", bottomspacevolume, "\n" + itemname, "in fridge is:",
                          itemvolume, qty - qty_taken)
                    if itemvolume <= 0:
                        del topspace["Top Space"][itemname]
                        print(topspace)
        else:
            print("Thank You for Using the Refrigerator.")
            break
main()
