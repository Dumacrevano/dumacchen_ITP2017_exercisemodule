def test():
    x = input("which one do you want to run?"
          "\nA. Pokemon Simulator \n"
          "B. Fridge Simulator\n")
    if(x.upper() == "A"):
        import No5
        No5.main()
    elif(x.upper() == "B"):
        import Refrigerator
        Refrigerator.main()
    else:
        print("No Program Available for that choice")
        test()
test()