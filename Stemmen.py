from time import sleep as wait

partijList = {}


#! Invullen van Partijnamen!
def getParties():
    while True:
        try:
            Partijnaam = input("Naam Partij: ")
            if Partijnaam == "Stop" or Partijnaam == "stop":
                break
            else:
                partijList[Partijnaam] = 0
                print(partijList)
        except ValueError:
            print("Gebruik geen nummers.")            
    return partijList

def partyDetails():
    print("-----------------------")
    print("Partijen: " + str(partijList))
    print("Aantal Partijen: " + str(len(partijList)))
    print("----------------------")

#! Stemmen partijen!

def PartijStemmer():
    while True:
        q2 = input("Welke Partij wil je stemmen \n")
        if q2 in partijList:
            partijList[q2] += 1
            print(partijList)
        elif q2 == "Stop" or q2 == "stop":
            max_key = max(partijList, key=partijList.get)
            print("Winnende Partij: " + str(max_key))
            break
        elif q2 not in partijList:
            print("Sorry ik begrijp je niet...")

#! Klaar voor de Verkiezingen
getParties()
wait(2)
print("Alle partijen zijn genoteerd...")
partyDetails()
print("Klaar voor de Verkiezingen...")
wait(1)
PartijStemmer()