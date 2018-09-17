The homework is an EtchASketch that check the position on two different
encoders and moves the position accordingly. The current position is 
represented by an orange light with the rest of it lighting it up green. 
The position moves just based on whether the encoder position is positive
or negative. The general flow of the program is set up of all the input and 
output channels (buttons, encoders, LED matrix), get input from the input
channels, then change the board values so the lights are powered accordingly, 
write the board, and then repeat. 

How to wire EtchASketch: 
Left/Right encoder on eQEP1
Up/Down encoder on eQEP2
Clear button on P9_42
Stop button on P9_23

The temp sensor script works by reading in values and then doing the 
corresponding math. It just uses the i2cget commands to read in each 
sensor. The sensors are wired to ground and then power to differeniate
the addresses of the temp sensors. 
