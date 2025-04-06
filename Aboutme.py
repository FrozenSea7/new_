def PSW () :
    QUEs=str(eval(input("What do you want to question")))
    if QUEs == "youtube":
        print("Xaero1362playmc")
    elif QUEs == "Twitch" or QUEs == "Discord" or QUEs == "Steam" or QUEs == "xbox" or QUEs == "MinecraftForum":
        print("Xaero1362")
    elif QUEs == "Minecraft wiki":
        print("Rexlex")

def ABOUT():
    print("A human from China.")

def main():
    while True :
        SCr=str(eval(input("Ask")))
        if SCr == "#PSW" :
            PSW()
        if SCr == "#ABOUT" :
            ABOUT()

main()


    
