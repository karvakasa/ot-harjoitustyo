# Minun OT-harjoitustyö
+ [rahastosovellus](https://github.com/karvakasa/ot-harjoitustyo/tree/master/rahastosovellus)

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/vaatimusmaarittelu.md)
+ [Työaikakirjanpito](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/tyoaikakirjanpito.md)
+ [Changelog](https://github.com/karvakasa/ot-harjoitustyo/blob/master/rahastosovellus/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
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