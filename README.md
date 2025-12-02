# RahastoSovellus
+ [rahastosovellus](https://github.com/karvakasa/ot-harjoitustyo/tree/master/rahastosovellus)
rahastonhoitajan sovellus, sovelluksen avulla rahastonhoitaja voi lisätä ja poistaa asiakkaita. maksaa osittain tai kokonaan asiakkaalle. Sovellus myös laskee vuosittaisien tuoton ja ottaa rahastonhoitajan osuuden tuotoista ja kokonais rahastonkoosta vuosittain. 

## Dokumentaatio
+ [Vaatimusmäärittely](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/vaatimusmaarittelu.md)
+ [Työaikakirjanpito](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/tyoaikakirjanpito.md)
+ [Changelog](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/changelog.md)
+ [Arkkitehtuuri](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

```bash
poetry run invoke build
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

1. Käynnistä sovelluksen testit komennolla:
```bash
poetry run invoke test
```

2. luo testikattavuus raportti komennolla:
```bash
poetry run invoke coverage-report
```

3. Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```bash
poetry run invoke lint
```

4. tiedoston formatointi
```bash
poetry run invoke format
```