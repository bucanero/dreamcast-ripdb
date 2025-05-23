# Sonic 2

## Rip Details

- **User:** Cloud1921
- **Date:** 2001-06-22 16:41:26
- **Status:** success in only making it work with a boot disc.

## Downsampling

Downsampled all of the adx files to 11025Hz, left channel.<br />It seems that I have was not able to downsample the sfd files.

## Bin Hacking

Applied hack3 to all of the bins with lba of 0, in order to make it into a boot disc verison.<br /><br />then in 1st_read.bin, search for:<br /><br />"CDE4 436A" and change it to "0900 0900"<br /><br /><br />then, again in 1st_read.bin, search for:<br /><br />"1032 0D8B" and change it to "0800 0D8B"<br />

## Comments

Needs boot disc.

