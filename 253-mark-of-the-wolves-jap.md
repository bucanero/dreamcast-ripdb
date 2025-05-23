# Mark OF the Wolves JAP

## Rip Details

- **User:** ROT for GENESIA TEAM and PROGAMES.FR.ST
- **Date:** 2001-12-06 23:20:39
- **Status:** Le jeu fonctionne ? merveille, mais reste en 60 Hz. Il y a une nouvelle s&eacute;quence (inconnue) anti-60Hz pour console PAL.

## Downsampling

NIET, NONE, RIEN !!!

## Bin Hacking

Binhack on 1st_read.bin and create new IP.bin with.<br />Manuellement avec un &eacute;diteur HEX, modifier en fonction de l'offset LBA de la premi?re session (il y a une piste CDDA) les 5EB0 0000 (moi pour graveur avec normalement offset ? 11700 = 104B 0000) et 6EB0 0000 (204B 0000) mais aussi CDE4436A ? remplacer par 09000900 (un seul). Faites les recherches sur toutes l'image iso cr&eacute;&eacute; avec MKISOFS.

## Comments

Jeu KATANA avec 1 CDDA protection par 5EB0, 6EB0 et CDE4436A donc il faut obligatoirement faire le jeu en autoboot et retoucher les 5EB0 ,? la main car 3 sont dans le 1st_read.bin et 4 autres cach&eacute;s dans d'autres fichiers du jeu, 1 seul 6EB0 et 1 seul CDE4436A aussi dans  1st_read.bin.<br />

