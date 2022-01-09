# WiFi-Password-Stealer
Programi *Wifi-Password-Stealer* nuk është krijuar për të promovuar në asnjë mënyrë hakimin joetik. Ai paraqet një program për të vjedhur dhe shfaqur të gjitha fjalëkalimet e WiFi-së të cilat janë ruajtur në një kompjuter. Pas ekzekutimit të kodit të Python, këto fjalëkalime dërgohen në email-in tuaj.

**_Shembull:_**  Të imagjinojmë një situatë ku ne harrojmë fjalëkalimin e WiFi-së dhe një i afërm i yni na e kërkon atë. Atëherë e vetmja gjë që duhet të bëjmë është të ekzekutojmë kodin e Python, ose të klikojmë dy herë në main.exe (në rast se e shndërrojmë kodin e Python në një fajll të ekzekutueshëm).

* Ky program është krijuar për të ekzekutuar në një makinë Windows.
* Laptopi i synuar duhet të ketë të instaluar paraprakisht gjuhën programuese Python.

![github-small](/pictures/email.jpg)

## Instalimi
Përdorim komandat e mëposhtme për instalim:

```
pip install secure-smtplib
pip install subprocess32

```

## Përdorimi
* Plotësoni _**Emrin** nga i cili do të dërgohet email dhe **Email** se kujt do ti dërgohet_
![github-small](/pictures/emailmessage.jpg)

* Plotësoni _**Email** nga i cili do të dërgohet email dhe **Password** i account-it të email-it prej të cilit do të dërgohet_
![github-small](/pictures/emaillogin.jpg)

* Krijimi i EXE përmes komandave:

```
pip install pyinstaller
pyinstaller main.py

```
* Klikojmë dy herë në main.exe

* Në 5-10 seconda, të gjitha të fjalëkalimet dërgohen në email-in tuaj.

> Shënim: Nëse dërgohet main.exe në një kompjuter tjetër dhe ky fajll klikohet 2 herë atëherë do të arrihet vjedhja e të gjithë fjalëkalimeve të WiFi-së të ruajtur në atë kompjuter.

## Referenca

Për informacione të metutejshme në lidhje me WiFi Password Stealing duke përdorur gjuhën programuese Python atëherë [klikoni](https://www.youtube.com/watch?v=SzYKzAHsdMg&t=238s).