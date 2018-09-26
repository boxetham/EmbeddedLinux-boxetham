In this homework I made a program that turns on an LED in response to a button 
press using mmap. I had to use mmap 3 times to access GPIO0, GPIO1, and GPIO3 due
to the pins I used. I then just check the input from the button and assign the LED
appropriately. 

Next I toggled a gpio pin as fast as I could. After set up, the program just makes
an on call then an off call with nothing else in a while loop. This is done with mmap. 
You can find this in gpioToggle. As you can see in the hw04 mmap speed document, 
I got a much faster speed than what I got in hw02. 

After this I learned how to use the display. The text and text1 documents are the scripts
that I used to the stuff with imagemagick. The on script is where I rotate the screen. If
there is a way I am supposed to rotate without rotating the actual display when turning it
on I couldn't figure it out. I noticed that there was an --edit command with fbi but then 
you have to give it input from the keyboard and I didn't know how to hook a keyboard up to 
the display. The pictures of the different things I did with the display can be found in the
homework 4 display pictures folder. 


========================
Professor Yoder's Comments

Looks good.  Wow, 340ns IS much faster.
I don't see your Memory Map numbers.

Score: 9/10