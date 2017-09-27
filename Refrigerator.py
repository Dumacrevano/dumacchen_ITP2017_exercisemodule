def main():
    topspace = {"Top Space": {}}
    midspace = {"Mid Space": {}}
    bottomspace = {"Bottom Space": {}}
    topspacevolume = 10
    midspacevolume = 10
    bottomspacevolume = 10
    print("Welcome to the Refrigerator!")
    while True:
        decide = input("Do You Want to Take Out/Put In Things Into the Refrigerator? Y/N ")
        if decide == "Y":
            action = input("Choose an Action: PUT/TAKE ")
            if action == "PUT":
                pickspace = input("Pick Space TOP/MID/BOTTOM: ")
                itemname = input("What Do You Want to Put In? ")
                itemvolume = int(input("Volume of Item: "))
                if pickspace == "TOP":
                    if topspacevolume-itemvolume > -1:
                        topspace["Top Space"][itemname] = [itemvolume]
                        print(itemname, "is in the Fridge.")
                        topspacevolume = topspacevolume - itemvolume
                        print("Available Space is in the Top is ", topspacevolume)
                    else:
                        print("Not Enough Space in the Top, Check Middle and Bottom Space")
                if pickspace == "MID":
                    if midspacevolume-itemvolume > -1:
                        midspace["Mid Space"][itemname] = [itemvolume]
                        print(itemname, "is in the Fridge")
                        midspacevolume = midspacevolume - itemvolume
                        print("Available Space in the Middle is ", midspacevolume)
                    else:
                        print("Not Enough Space in the Middle, Check Top and Bottom.")
                if pickspace == "BOTTOM":
                    if bottomspacevolume-itemvolume > -1:
                        bottomspace["Bottom Space"][itemname] = [itemvolume]
                        print(itemname, "is in the Fridge")
                        bottomspacevolume = bottomspacevolume - itemvolume
                        print("Available Space in the Bottom is ", bottomspacevolume)
                    else:
                        print("Not Enough Space in the Bottom, Check Top and Middle.")
            if action == "TAKE":
                pickspace = input("Pick space TOP/MID/BOTTOM: ")
                itemname = input("What Do You Want to Take Out?")
                if pickspace == "TOP":
                    topspace["Top Space"][itemname]: [itemvolume]
                    topspacevolume = topspacevolume + itemvolume
                    print(itemname, "is out of the Fridge.")
                    print("Available Space in the Top is ", topspacevolume)
                    del topspace["Top Space"][itemname]
                if pickspace == "MID":
                    midspace["Mid Space"][itemname]: [itemvolume]
                    midspacevolume = midspacevolume + itemvolume
                    print(itemname, "is out of the Fridge.")
                    print("Available Space in the Middle is ", midspacevolume)
                    del midspace["Mid Space"][itemname]
                if pickspace == "BOTTOM":
                    bottomspace["Bottom Space"][itemname]: [itemvolume]
                    bottomspacevolume = bottomspacevolume + itemvolume
                    print(itemname, "is out of the Fridge.")
                    print("Available Space in the Bottom is ", bottomspacevolume)
                    del bottomspace["Bottom Space"][itemname]
        else:
            print("Thank You for Using the Refrigerator.")
            break
