# SONIM: A package for converting images to sound using sonification. 

This project also serves the purpose of allowing us to practice the standard developer workflow.

We are anticipating to create a class that takes two inputs: 1. RGB image, 2. Time of sound (s).
The function we expect to be created are:
* Func1 => Blue channel - Red channel
* Func2 => A mapping of intensity to frequency to create a sin wave corresponding to a pixel.
We will have to anticipate the range of frequencies that humans can hear.
* Func3 => Combine the waves corresponding to all pixels in a row.
* Func4 => Combine all rows into one sound file.