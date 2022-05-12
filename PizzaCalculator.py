Bestelling = {}

def addPizzatoList():
    q = input("Wilt u nog een pizza? [J/N] \n")
    if q == "J":
        print(Bestelling)
        getPizzaChoice()
    elif q == "N":
            print(Bestelling)
            exit()

def convertNumbers():
    global PersonKeuze
    if PersonKeuze <= 1:
        PersonKeuze = "Small"
        Bestelling["Bestelling: "] = PersonKeuze
        addPizzatoList()
    elif PersonKeuze <= 2:
        PersonKeuze = "Medium"
        Bestelling["Bestelling: "] = PersonKeuze
        addPizzatoList()
    elif PersonKeuze <= 3:
        PersonKeuze = "Large"
        Bestelling["Bestelling: "] = PersonKeuze
        addPizzatoList()


def getPizzaChoice():
    global PersonKeuze
    while True:
        print("""\033[0m
        Kies uw pizza:
            [1] Small
            [2] Medium
            [3] Large
            """)
        try:
            PersonKeuze = int(input("Kies hier een pizza: "))
            convertNumbers()
        except ValueError:
            print("Sorry maar ik snap u niet.")
            getPizzaChoice()
        
        
    

def ShowLargeText():
    print("""\033[1;31;40m
██████╗ ██╗███████╗███████╗ █████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██║  ███╔╝   ███╔╝ ███████║    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║███████╗███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   
""")
ShowLargeText()
getPizzaChoice()
