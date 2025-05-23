# Unreal Tournament

## Rip Details

- **User:** Pug_ster
- **Date:** 2001-11-25 15:42:21
- **Status:** Game booted and background music working!  Though it was shorter though.

## Downsampling

Cut all Audio tracks to half the size...

## Bin Hacking

Used broadband adapter and it took about 35 minutes to extract 2 .iso files and 19 .raw files.  Converted all about 693 megs worth of .raw files to .wav using raw2wav.exe and shortened all audio tracks to half the size (I used soundforge 4.5c.)  The result is that I got about 400 mgs worth of audio.  Then I used Discjuggler to burn an open session of 19 audio tracks plus the 2 sec lead audio track.   Created a dummy file (dummy.dat) that is exactly 603779072 bytes large and copy /b track03.iso+dummy.dat+track23.iso data.iso.  Extract data.iso.  Dahack and cdda the following files 1st_read.bin 2_acc.bin and utdc.bin with appropriate lba number.  I don't know if it was necessary, but I also hacked to ip.bin to reflect changes in the lba number too (since the audio tracks are shortened.)

## Comments

None

