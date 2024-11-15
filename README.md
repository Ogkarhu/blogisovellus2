# blogisovellus2
Linkkienjakosovellus kommenttikentillä ja vuorovaikutteisuudella käyttäjän kanssa 

Blogisovellus johon pääkäyttäjä voi lisätä (muiden alustojen) videoita saatetekstillä ja muut käyttäjät pystyvät kirjautuneina käymään keskustelua jaetuista. Konseptissa on keskiössä sisällönkuratointi ja sitä kautta mielenkiintoisen sisällön löytäminen.

Yksinkertainen malli Yksi kuraattori, muut käyttäjät voivat kommentoida

Monimutkainen malli Useita kuraattoreja, käyttäjät voivat valita keitä seuraavat

Molemmissa malleissa sovellus pitää kirjaa käyttäjien tykkäyksistä, kommenteista ja niiden järjestyksestä. Käyttäjä voi kirjautua joko käyttäjätunnuksella tai sähköpostiosoitteella ja salasanalla.

Testausohjeet



    Aluksi kloonaa repositorio ```git clone https://github.com/Ogkarhu/blogisovellus2.git```

    Avaa kohdekansio (cd)

    Testataksesi sovellusta sinun täytyy asentaa esivaatimukset ```pip install -r requirements.txt```

    Rakenna virtuaaliympäristö ```python3 -m venv venv```

    Avaa virtuaaliympäristö ```source venv/bin/activate```

    Avaa tietokanta uuteen terminaali-ikkunaan ```Start-pg.sh```

    Luo tietokanta ajamalla uudessa terminaali-ikkunassa ```schema.sql psql < schema.sql```

    Käynnistä uuteen ikkunaan paikallinen sovellus ```flask run --debug```

    Voit avata sivuston selaimessa http://localhost:5000/
