# Monty-Hall-Problem-s
In this article, we are going to see how to create Monty Hall games using Pygame in Python. Monty Hall was a game show of the American television game show Let’s Make a Deal. 

Suppose you’re on a game show, and you’re given the choice of three doors, Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which has a goat. He then says to you, “Do you want to pick door No. 2?” Is it to your advantage to switch your choice?

Work Flow and Logic 
The entire simulation can be condensed into the following points:

Since there are three doors, a random permutation of the numbers 1, 2, 3 would be generated, each number representing the door number. The first two numbers of this randomly generated permutation would correspond to the doors behind which goats are present, and the third number would be the door number behind which there is a car.
Once the configuration is generated, the same is represented graphically through images. There is an image for each configuration.
There is one point to be taken care of — according to the puzzle, after the user has chosen a door number, only the door behind which there is a goat is to be revealed. So, if the user selects the door behind which there is a car, then any of the two remaining doors can be revealed. However, if the user selects a door behind which there is a goat, only one of the two remaining doors can be revealed (as it is not permissible to reveal the door that the user has selected).
