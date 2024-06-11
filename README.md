# Engeto-Election-Scraper

Zdravím mého kontrolora!
Vím, že jsem dosti ve skluzu,ale jsem už zničená a zmatená, takže posílám to, co mám ať dostanu nějakou radu. Díky moc. Přikládám i hlašení chyb.
S pozdravem
Veronika



Election Scraper 3rd Engeto project


Description

This programm is able to collect election data from Czech Republic from 2017 from https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ


Installation of libraries

You can find all necessary libraries in file requirements.txt


Running the programm

You will need two arguments to run the programm. 
1st argument is URL that you will choose and enter. You can find it under "X" in column "Výběr obce".
2nd argument is name of exported csv file.


Example

You will choose Litoměřice. 
1st argument will be URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203 . 
2nd argument is name of future csv file: results_litomerice

python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203" "results_litomerice.csv"
