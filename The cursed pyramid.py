blocks = int(input("Enter the number of blocks: "))


height=0 #height of the pyramid
placedBlocks=0 #placed blocks in each layer
while blocks:
    if blocks > 0:
        placedBlocks+=1
        blocks-=placedBlocks
        if blocks<0:
            break
            print("woah! there!")
        else:
            print(height, placedBlocks, blocks, sep=",", end="\n")
            height+=1
    else:
        break

print("The height of the pyramid:", height)
