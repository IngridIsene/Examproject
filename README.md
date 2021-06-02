# Examproject
# Booking side av sommerutstyr

Det er lagt til en bruker til sensor i databasen som kan brukes hvis ønskelig:
Brukernavn: Sensor 
Passord: Sommer2021! 

Fra før er det lagt til data i database filen schema.sql. Schema.sql inneholder tre tables:
1. users --> som inneholder alle registrerte brukere
2. products --> Som inneholder alle annonser / utstyr som har blitt opprettet 
3. bookings  -->  som inneholder hvem som har booket hvilket utstyr

Det har blitt brukt VUE version 3 i dette prosjektet.
Det har blitt brukt bootstrap 5 til å bygge opp applikasjonen --> https://getbootstrap.com/docs/5.0/getting-started/introduction/ 
Bootstrap er brukt til blant annet login form, registration form, booking cards, create add, your ads, your bookings og booking side.  




________________________________________________________________________________________________________________________________________

## Hvordan kjøre applikasjonen? 

- Selve prosjektet ligger i Examproject mappen.

- skriv command: ls i terminalvindu 

- Det vil da komme opp booking som et alternativ --> kjør da commanden "cd booking"

- Når man er inne i booking filen --> kjør command npm run serve (Da starter frontend) 

- Åpne en ny terminal og skriv igjen ls 

- Det vil da komme opp backend som et alternativ --> kjørt da commanden "cd backend" 

- Aktiver venv ved command: source venv/bin/activate (PÅ MAC)

- Når man er inne i backend filen --> kjør command "python3 booking.py" (Da starter backend)


________________________________________________________________________________________________________________________________________

# FUNKSJONALITET 

## Logg inn / Registrer ny bruker

- Det er mulighet for å registrere ny bruker ved å trykke på "register" i navbaren oppe i venstre hjørne 

- For å registrere en ny bruker må alle input feltene registreres, hvis man forsøker å hoppe over noen av feltene vil meldingen "vennligst fyll ut dette feltet vises"

- Både username og email må være unique, dvs at det ikke kan ligge registrert i databasen fra før. Dersom en ny bruker prøver å registrere seg med et brukernavn eller epost som allerede er i bruk vises meldingen "Username/Email Taken! Register again" 

-  Passordet kreves en lengde på minst 7 characters og det kreves et spesialtegn, hvis dette ikke oppfylles vil en melding vises. 

- Når det har blitt registrert en bruker vil brukeren få mulighet til å logge inn ved å trykke på log in i navbaren. Her logges det inn med brukernavn og passord. Hvis brukernavn og passord ikke matches kommer det følgende melding opp: "Username or password incorrect, Try again!" 


## Home (Bruker ikke logget inn) 

- Det er mulighet for å se produktene/utstyret som kan bookes uten å logge inn. 

- Knappen viser "Book" dersom utstyret ikke er booket av en annen bruker eller "Not Available" dersom utstyret er booket av en annen bruker.

- Dersom man ikke er logget inn og trykker på "Book" vil man bli sendt til "log in" siden.

- Brukeren kan velge å sortere utstyret basert på: Price "low til high" eller "high til low" og "Oldest to newest Ads" eller "Newest to Oldest Ads". By default vises "Newest to oldest" på homepage når bruker ikke er logget inn. 

- Utstyres vises by default i "Grid", men brukeren kan trykke på knappen "Display as" og velge "list" som et alternativ, da vil en og en annonse legge seg under hverandre. Ved å velge mellom Grid og List kan brukeren endre displayet. 

- Det er lagt til et søkefelt som gjør det mulig å søke etter utstyr basert på NAVN. 


## Home (Bruker logget inn) 

- Brukeren vil ha den samme funksjonaliteten når han/hun har logget inn. Men følgende funksjonalitet er også lagt til: 

- Preferert sortering blir lagret, dvs at hvis brukeren velger å eksempel se utstyret basert på Price "Low til High" vil dette lagres slik at neste gang brukeren logger inn vil den valgte preferansen vises. Dette blir lagret i databasen knyttet til "username" og OPPDATERES når brukeren velger en annen måte å sortere annonsene/ustryret på. 

- Det er også lagt til en ekstra knapp som viser "Your ad" under utstyret som du selv har lagt, dvs at det IKKE er mulig å booke egne annonser. 

- Når brukeren er logget inn vil et til alternativ bli lagt inn i navmaren som heter PROFILE. 

## Profile 

- Brukerens brukerinformasjon er lagret og vil vises under "Profile information"

- "Your bookings" viser oversikt over utstyret brukeren har booket. Her vises booking id, produkt id, produkt navn og til/fra dato utstyret er booket. 

- "Your Ads" viser oversikt over egne annonser. Det er lagt til en knapp i denne tabellen "X" som gjør det mulig for brukeren å SLETTE egne annonser (Må være innloget for dette og det er kun mulig å slette egne annonser). Dersom en annonse slettes forsvinner den fra forsiden, MEN den vil ikke slettes fra "Your Ads" dersom en annen bruker har booket utstyret. 

- Brukeren kan laste opp egne annonser under "Create an Ad". Her fylles "Product name", "Price", "Dato til og fra" og "Description" ut. Det er også mulig å velge default bilder til annonsen i en dropdown meny. Når en annonse er opprettet blir den lagt til på forsiden og i "Your Ads" tabellen.

- Det er KUN mulig å velge dato fra dagens dato og fremover når en annonse opprettes, så hvis man velger fra-dato: "04.06.2021" så kan til-dato IKKE være "01.06.2021" den MÅ være frem i tid. 

##  Book 
- Hvis utstyret er ledig vil en "Book" knapp vises under annonsen. Hvis man trykker på "Book" knappen vil man komme til en ny side som viser bilde av utstyret, pris, beskrivelse og availability.

- Her velges perioden (til og fra dato) og det er KUN mulig å velge dato fra når utstyret er ledig. 

- Brukeren MÅ velge dato for booking og vil ikke kunne gå videre uten å velge dato

- Når utstyret bookes OPPDATERES knappen fra "Book" til "Not avilable" på fremsiden. Den blir også lagt til i "Your bookings" på profilen. 

- På profilen vil det vises oversikt over egne bookinger, det er også lagt til en knapp som gjør det mulig å slette bookinger. Da vil den fjernes fra "your bookings" og annonsen vil legges til på forsiden igjen med knapp "Book". 


## LAYOUT

- Det er lagt inn forside bilde på forsiden 

- Det er lagt til en footer på forsiden 

- Applikasjonen fungerer på mobilskjermer på 375px 

