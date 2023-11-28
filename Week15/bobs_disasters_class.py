import random

class Disasters:
    def __init__(self) -> None:
        pass

    def ShipIncorrectColor(self, colors, colorchoosen):
        disasterchance = random.randint(1, 2)

        if disasterchance == 1:
            randomcolor = random.randint(0,len(colors)-1)


            keysbad = colors.keys()
            keygood = []

            for key in keysbad:
                    keygood.append(key)

            newcasecolor = keygood[randomcolor]
            newcaseprice = colors.get(newcasecolor)


            if colorchoosen[0] != newcasecolor:
                print("\n#--------------------------------------------------------------------------------------------#")
                print(f"DISASTER HAS STRUCK:\n You chose {colorchoosen[0]} but somehow you ended up with {newcasecolor}")
                print("#----------------------------------------------------------------------------------------------#\n")
                return [newcasecolor, newcaseprice], newcaseprice
            
        return colorchoosen, colorchoosen[1]
    
    def failedDelivery(self, premium_shipping, warranty):
        if warranty == "n":
            if premium_shipping == "n":
                river = random.randint(1,10)
                if river <= 3:
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
            elif premium_shipping == "y":
                river = random.randint(1,10)
                if river == 1:
                    return("Uh Oh!, the UPS Driver drove into a river and destroyed your PC")
                else:
                    return("Your package was properly shipped")
        else:
            return("Your package was properly shipped")
        
    def WrongStorageOption(self, premium_shipping, warranty):
        # If the user buys a warranty then the user will be safe from the disaster
        if warranty == "n":
            
            # The user will still be safe if they choose premium shipping
            if premium_shipping == "n":
                intern_mistake = random.randint(1,10)

                # If no warrenty or premiun shipment was choosen the user will have
                # 50% of getting the wrong storage order
                if intern_mistake <= 5:
                    return("\nOops, sorry the new intern messed up your storage order choice.\n")
                else:
                    return("")
                
            elif premium_shipping == "y":
                    return("")
            
        else:
            return("")