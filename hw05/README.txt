Makefile - this file contains the resulting makefile from the makefile exercise
it uses variables to set most of the flags needed in the gcc compiler
then uses the gcc compiler to compile the program first by compiling the 
.c file to the .o file and then create the executable

gpio_test.c - this file contains the code that makes the light toggle the on
and off state with a button push. I changed the io pins of the button and LED. 
it uses interrupts in order to achieve a faster response to GPIO. This happens 
in the kernel space. 

a.out_host.jpeg - shows the output of the hello world function when run on the 
host computer

a.out_bone.jpeg - shows the result from the cross compiling and the function being
run on the bone