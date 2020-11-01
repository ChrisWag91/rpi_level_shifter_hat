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
- TI level shifter ICs
- Enable indicator Led
- Power indicator Led
- Optional external enable (rev_02 only)

## Get PCB kits here:
https://www.ebay.de/itm/254674762451

https://www.tindie.com/products/chris_wag/rpi-level-shifter-hat/

## Mounting Hardware
- 1pcs  40 Pin Header Female (20x2 Pins)
- 1pcs  40 Pin Header Female (20x2 Pins) (Optional)
- 1pcs  screw Terminal P= 5mm (Optional)
- 4pcs  M2.5 x 12mm Standoffs
- 4pcs  M2.5 x 5mm Screws

## Usage & Setup

Assemble as shown here:
(Make sure to connect the Raspberry to the 3V3 side)

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_00/F010_rpi_logic_level_shifter_hat_photo.JPG?raw=true"
height="200" border="0" /></a> 

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
