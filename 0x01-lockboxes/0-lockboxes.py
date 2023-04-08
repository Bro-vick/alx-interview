#!/usr/bin/python3
""" Lockboxes Algorithm """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)  # This gets the number of boxes
    unlockedBoxes = [0] # This initializes a list with the first box (index 0)
    for boxNum, box in enumerate(boxes): # Loop through each box and its index
        for key in box:  
            """ Here we loop through each key  in the current box and check 
            if the key can open a new box that hasn't been unlocked yet by 
            checking if the key is less than the total number of boxes (n),
            - if the key has not been added to the list of unlocked boxes 
            (unlocked_boxes), and if the key does not unlock the current box.
            """
            if key < n and key not in unlockedBoxes and key != boxNum:
                unlockedBoxes.append(key)
    return len(unlockedBoxes) == n
