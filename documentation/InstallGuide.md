# Installation Guide

Lyhyt ohjeistus projektin vaatiman pythonin virtuaaliympäristön asentamiseen ja projektin käynnistämiseen


- Ladataan GitHub projekti zip-tiedostona, puretaan se paikallisesti ja mennään sovelluksen juurihakemistoon

```
unzip -a file_name.zip
```
-  Luodaan virtuaalinen python ympäristö
```
python3 -m venv venv
```
-  Aktivoidaan virtuaaliympäristö
```
source venv/bin/activate
```
-  Asennetaan virtuaaliympäristöön sovelluksen käyttämät kirjastot
```
pip install -r requirements.txt
```
-  Käynnistetään sovellus
```
python3 run.py
```

# Asennus Herokuun

Lyhyt ohjeitus projektin käyttöön saamiseksi Herokussa. Oletus on, että git on asennettuna. Tarvitset Herokun käyttäjätunnukset ja Herokun työvälineet komentoriville [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

#### Asennettuasi projektin paikallisesti, luodaan Herokuun paikka sovellukselle

-  Aktivoidaan virtuaaliympäristö
```
source venv/bin/activate
```
- Luodaan sovellukselle paikka Herokuun
```
heroku create sovelluksen-nimi
```
- Nyt sovellukselle on paikka Herokussa. Lisätään paikalliseen versionhallintaan tieto Herokusta
```
git remote add heroku https://git.heroku.com/sovelluksen-nimi.git
```
- Lähetetään projekti Herokuun 
```
git add .
git commit -m "Initial commit"
git push heroku master
```
#### Luodaan Herokuun sovellusta varten tietokanta ja sen hallintaan vaaditut asetukset

- Luodaan ympäristömuuttuja
```
heroku config:set HEROKU=1
```
- Luodaan Herokuun tietokanta
```
heroku addons:add heroku-postgresql:hobby-dev
```
- Luodaan ympäristömuuttuja
```
heroku config:set HEROKU=1
```
- Luodaan lopuksi ylläpitäjän käyttäjä
```
heroku pg:psql

INSERT INTO account (name, username, email, password) VALUES ('Admin', 'admin', 'email', 'admin');
```




