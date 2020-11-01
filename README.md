 # RPI Level Shifter Hat
An open source Raspberry Pi Hat for bidirectional 3V3 to 5V level shifting

This device is intended to allow communication between a Raspberry Pi and a 5V microcontroller such as an Arduino.

Example:

**RASPBERRY Pi** <==3V3 Signal==> **RPI Level Shifter Hat** <==5V Signal==> **Arduino**

*Attention:* Pull GPIO 26 high after boot in order to activate the board. This prevents uncontrolled behaviour during boot up.

*Attention:* Make sure to check the steps given under *Usage & Setup*

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_02/F010_rpi_logic_level_shifter_hat_kicad_iso.jpg?raw=true"
height="200" border="0" /></a>
<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_02/F010_rpi_logic_level_shifter_hat_kicad_top.jpg?raw=true"
height="200" border="0" /></a> 

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_02/F010_rpi_logic_level_shifter_hat_photo_iso.jpg?raw=true"
height="200" border="0" /></a> 

## Features
- compatible with Raspberry Pi 2/3/4 (rev_00 and rev_02)
- compatible with Raspberry Pi Zero / Zero W (rev_02 only) 
- Bidirectional level shifting for all GPIOs
- Enable level shifter with RPI Pin 37 (GPIO Pin 26) 
- Optional 5V power in / out
- Optional Raspberry GPIO extension Header
- TXB0108 TI level shifter ICs ([Datasheet](https://www.ti.com/lit/ds/symlink/txb0108.pdf?ts=1597483061918&ref_url=https%253A%252F%252Fwww.google.com%252F))
- Enable indicator Led
- Power indicator Led
- Optional external enable (rev_02 only)

## Get PCB kits here:
https://www.ebay.de/itm/254674762451 -> CURRENTLY SOLD OUT

https://www.tindie.com/products/chris_wag/rpi-level-shifter-hat/

Unfortunately the first batch of kits is nearly sold out.
I will restock the components shortly. Watch this space! 
Meanwhile feel free to source the PCB and Hardware yourself. 
Design files are available under *PCB* and *BOM*.

https://www.tindie.com/products/chris_wag/rpi-level-shifter-hat/

## Mounting Hardware
- 1pcs  40 Pin Header Female (20x2 Pins)
- 1pcs  40 Pin Header Male (20x2 Pins) (optionally 0 or 2)
- 1pcs  screw Terminal P= 5mm (optional)
- 4pcs  M2.5 x 12mm Standoffs
- 4pcs  M2.5 x 5mm Screws

## Usage
1. Solder your Pin Headers as you need them. Make sure to mount the female header for the **Raspberry on the 3V3 side on the bottom of the PCB**. See the picture below. If you want to use 3V3 signals from the Raspberry directly also solder male headers to the footprint maked *RPI GPIO Extension*.
2. Optionally wire a 5V power supply in. This will be used to power both, the Raspberry Pi and the Levelshifter HAT. This should be done if you use lots of the 5V outputs with higher current draw
3. Configure your GPIOs as Input or Output as needed. See *Examples* for a python configuration sample.

Assemble as shown here:
(Make sure to connect the Raspberry to the 3V3 side)

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_00/F010_rpi_logic_level_shifter_hat_photo.JPG?raw=true"
height="200" border="0" /></a> 

## Setup
### Enable after boot and set GPIO drive strength
1. Install wiringpi on the Raspberry in order to set GPIO drive strength.
    ```console	
    sudo apt install wiringpi
    ```
    This allows us to increase the standard drive strength of the GPIOs from 8mA per IO to 12mA, 14mA or 16mA. Higher drive strength can be required to trigger the direction detection circuit on the level shifter ICs for more demanding 5V circuits.

2. Auto configure GPIO drive strength automatically after boot up.
    Therefore we add the command "gpio drive 0 6" to the autostart sequence
    ```console	
    sudo nano /etc/rc.local
    ```
    [Optional] Add the following line before "exit 0":
    ```console	
    gpio drive 0 6 &
    ```
    The value *6* in the end sets the output drive strength from the default 8mA to 14mA. This should help to reach the 5V logic level for more demanding output configurations.

3. Enable RPI Level Shifter Hat automatically after boot.
    This is done by pulling GPIO 26 high. 
    You can use *Wiringpi* or a python (see step 4) to do that.
     ```console	
    sudo nano /etc/rc.local
    ```
    Add the following line before "exit 0":
    ```console	
    gpio -g mode 26 out &
    gpio -g write 26 1 &
    ```

4. [Alternative to step 3]
    Copy the script "enable_rpi_logic_level_shifter.py" from the folder "Examples" to a local directory on your raspberry and add it to the autostart file as follows:

    ```console	
    sudo nano /etc/rc.local
    ```

    Add the following line before "exit 0":

    ```console	
    python /[insert local path to the enable script]/enable_rpi_logic_level_shifter.py &
    ```

After this setup your rc.local file should look similar to this (Content depends on your version of Raspberry OS):

```console	
   #!/bin/sh -e
    #
    # rc.local
    #
    # This script is executed at the end of each multiuser runlevel.
    # Make sure that the script will "exit 0" on success or any other
    # value on error.
    #
    # In order to enable or disable this script just change the execution
    # bits.
    #
    # By default this script does nothing.

    # Print the IP address
    _IP=$(hostname -I) || true
    if [ "$_IP" ]; then
    printf "My IP address is %s\n" "$_IP"
    fi

    gpio drive 0 6 &
    gpio -g mode 26 out &
    gpio -g write 26 1 &
    #python /home/pi/gpio_test_OUTPUT_with_Enable.py

    exit 0
```

## Versions
### rev_00
- initial release

### rev_02
- external enable pad added
- RPI Zero screw holes added
- correction & optimization of silk screen

*******************************************************************************************************************************

## Warning
This design is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. Without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## License
<a href="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png
" target="_blank"><img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.png"
width="88" height="31" border="2" /></a>


License text: 
https://creativecommons.org/licenses/by-nc/3.0/

*******************************************************************************************************************************
