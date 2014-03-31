""" 
Käyttöjärjestelmien viikkotehtävät 1

Forkkaa kolme prosessia ja kirjoittaa niiden prosessi-id:n, 
isäprosessin id:n sekä prosessiryhmän id:n tiedostoon jonka nimi on prosessi-id.

@author Jani Anttonen
"""
import os

# Alustetaan taulu, jota käytetään datan säilyttämiseen ennen sen tallentamista tiedostoon.
pidit = []

# Löydetään nykyisen prosessin ID, jota käytetään tiedostonimessä.
tama = os.getpid()

# Tehdään kolme lapsiprosessia
for i in range(0,3):
    child_pid = os.fork()
    pidi = str(os.getpid()),str(os.getppid()),str(os.getpgrp())
    pidit.append(pidi)
	
# Formatoidaan tiedostonimi ja luodaan tiedosto.
tiedostonimi = '{0}{1}'.format(tama, '.txt')
tiedosto = open(tiedostonimi,'w')

# Kirjoitetaan tiedostoon.
for i in range(0,3):
	tiedosto.write(str(pidit[0]))
	tiedosto.write("\n")