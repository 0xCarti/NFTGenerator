from PIL import Image
import os
import sys, random, time

# Trackers
outputStrings = []
backgrounds = []
total_traits = []
total_outputs = 1
debug = False

# Check for debug
if len(sys.argv) >= 1:
    if "-d" in str(sys.argv):
        debug = True
        print("Debug set to true.")

# Load Backgrounds
paths = os.listdir("./backgrounds/")
for path in paths:
    backgrounds.append(Image.open("./backgrounds/" + path))
total_outputs *= len(backgrounds)

# Load traits
traitFolders = os.listdir("./traits/")
for folder in traitFolders:
    traits = []
    paths = os.listdir("./traits/" + folder)
    for path in paths:
        traits.append(Image.open("./traits/" + folder + "/" + path))
    total_outputs *= len(traits)
    total_traits.append(traits)

# Display Debug Info
if debug:
    print("Loaded the following backgrounds.")
    for background in backgrounds:
        print("\t" + background.filename)
    print("Loaded the following traits.")
    for traits in total_traits:
        for trait in traits:
            print("\t" + trait.filename)

print(f"Max NFT's Generated = {total_outputs}.")

while len(outputStrings) < total_outputs:
    img = Image.new("RGBA", (600, 600), 0)
    background = random.choice(backgrounds)
    trait_string = background.filename
    background = background.convert("RGBA")
    img.paste(background, (0, 0), mask=background)
    for traits in total_traits:
        trait = random.choice(traits)
        trait_string += trait.filename
        trait = trait.convert("RGBA")
        img.paste(trait, (0, 0), mask=trait)

    if trait_string not in outputStrings:
        img.save("./outputs/nft#" + str(len(outputStrings)) + ".png")
        print(f"Saved NFT #{len(outputStrings)}")
        outputStrings.append(trait_string)

    #time.sleep(1)
