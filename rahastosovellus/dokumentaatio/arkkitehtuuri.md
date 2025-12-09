## Arkkitehtuurikuvaus
### Rakenne

Ohjelman rakenne noudattelee perinteistä ui, services, entities, repositories arkkitehtuuria.

```mermaid

  flowchart TD
    Ui --> Services
    Services --> Entities
    Services --> Services
    Services --> Repositories
    Repositories --> Entities

```

### Käyttöliittymä

Käyttöliittymä on vielä Index.py tasolla

### Tiedon tallennus

tiedot tallennetaan kahteen eri csv tiedostoon asiakas.csv ja asiakashistoria.csv tiedostoihin. asiakas.csv tiedostossa on tiedot nykyisistä asiakkaista ja heidän tiliensä arvosta. Asiakashistoria.csv tiedostossa on tiedot tallennettu viime vuotisista asiakkaiden tiedoista, nimestä ja tilin arvosta.


### Päätoiminnallisuudet

Osiossa sekvenssikaaviolla esitettynä tiettyjä toiminnallisuuksia

#### Asiakkaan hakeminen

Asiakkaan löytäminen toimii seuraavalla periaatteella:

```mermaid

  sequenceDiagram
    Ui->>Services: create Asiakas("ville vallaton, 100e)
    Services->>Repository: find("ville vallaton")
    Repository->>Services: 404 not found
    Services->>Repository: addcustomer(ville vallaton, 100e)
    Repository->>Services: asiakas("ville vallaton", 100e)
    Services->>Ui: "Asiakas ville vallaton on nyt lisätty, tilillä 100e
```

### Ohjelman rakenteeseen jääneet heikkoudet

Käyttöliittymä vielä tekemättä