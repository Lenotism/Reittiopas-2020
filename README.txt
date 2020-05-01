TYÖN TARKOITUS

Tämä työ on toteutettu vastauksena Solidabiksen kevään 2020 koodaushaasteeseen. Tavoitteena oli luoda reittihaku-sovellus, joka laskee lyhyimmän reitin, käyttäen ainoastaan bussilinjoja. Tehtävässä oli määritelty erikseen pisteiden väliset matka-ajat ja bussien reitit.


RATKAISU

Tehtävän ratkaisussa olen olettanut, että optimaalinen kulkureitti vaatii enintään kahta vaihtoa bussista toiseen. Tehtävää pitäisi pystyä laajentamaan lisäpysäkkien ja lisälinjojen avulla ja antamaan silti optimaalisen reitin, kunhan kyseinen oletus toteutuu.

Ratkaisu perustuu kiinnittämällä ensin bussista toiseen tarvittava vaihtojen lukumäärä. Optimireitit lasketaan erikseen tilanteissa, jossa bussilinjaa vaihdetaan kaksi kertaa, kerran tai ei ollenkaa. Tämän jälkeen näistä ratkaisuista valitaan paras. Laskuri tallentaa myös kaikki yhtä hyvät reitit. Tällöin, jos saman matkan voi kulkea yhtä nopeasti samassa ajassa, käyttäjä saa tiedot kaikista reittivaihtoehdoista, joiden matka-aika on sama.

count_distance() laskee matka-aja, kun käytetään ainoastaan yhtä linjaa.

count_distance_two() laskee matka-ajan, kun käytetään kahta eri linjaa. Laskee etäisyyden A->B menetelmällä (A+I)+(I+B), jossa I on vaihtopiste. Käyttää funktiota "count_distance".

count_distance_three() laskee matka-ajan seuraavasti: Ensin, se huomioi, mitä bussilinjoja käyttämällä voi lähteä liikkeelle. Se valitsee linjan ja käy läpi jokaisen pisteen, jossa linjaa voidaan vaihtaa. Kun päästään linjanvaihtopisteeseen, ongelma rajoittuu "kahden linjan ongelmaksi" ja voidaan käyttää funktiota "count_distance_two".

Main funktio vertaa mikä tulos näiden kolmen funktion lopputuloksista on paras ja palauttaa kaikki reitit jotka antavat parhaan tuloksen. Main funktio ottaa parametreikseen alku ja loppupisteen, jotka käyttäjä syöttää nettisivulla.

 
Työ sisältää seuraavat tiedostot:

Bussi2.py
index.html
result.html
base.html

Käyttöjärjestelmäni oli Windows 10 ja käytin Visual Studio Codea koodin kirjoittamisessa. 
Optimireitin laskemisessa on käytetty Pythonia, versio 3.7.6. Web-sivu on tehty käyttäen ainoastaan HTML:ää.
Käytössäni oli Flask ja sieltä asennettuna virtualenv käyttäen seuraavia ohjeita:

https://flask.palletsprojects.com/en/1.1.x/installation/
https://www.youtube.com/watch?v=Z1RJmh_OqeA

Käyttäessäni koodia kirjoitin (Visual Studio Code) terminaaliin seuraavat komennot:
env\Scripts\activate       Aktivoi virtuaaliympäristön

$env:FLASK_ENV = "development"
$env:FLASK_APP = "Bussi2.py"  

flask run

jonka jälkeen web-sivustolle pääsee.






ALKUPERÄINEN TEHTÄVÄNANTO:

Tehtäväsi on toteuttaa reittihaku-sovellus, joka kertoo nopeimman mahdollisen reitin kahden pisteen välillä, mikä on kuljettavissa linja-autolla. Sovelluksen tulee myös kertoa mitä linja-autoreittejä tulisi käyttää perille pääsemiseksi.

Matkustaja voi vaihtaa bussilinjaa reitin varrella, jos se on suotuisaa nopeuden kannalta. Kulkuvälineen vaihtamisesta ei tule matkustamiseen lisäaikaa. Mahdollisissa vaihdoissa voit siis olettaa, että matka jatkuu saman tien ja kulkuvälineitä ei joudu odottamaan pysäkeillä.

Tehtävän toteutusta varten saat json-muotoisen datan, josta löydät seuraavat tiedot:
-Kaikki kartassa olevat pysäkit

-Kaikki kartan pysäkkien väliset yhteydet sekä matkan kesto niiden välillä. Tiet ovat kaksisuuntaisia (eli niitä voi matkustaa molempiin suuntiin), mutta aineistossa ne esiintyvät vain toiseen suuntaan.

-Värikoodatut bussilinjastot ja niiden kulkemat pysäkkien välit kartastossa.


Lopputuloksena sinun tulee luoda web-käyttöliittymä, jossa käyttäjä voi hakea reittejä kahden pisteen välillä. Käyttöliittymästä näkee nopeimman mahdollisen reitin ja siihen käytettävät kulkuvälineet reitin varrella.

Toteutuksessa käytettävät teknologiat ovat vapaasti päätettävissäsi. Tehtävässä ei kuitenkaan saa käyttää mitään kolmannen osapuolen palvelua tai kirjastoa, mikä laskee parhaimman reitin.


#######

