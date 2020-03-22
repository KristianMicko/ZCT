Toto je zadanie č. 1 zo zct a je vytvorene v docker toolbox vo Windowse.
Pre nahratie potrebných image-ov a container-ov je potrebné nastaviť viditeľnosť priečinka s hostovského počítača
podľa návodu na stránke: http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows

Aplikácia je webová. 

1. Skladá sa z backend-u, čo tvorí aplikácia flask v python-e a databázový engine bol použitý MYSQL.

2. Frontend tvoria html súbory s javascriptovým framework-om Vue.js a na zostavenie GUI bol použitý Bootstrap a knižnica jquery.
Pre aplikáciu boli použité CDN-ka pre Vue.js a jquery zároveň frontend-ova časť je hostovaná na kontajnery, ktorý poskytuje chod apache2 server-a.

Na zostavenie obrazov a kontajnerov je pripraveny subor prepare.sh ten subor zaroven spusti aj chod kontajnerov.
Pri zostavovaní kontajnerov môže vzniknúť chyba pri uvodnej konfiguracii databázy MYSQL. 
Na riešenie tohto problému je potrebné použiť tieto príkazy:

/*na zmenu adresára*/
cd databazy

/*na spustenie doplnujuceho scripty*/
./naplnenie.sh  

Pre správny chod aplikácie je potrebné, aby bežal na tejto IP:
http://192.168.99.100:8080/

Dôležité je, aby sa táto IP adresa zachovala, inak nebudú správne reagovať event-y na html stránke.

V úvode aplikácie je jednoduchá authentifikácia za pomoci prihlasovacieho formulára. 
Defaultne je nastavený login:Jozef@ss.com a heslo:tajny 

Pre vytvorenie inych pouzivatelov spustite prikaz:

docker exec -it mysql mysql

pouzite databazu zct s prikazom: use zct;

a vykonajte dopyty nad tabulkou "prihlasenie".

Zbytok aplikácie by mal sa bez problémov používať


