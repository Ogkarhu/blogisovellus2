# blogisovellus2
Linkkienjakosovellus kommenttikentillä ja vuorovaikutteisuudella käyttäjien kanssa 

Blogisovellus johon pääkäyttäjä voi lisätä  videoita (youtube) saatetekstillä ja muut käyttäjät pystyvät kirjautuneina käymään keskustelua jaetuista videoista. Konseptissa on keskiössä sisällönkuratointi ja sitä kautta mielenkiintoisen sisällön löytäminen.

Sovellus pitää kirjaa käyttäjien tykkäyksistä, kommenteista ja niiden järjestyksestä. Käyttäjä voi kirjautua käyttäjätunnuksella ja salasanalla.

Käyttö:
- Luo uusi käyttäjä
    - vain adminit voivat lisätä videoita, joten luo ainakin yhdet admin-tunnukset.
- Kirjaudu sisään luomillasi tunnuksilla
- Siirry sivulle "lisää video"
- linkki-kenttään voi laittaa youtube-videon lähes missä tahansa muodossa.
    - "kommentti"-kenttään voi kertoa lisäämästään videosta lisää
- lisätty video ilmestyy kaikkien käyttäjien etusivuille
- jos haluat seurata tiettyä käyttäjää, siirry käyttäjät sivulle.
    -siellä voit painaa "seuraa-käyttäjää" jos haluat nähdä käyttäjän lisäämiä videoita omassa syötteessäsi ja vastaavasti "lopeta seuraaminen" jos et enää halua.
- Seuraamasi videot näkyvät "oma syöte" sivulla
- Voit kommentoida omia tai muiden lisäämiä videoita videokohtaisten kommenttikenttien kautta.

Testausohjeet

- Aluksi kloonaa repositorio 
```
git clone https://github.com/Ogkarhu/blogisovellus2.git
```
- Avaa kohdekansio (cd)
- Testataksesi sovellusta sinun täytyy asentaa esivaatimukset 
```
pip install -r requirements.txt
```
- Rakenna virtuaaliympäristö 
```
python3 -m venv venv
```
- Avaa virtuaaliympäristö 
```
source venv/bin/activate
```
- Avaa tietokanta uuteen terminaali-ikkunaan 
```
Start-pg.sh
```
- Luo tietokanta ajamalla uudessa terminaali-ikkunassa 
```
schema.sql psql < schema.sql
```
- Käynnistä uuteen ikkunaan paikallinen sovellus 
```
flask run --debug
```
- Voit avata sivuston selaimessa http://localhost:5000/
