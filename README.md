# Tietokantasovellus 2020 - Ravintolan työvuorolista
Tämä repositorio on tarkoitettu [AINEOPINTOJEN HARJOITUSTYÖ: TIETOKANTASOVELLUS-kurssin](https://courses.helsinki.fi/fi/tkt20011) suorittamiseksi. 

Sovelluksen tarkoituksena on toimia työkaluna, jolla luodaan työvuorolista ravintolan työntekijöille. Käyttäjän tulee lisätä sovellukseen ravintolan henkilöstö. Ravintolan henkilöstö jakautuu tässä sovelluksessa seuraaviin luokkiin; leipuri, kokki, tarjoilija, kassahenkilö, tiskari. Käyttäjä voi lisätä ravintolalle työvuoroja, jotka voi suorittaa tiettyyn luokkaan kuuluva työntekijä. Toistuvia työvuoroja voi lisätä samalla kertaa joko viikottain toistuvaksi tai päivittäin toistuvaksi. 

Kullakin työntekijällä on tietty maksimiviikkotuntimäärä, jota enempää tunteja järjestelmä ei saa työntekijälle antaa. Lisäksi työntekijälle voidaan merkitä lomapäiviä, joihin järjestelmä ei saa antaa kyseiselle työntekijälle työvuoroja. 

Järjestelmä luo työvuoroista henkilöstövahvuuskalenterin, joka näyttää tarvittavien työntekijöiden määrän luokittain eri päivinä. Järjestelmä luo annetuista työvuorosta sekä ravintolan työntekijöistä työvuorolistan, jossa jokainen ravintolan työvuoro asetetaan jollekin työntekijälle ja jossa kenenkään työntekijän viikkotunnit eivät ylity ja lomapäivät säilyvät. Lisäksi yksittäisen työntekijän viikkotuntimäärää voidaan tarkastella.

#### Sovelluksen toiminnot

[Sovellusta pääsee testaamaan täältä](https://tsoha-rostermaker.herokuapp.com)

Käyttäjälle test (salasana test123) on luotu kolme ravintolaa, Ravintola 3:lle on luotu 25 työntekijää sekä 70 työvuoroa viikon 43 päiville. 

+ Käyttäjä voi rekisteröityä sekä kirjautua sovellukseen
+ Käyttäjä voi luoda ravintolan omalle käyttäjälleen
+ Käyttäjä voi lisätä ravintolalleen työntekijöitä 
+ Käyttäjä voi lisätä ravintolalleen työvuoroja. Yhdellä kerralla voi lisätä vuoron joko joka päivälle toistuvaksi tai kerran viikossa toistuvaksi
+ Käyttäjä voi myös muokata/poistaa edellä mainittuja
+ Käyttäjä voi listata viikottaisen henkilöstövahvuuskalenterin
+ Käyttäjä voi tehdä työvuorolistan - sovellus listaa työvuorot käyttäjän nähtäväksi
+ Työvuorolistan yhteydessä ilmoitetaan käyttämättä jääneet työtunnit sekä mahdolliset vuorot, joihin ei riittänyt työntekijöitä
+ Työntekijöille voi antaa vapaapäiviä 
+ Työntekijäkohtasen työraportin voi listata viikottaisella tarkkuudella
