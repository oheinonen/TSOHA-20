# Tietokantasovellus 2020 - Ravintolan työvuorolista
Tämä repositorio on tarkoitettu [AINEOPINTOJEN HARJOITUSTYÖ: TIETOKANTASOVELLUS-kurssin](https://courses.helsinki.fi/fi/tkt20011) suorittamiseksi. 

Sovelluksen tarkoituksena on toimia työkaluna, jolla luodaan työvuorolista ravintolan työntekijöille. Käyttäjän tulee lisätä sovellukseen ravintolan henkilöstö. Ravintolan henkilöstö jakautuu tässä sovelluksessa seuraaviin luokkiin; leipuri, kokki, tarjoilija, kassahenkilö, tiskari. Yksi työntekijä voi kuulua useaan luokkaan, ts. suorittaa eri tehtäviä eri aikoina. Käyttäjä voi lisätä ravintolalle työvuoroja, jotka voi suorittaa tiettyyn luokkaan kuuluva työntekijä. Toistuvia työvuoroja voi lisätä samalla kertaa joko viikottain toistuvaksi tai päivittäin toistuvaksi. 

Kullakin työntekijällä on tietty maksimiviikkotuntimäärä, jota enempää tunteja järjestelmä ei saa työntekijälle antaa. Lisäksi työntekijälle voidaan merkitä lomapäiviä, joihin järjestelmä ei saa antaa kyseiselle työntekijälle työvuoroja. 

Järjestelmä luo työvuoroista henkilöstövahvuuskalenterin, joka näyttää tarvittavien työntekijöiden määrän luokittain eri päivinä. Järjestelmä luo annetuista työvuorosta sekä ravintolan työntekijöistä työvuorolistan, jossa jokainen ravintolan työvuoro asetetaan jollekin työntekijälle ja jossa kenenkään työntekijän viikkotunnit eivät ylity ja lomapäivät säilyvät. 

#### Tällä hetkellä käytössä olevat toiminnot

[Sovellusta pääsee testaamaan täältä](https://tsoha-rostermaker.herokuapp.com)

+ Käyttäjä voi rekisteröityä sekä kirjautua sovellukseen
+ Käyttäjä voi luoda ravintolan omalle käyttäjälleen
+ Käyttäjä voi lisätä ravintolalleen työntekijöitä ( voi olla vain yksi rooli tällä hetkellä)
+ Käyttäjä voi lisätä ravintolalleen työvuoroja. Yhdellä kerralla voi lisätä vuoron joko joka päivälle toistuvaksi tai kerran viikossa toistuvaksi
+ Käyttäjä voi myös muokata/poistaa edellä mainittuja
+ Käyttäjä voi listata viikottaisen henkilöstövahvuuskalenterin 
+ Käyttäjä voi listata työvuorolistan (ominaisuus vielä keskeneräinen eikä juurikaan testattu, mutta pitäisi toimia käyttäjän oikeilla syötteillä)  
+ Työntekijöille ei vielä voi antaa vapaapäiviä 
+ Työntekijäkohtaista raportointia ei vielä implementoitu


#### Lopullisen version suunnitellut toiminnot:

+ Kirjautuminen
+ Työntekijöiden lisääminen, muokkaaminen ja poistaminen
+ Työvuorojen lisääminen, muokkaaminen ja poistaminen
+ Henkilöstövahvuuskalenterin teko
+ Työvuorolistan teko (ja muutos)
+ Henkilökohtaisen työvuorolistan listaus
+ Työvuorolistan listaus
+ Työntekijäkohtainen työraportti (tehdyt tunnit tietyllä aikavälillä)
+ Työntekijän tekemien tuntien listaus kiireellisyysluokittain
+ Työvuorolistan ylimiehityksen raportointi
