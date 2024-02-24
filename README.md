# Morse Code Translator 


The goal of this project was to create a device that could listen to a message in morse code and translate it into plain English for us to understand. The project consists of three main components; a script to generate the sound, interpret the sound into duration lengths, and apply the translation given the lengths. 

## Installation 
The sound sensor uses the Arduino UNO microcontroller along with a sound module to detect the volume of the incoming sounds as an analog input. Note that for morse code, only the presence or absence of the noise is required, so it is independent of pitch or volume. 

To operate, plug in the device and ensure that its inputs are outputting into the correct serial port in order for the Python script to operate the translation. The Python script should be running while the Arduino takes sound inputs and converts it into lengths. 

## Hardware Setup Photos 

![IMG_0D92022AE0AA-1](https://github.com/three-beep-one-boop/morse_code/assets/130770806/f06d32db-63fe-4c5d-8c54-0ca50140180a)
![IMG_5C61745EAE12-1](https://github.com/three-beep-one-boop/morse_code/assets/130770806/5f0f497c-d5ab-4d90-868a-0bb80822331a)

## Video Demo
[![Morse Code Demo](https://img.youtube.com/vi/RhFaCivZoM0/0.jpg)](https://www.youtube.com/watch?v=RhFaCivZoM0)
