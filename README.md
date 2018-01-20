# Deploy-Your-Talent

This repository collects material around a workshop that a team of consultants at CA Technologies created to help students (aged around 14) get a taste of IT technology and coding. CA Technologies is running a world wide program - through which CA invests a lot time, money and other resources - to promote STEM education. We are a group of enthusiastic employees who contribute to this program, there are other CA employees who do similar things.

We use a simple IoT example, based on MicroPython, an ESP2866 Microcontroller (NodeMCU) on a breadboard, lights (NeoPixel LEDs), a temperature sensor (DS18B20) and an MQTT broker (sitting on a RaspberryPi) to show how simple students can built their own IoT application.
Here is an example of how the breadboard is to be built:

![alt text](https://github.com/Crayfish68/IoT-Workshop-for-Students-DYT-CA-Technologies/blob/master/Images/Breadboard.png)

At the end of this workshop (about 45 minutes), the students should have an understanding of what (technologies) IoT is made up of and be able to control a ring of LEDs from their phone and vice versa read/see temperature of a sensor on their phone.  The attached picture is what they will build during this workshop, we will walk them through each bit. (The presentation animates this graphic.)

![alt text](https://github.com/Crayfish68/IoT-Workshop-for-Students-DYT-CA-Technologies/blob/master/Images/IoT%20Workshop%20Overview.png)


The cost of a single workplace (per student) is around 15€. To recreate this workshop, a public MQTT broker service (such as Adafruit.io) will do, to run a class of 10 or more students, you'll need to set up your own MQTT broker (mosquitto with NodeRED) somewhere.

Feel free to us this workshop as is, improve it or send us pull requests! Contact us with any questions.

Thanks

Here is the current structure of this repository:

<pre>
.
├── fonts
│   these fonts are used in the presentation(s)
│   └── CA_Sans_FINAL
│       this is a proprietary font, please don't use without permission
│       ├── CA Sans OpenType
│       └── CA Sans TrueType
├── images
│   some images that are used in README.md's
├── presentations
│   this is the presentation we use for the walkthrough at the workshop
├── src
│   here are the scripts that we use during the workshop
└── tools
    some tools and software that is useful/needed for this workshop
    ├── ESPlorer
    │   a good IDE for the ESP controllers, allows a more comfortable way of coding
    │   ├── lib
    │   ├── _lua
    │   └── _micropython
    ├── mac
    │   ├── additional stuff
    │   ├── java
    │   └── USB driver
    ├── MicroPython
    │   here are MicroPython firmwares stored
    └── Windows
        │ in Windows, you might need to install these drivers for the boards to be recognised
        ├── CP210x_Windows_Drivers
        │   ├── x64
        │   └── x86
        ├── Java
        │   Coffee!
        └── NodeMCU Flasher
            │ in Windows use this tool to flash the ESP8266 boards
            └── Config

</pre>
