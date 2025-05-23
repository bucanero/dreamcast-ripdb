# Ready 2 Rumble Boxing - PAL

## Rip Details

- **User:** Eleven of 9
- **Date:** 2001-07-07 19:20:07
- **Status:** Selfboots in 60Hz (no need to search for menus for the 60Hz switch any more)

## Downsampling

None - just rename track04.wav - track06.wav to track01.wav - track03.wav

## Bin Hacking

dahack 1st_read.bin 34085<br />cdda 1st_read.bin<br /><br />Hex edit 1st_read.bin<br />change: 01 E4 03 A0 02 E4 01 A0 03<br />to:         00 E4 03 A0 00 E4 01 A0 00<br /><br />Binhack 1st_read.bin / ip.bin 34085

## Comments

Ony do the hex editing if using a PAL console & your TV can accept the 60Hz signal.

