# Käyttötapaukset

Sovelluksen käyttö tapahtuu yläpalkissa olevien nimettyjen linkkien avulla ja tutkittavalla sivulla aukeavien toiminnallisuuksien kautta. 
Alla on kuvattu reitit tällä hetkellä toteutettujen toiminnallisuuksien suorittamiseen.

## Etusivu

Listaa aktiiviset kirjoitukset SQL kyselyllä:
```
text("SELECT Account.id, Article.postname FROM Account"
                    " INNER JOIN Article ON Article.account_id = Account.id"
                    " WHERE (Article.active = True)")
```

## Kirjautuminen

- Rekisteröityminen: yläpalkki "Register" -> syötä vaaditut tiedot -> paina "Register" -> ohjaa Sisäänkirjautumiseen.

- Sisäänkirjautuminen: yläpalkki "Login" -> syötä vaaditut tiedot -> paina "Login" -> ohjaa etusivulle. 

- Uloskirjautuminen: (sisäänkirjautuneena) yläpalkki "Log out" -> ohjaa etusivulle

## Kirjoitukset

- Uusi kirjoitus: yläpalkki "Add a post" -> Anna nimi, päätä onko viesti aktiivinen, kirjoita teksti. -> paina "Add a new post" 
                                      -> ohjaa "artikkelien" listaan

- Näytä kirjoitukset: yläpalkki "List posts" -> ohjaa "artikkelien" listaan

* Avaa kirjoitus: Paina "artikkelien" listassa "View post"
  * Hakee kirjoitukseen liittyvät vastineet ja listaa ne kirjoituksen alapuolelle SQL kyselyllä:
```
text("SELECT Account.id, Account.username, Response.id, Response.text, Response.date_created FROM Response"
                      " LEFT JOIN Article ON Article.id = Response.article_id"
                      " LEFT JOIN Account ON Account.id = Response.account_id"
                      " WHERE Article.id = :article_id"
                      " ORDER BY  Response.date_created ASC").params(article_id=article_id)
```

- Lisää vastine: Avattuasi kirjoituksen paina "Add a response" -> Kirjoita haluamasi teksti -> paina "Add a new response" 
  -> ohjaa vastineeseen liittyvään kirjoitukseen 

- (admin)Kirjoitusten poistaminen: Paina "Delete" "artikkelien" listassa

- (admin)Kirjoitusten aktiivisuuden muuttaminen: Paina "Change activity" "artikkelien" listassa



## Ryhmät

- Luominen: yläpalkki "Create a group" -> syötä tiedot -> paina "Create a new group" -> ohjaa etusivulle
- Liittyminen: yläpalkki "Join a group" -> liittyäksesi paina Join group
