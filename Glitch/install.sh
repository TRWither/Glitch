#!/bin/bash

git clone https://github.com/TRWither/Glitch.git

cd Glitch || exit

chmod +x src/main.py

sudo cp src/main.py /usr/bin/glitch

echo "Glitch successfully installed !"
echo "Type glitch in your terminal to run it."
echo "RUNNING GLITCH WITH THIS METHOD WILL MAYBE NOT WORK, SO IF IT WON'T WORK, FOLLOW THE INSTRUCTIONS : "
echo "1. cd Glitch"
echo "2. chmod +x src/main.py"
echo "3. ./main.py OR sudo ./main.py OR sudo python3.11 src/main.py"
