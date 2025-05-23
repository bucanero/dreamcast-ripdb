# Dead Or Alive 2 *PAL*

## Rip Details

- **User:** IrRitaTiOn - fb2k@gmx.de
- **Date:** 2001-10-13 00:36:52
- **Status:** WORKS PERFECT!

## Downsampling

NOTHING

## Bin Hacking

- 300MB Dummy File (Name: "0.0") in the root-dir<br />- hack4 -w -0 1st_read.bin<br />- hack4 -w -3 1st_read.bin<br />- burn Audio-Track:<br />  cdrecord -dev=x,x,x -multi -audio audio.raw -speed=8<br />- create Data-Image:<br />  mkisofs -C 0,11702 -V DOA2 -l -o Data.iso [dir of DOA2]<br />- Image-hack:<br />  ipins [Enter]<br />  bootsector: ip.bin<br />  iso: data.iso<br />- burn Datatrack:<br />  cdrecord -dev=1,0,0 -xa1 data.iso -speed=8

## Comments

nothing to note - do what i said and this game will work perfectly!

