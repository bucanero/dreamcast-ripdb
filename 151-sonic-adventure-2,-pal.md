# Sonic Adventure 2, Pal

## Rip Details

- **User:** The Gorrila
- **Date:** 2001-07-06 18:33:10
- **Status:** Success, nice selfbooter with room for a 50mb dummy

## Downsampling

Adx to mono, had to make them loopable again, took ages!!<br />SFD downsampled<br />EVENT_ADX.AFS removed, replaced with a 0mb dummy<br />Internet Option stripped, and internet bins removed (2_dp.bin, SG_DPLDR.bin and MAIGO.bin)<br />Jap text removed

## Bin Hacking

hack3 1st_read.bin<br />CDE4436A ---> 09000900<br />10320D8B ---> 08000D8B<br />

## Comments

In the 1st_read.bin, removed reference to sg_dpldr.bin (therefore the internet files could be stripped)<br />Replace the IP.bin with a homebrew IP.bin because the origional IP is protected

