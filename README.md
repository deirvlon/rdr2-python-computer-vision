# rdr2-python-computer-vision
Red Dead Redemption 2 playing bot. Follows the trace on the map and move the player accordingly

## Running script

Run `main.py` after 5 seconds it will start. Before it starts be sure that you are in the game.

## Explanation -  How it works?


IDEA is to get some part of minimap and process it and control mouse movements in order to direct player accordingly


# ![RDR2](https://i.ibb.co/QYxS2z3/Screenshot-2021-01-31-000406.png)


CROP Little portion of the minimap
# ![Minimap](https://i.ibb.co/K6y5ZyM/Screenshot-2021-01-31-001443.png)



Then we use color masking in order to get the only RED color which indicates our line on map. After processing we will get this image.
# ![Processing](https://i.ibb.co/8PBmDNW/Screenshot-2021-01-31-002101.png)




So now we can use this image in order to guess the direction the player has to turn and feed into the mouse movements.
# ![Processing](https://i.ibb.co/RT4smZb/Screenshot-2021-01-31-001745.png)

Our purpose is to hold that straight line in the middle. If the line bends, so our player also have to turn in that direction. In order to find which way we have to turn we get all the coordinates of pixels in the processed image which contains (#000) color with is BLACK. For finding the direction we just find average of coordinates and take the X coordinate of that averaged point and use it for calculating the ERROR. 
# ![Processed image](https://i.ibb.co/zmvFzpF/Screenshot-2021-01-ss31-003309.png)



Error calculation is easy just find the center of the image and define it as TARGET.
`Error = Target - Average;`


# ![Turn](https://i.ibb.co/T0Th2vW/Screenshot-2021-01-31-003309.png)

The Red line indicates the center and the blue point indicates the average.
