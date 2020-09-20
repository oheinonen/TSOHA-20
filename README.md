# Tietokantasovellus 2020 - Ravintolan työvuorolista
Tämä repositorio on tarkoitettu [AINEOPINTOJEN HARJOITUSTYÖ: TIETOKANTASOVELLUS-kurssin](https://courses.helsinki.fi/fi/tkt20011) suorittamiseksi. 

Sovelluksen tarkoituksena on toimia työkaluna, jolla luodaan työvuorolista ravintolan työntekijöille. Ravintolan henkilöstö jakautuu seuraaviin luokkiin; leipuri, kokki, tarjoilija, kassahenkilö, tiskari. Yksi työntekijä voi kuulua useaan luokkaan, ts. suorittaa eri tehtäviä eri aikoina. Ravintolan aukiolojen mukaiset tunnit jaetaan kiireysluokkiin. Kiireysluokille määritellään minimivahvuus kuhunkin työtehtävään, eli kuinka monta työntekijää täytyy olla töissä suorittamassa kutakin tehtävää.

Kullakin työntekijällä on tietty maksimiviikkotuntimäärä, jota enempää tunteja järjestelmä ei saa työntekijälle antaa. Lisäksi työntekijälle voidaan merkitä lomapäiviä, joihin järjestelmä ei saa antaa kyseiselle työntekijälle työvuoroja. 

Järjestelmä luo työvuorolistan, jossa tuntikohtaiset tarvittavat henkilövahvuudet täyttyvät ja jossa kenenkään työntekijän viikkotunnit eivät ylity ja lomapäivät säilyvät. 

#### Tällä hetkellä käytössä olevat toiminnot

[Sovellusta pääsee testaamaan täältä](https://tsoha-rostermaker.herokuapp.com)

+ Käyttäjä voi rekisteröityä sekä kirjautua sovellukseen
+ Käyttäjä voi luoda ravintolan ja sen aukioloajat
+ Käyttäjä voi luoda eri kiireysluokkia ravintolalleen


#### Toimintoja:

+ Kirjautuminen
+ Kiireellisyysluokkien teko (ja muutos)
+ Henkilöstövahvuuskalenterin teko (ja muutos)
+ Työvuorolistan teko (ja muutos)
+ Henkilökohtaisen työvuorolistan listaus
+ Työvuorolistan listaus
+ Työntekijäkohtainen työraportti (tehdyt tunnit tietyllä aikavälillä)
+ Työntekijän tekemien tuntien listaus kiireellisyysluokittain
+ Työvuorolistan ylimiehityksen raportointi
