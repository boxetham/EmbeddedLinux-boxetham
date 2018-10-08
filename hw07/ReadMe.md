leds.js: This file started from the example leds.js in exerises/iot/blynk.
         I set P9_14 as an output pin and I added a virtual pin on V1.
         I added a function that watch V1 and every time it changed it 
         read the new value, computed the fraction of the way the slider was
         and then wrote to the new led pin with an analog write. f
         The value is only updated when the slider is released.
