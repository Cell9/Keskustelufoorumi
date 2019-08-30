# Installation Guide

Lyhyt ohjeistus pojektin vaatiman pythonin virtuaaliympäristön asentamiseen ja projektin käynnistämiseen


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
