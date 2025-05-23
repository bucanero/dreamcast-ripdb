# Soul Calibur - PAL - working

## Rip Details

- **User:** Eleven of 9
- **Date:** 2001-07-22 12:33:41
- **Status:** Selfboots on a 74 minute cdr. In-game background music plays perfectly.

## Downsampling

Delete all files that end L.P16

## Bin Hacking

Hex edit 1st_read.bin, change all instances of L.P16 to R.P16<br />Hack3 1st_read.bin <2nd msinfo#><br />Binhack 1st_read.bin ip.bin <2nd msinfo#><br /><br />Here is the SORTTXT.TXT file (with all L.P16 files removed & dummy file added):<br /><br />data/000dummy.dat 1<br />data/1ST_READ.BIN 2<br />data/HUMAN.DAT 3<br />data/STAGE.DAT 4<br />data/GBGM0DR.P04 5<br />data/GBGM0DL.P04 6<br />data/HOPEN.DAT 7<br />data/GBGM0CR.P04 8<br />data/GBGM0CL.P04 9<br />data/GBGM0BR.P04 10<br />data/GBGM0BL.P04 11<br />data/VCSEL.DAT 12<br />data/ENBU.DAT 13<br />data/CDATA.DAT 14<br />data/CINIT.DAT 15<br />data/KMISSION.DAT 16<br />data/GBGM0FR.P16 17<br />data/KGALLERY.DAT 18<br />data/GBGM0FR.P08 19<br />data/KENDING.DAT 20<br />data/SBGM10R.P16 21<br />data/SBGM0FR.P16 22<br />data/SBGM0ER.P16 23<br />data/SBGM0DR.P16 24<br />data/SBGM0CR.P16 25<br />data/SBGM0BR.P16 26<br />data/SBGM0AR.P16 27<br />data/SBGM09R.P16 28<br />data/SBGM08R.P16 29<br />data/SBGM07R.P16 30<br />data/SBGM06R.P16 31<br />data/SBGM05R.P16 32<br />data/SBGM04R.P16 33<br />data/SBGM03R.P16 34<br />data/SBGM02R.P16 35<br />data/SBGM01R.P16 36<br />data/GBGM15R.P16 37<br />data/GBGM14R.P16 38<br />data/GBGM13R.P16 39<br />data/GBGM12R.P16 40<br />data/GBGM11R.P16 41<br />data/GBGM10R.P16 42<br />data/GBGM0ER.P16 43<br />data/GBGM0AR.P16 44<br />data/GBGM09R.P16 45<br />data/GBGM08R.P16 46<br />data/GBGM07R.P16 47<br />data/GBGM06R.P16 48<br />data/GBGM05R.P16 49<br />data/GBGM04R.P16 50<br />data/GBGM03R.P16 51<br />data/GBGM02R.P16 52<br />data/GBGM01R.P16 53<br />data/0GDTEX.PVR 54

## Comments

You must add a 145MB dummy file (called 000Dummy.dat) to the 2nd session to decrease loading times, and also burn in the original file order.

