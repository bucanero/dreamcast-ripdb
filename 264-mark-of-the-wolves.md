# Mark of the wolves

## Rip Details

- **User:** Matthias
- **Date:** 2002-01-28 23:41:57
- **Status:** <br /> Le jeu fonctionne ? merveille, mais reste en 60 Hz. Il y a une nouvelle s&eacute;quence (inconnue) anti-60Hz pour console PAL.  <br />

## Downsampling

<br /> NIET, NONE, RIEN !!!  <br /><br />

## Bin Hacking

Binhack on 1st_read.bin and create new IP.bin with.<br />Manuellement avec un &eacute;diteur HEX, modifier en fonction de l'offset LBA de la premi?re session (il y a une piste CDDA) les 5EB0 0000 (moi pour graveur avec normalement offset ? 11700 = 104B 0000) et 6EB0 0000 (204B 0000) mais aussi CDE4436A ? remplacer par 09000900 (un seul). Faites les recherches sur toutes l'image iso cr&eacute;&eacute; avec MKISOFS.

## Comments

none

