
print("Welcome to My text-based RPG game!\n")
print("The game will be played via choices (1) or (2) after a question you must write 1 or 2 anything else will take you through choice one\n")
print("Context: You wake up after a normal day, but for some reason you are on a random island you have never seen before.\n")
print("You get out of a random bed and must dedcide where to go first")
bathorclosed=input("Go to the Bathroom (1) or the closed door(2)?\n")

if bathorclosed != "1" or "2":
    bathorclosed ="1"
if bathorclosed == "1":
    print("You enter the bathroom there is nothing unusual, you also use the bathroom and go back to the closed door")
if bathorclosed == "2":
    print("You inspect the closed door but do not discover anything.")


#var=input("(1) (2)")
print("You try the dorknob, and it opens into a dark hallway, the visibility is very low and you cannot see much. This is odd, you think, as you woke up to daylight and the window behind you shows the suns reflection from the ocean.\n")
hallwayorwindow = input("You now have a choice if you would like to go through hallway (1) or jump out via the window(2)")
if hallwayorwindow != "1" or "2":
    hallwayorwindow = "1"
if hallwayorwindow == "1":
    print("You explore through the dark hallway, cautious of any individuals, you walk through the dark hallway and at the end you feel a door.\n")
    print("You try to open the door but it does not budge and you hear yelling and footsteps coming through the door.\n")
    print("This scares you and you run back through the hallway and jump out the window\n")
if hallwayorwindow == "2":
    print("you jump out of the window and you get shocked by how beautiful this island truly is, it seems like nature documentaries you used to watch.\n")
    print("This is not good news for you, however, as you are a teenager and want your normal life back, and this bizarre island means you are ridiculously far from home!\n")
print("Behind you, you hear footsteps and someone yelling at you. This leaves you with another choice!\n")
runortalk=input("Do you try to outrun the person behind you (1) or attempt to talk to the person (2).")
if runortalk != "1" or "2":
    runortalk = "1"
if runortalk == "1":
    print("You run as fast and as far as you can, the person behind you also starts running after you!\n")
    print("Slowly but surely, the person behind you catches up to you and you start screaming scared that this person wants to harm you\n")
    print("Tired from running, you give up and decide to talk to this person")
if runortalk == "2":
    print("You decide to talk to this individual, cautious that they may want to harm you\n")
print("You say: Who are you and where am I!\n")
print("Person says: އައި އޮންލީ ޓްރައި ހެލްޕް ޔޫ އައި ފެއިންޑް ޔޫ އިއްޔެ ނުރައްކާތެރި ދޯންޏެއްގައި (Foreign Language you don't understand)\n")
print("You try to sign out that you don't understand.\n")
print("The person understands and tries to sign to you that they want to give you food and help you out.\n")
print("You trust and believe this individual and they guide you to the front of the house \n")

