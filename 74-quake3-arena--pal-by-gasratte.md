# Quake3 Arena -PAL by Gasratte

## Rip Details

- **User:** by Gasratte - go.to/selfboot
- **Date:** 2001-06-07 11:25:56
- **Status:** Boot: Quake3 Arena PAL - Selfboot

## Downsampling

Convert all trackxx.raw to trackxx.wav<br />Raw2wav *.raw<br /><br />Rename track04.wav as track01.wav,<br />Rename track05.wav as track02.wav<br />Rename track06.wav as track03.wav...<br />Move "track01.wav - track16.wav" to C:\Selfboot\Cdda<br /> <br />Burn all CDDA Track at the 1st Audio session<br />dir /b /o /s c:\selfboot\cdda\track*.wav > CDDATXT.TXT<br />cdrecord -dev=x,x,x -multi -audio -speed=x @CDDATXT.TXT

## Bin Hacking

dahack 1st_read.bin 2nd msinfo number<br />dahack Intro.bin 2nd msinfo number<br />dahack Q3_usa.bin 2nd msinfo number<br />dahack Ginxfer.bin 2nd msinfo number<br />dahack Ginreset.bin 2nd msinfo number<br />cdda 1st_read.bin<br />cdda Intro.bin<br />cdda Q3_usa.bin<br />Binhack 1st_read.bin ,ip.bin files & input 2nd msinfo number<br />

## Comments

Game Type: Katana with CDDA<br />Tracks: 16<br />BOOT.BIN : 1st_read.bin<br />Protection: Yes<br />Ripping time: 27 hours<br />O/S - Windows Settings: Win 98 SE / HyperTerm / 115200<br />GZIP Size: <br />track03.iso.gz 286Mb <br />track04.raw.gz 27.5mb<br />track05.raw.gz 25.3mb<br />track06.raw.gz 34.5mb<br />track07.raw.gz 32.4mb<br />track08.raw.gz 30.1mb<br />track09.raw.gz 28.5mb<br />track10.raw.gz 32.5mb<br />track11.raw.gz 24.6mb<br />track12.raw.gz 28.7mb<br />track13.raw.gz 31mb<br />track14.raw.gz 19.71mb<br />track15.raw.gz 20.9mb<br />track16.raw.gz 19.8mb<br />track17.raw.gz 22mb<br />track18.raw.gz 15.1mb<br />track19.raw.gz 15.2mb<br />track20.iso.gz 204.7mb start sector=430093<br />

