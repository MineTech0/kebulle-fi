# kebulle.fi

Paikka johon menet, kun haluat löytää parhaimman kebulan suomesta. Oikeiden ihmisten mielipiteen mukaan.

Toteutettu Helsingin Yliopiston kurssilla [Tietokantasovellus](https://studies.helsinki.fi/opintotarjonta/cu/hy-CU-118025659-2021-08-01/TKT20011/Aineopintojen_harjoitusty%C3%B6_Tietokantasovellus)

## Ominaisuudet

- [x] Kebab ravintoloiden arvostelu
- [x] Kebab ravintoloiden lisääminen
- [x] Ravintoloiden kommentointi
- [x] Kebabilat lueteltu alueellisesti
- [x] Suosituimman ravintolan äänestäminen
- [x] Suomen laajuinen ravintola leaderboard

## Käynnistys

Kopioi .env.example tiedosto .env tiedostoksi ja täytä tarvittavat tiedot.

### Asenna riippuvuudet 

``python3 -m venv venv``

``source venv/bin/activate``

``pip install -r requirements.txt``

Alusta tietokanta

``psql < schema.sql``

### Käynnistä sovellus

``flask --app src/app run``



