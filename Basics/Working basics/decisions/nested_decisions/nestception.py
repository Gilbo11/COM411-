print("where should i look")
place = input()
if place == "in the bedroom":
        print("where should i look")
        bedroom_place = input()
        if bedroom_place == "under the bed":
            print("found some shoes but no batteries")
        else:
            print("Found some mess but no battery.")

elif place == "in the bathroom":
        print("where in the bathroom should i look?")
        bathroom_place = input()
        if bathroom_place == "in the bathtub":
            print("found a rubber duck but no battery")
        else:
            print("Found a wet surface but no battery.")

elif place == "in the lab":
        print("where in the lab should i look")
        lab_place = input()
        if lab_place == "on the table":
            print("yes i found my battery")
        else:
            print("found some tools but no battery")

else:
    print("I do not know where that is but i will keep looking")
