 # RPI Level Shifter Hat
An open source Raspberry Pi Hat for bidirectional 3V3 to 5V level shifting

*Attention:* Pull GPIO 26 high after boot in order to activate the board. This prevents uncontrolled behaviour during boot up.

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_00/F010_rpi_logic_level_shifter_hat_kicad_iso.jpg?raw=true"
height="200" border="0" /></a>
<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_00/F010_rpi_logic_level_shifter_hat_kicad_top.jpg?raw=true"
height="200" border="0" /></a> 


## Features
- compatible to Raspberry Pi 2/3/4
- Bidirectional level shifting for all GPIOs
- Enable level shifter with RPI Pin 37 (GPIO Pin 26) 
- Optional 5V power in / out
- Optional Raspberry GPIO extension Header
- TXB0108 TI level shifter ICs ([Datasheet](https://www.ti.com/lit/ds/symlink/txb0108.pdf?ts=1597483061918&ref_url=https%253A%252F%252Fwww.google.com%252F))
- 50mA continuous output current 
- Enable indicator Led
- Power indicator Led

## Get PCB kits here:
https://www.ebay.de/itm/254674762451 -> CURRENTLY SOLD OUT

https://www.tindie.com/products/chris_wag/rpi-level-shifter-hat/

Unfortunately the first batch of kits is nearly sold out.
I will restock the components shortly. Watch this space! 
Meanwhile feel free to source the PCB and Hardware yourself. 
Design files are available under *PCB* and *BOM*.

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

<a target="_blank"><img src="https://github.com/ChrisWag91/rpi_level_shifter_hat/blob/master/Graphics/Rev_00/F010_rpi_logic_level_shifter_hat_photo.JPG?raw=true"
height="200" border="0" /></a> 

## Versions
### rev_00
- initial release

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
