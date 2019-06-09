import requests
from bs4 import BeautifulSoup

baseurl ="https://www.romaniablockchainsummit.com/speaker/"
names = ['Mihai-Alisie', 'Livio-Weng', 'MRU-PATEL', 'Armand-Domuta', 'Sergiu-Draganus', 'Aviya-Arika', 'Dr-Ian-Gauci', 'Jorge-Sebastiao', 'Nicholas-Merten', 'Allen-Wu', 'Greg-Limon', 'Andreea-Porcelli', 'Alexandru-Petrescu', 'Douglas-Anderson', 'Artem-Trofymenko',
'Antonios-Koumbarakis', 'Dave-Pulis', 'Victoria-Gago', 'Maria-Marenco', 'Tiberiu-Focica', 'Dan-Nistor', 'Paul-Coste', 'Toby-Lewis', 'Mihai-Milea', 'Teuta-Bakalli', 'Haseeb-Awan', 'Tudor-Stomff', 'Marc-Taverner', 'Pancho-Vanhees', 'Carlos-Moreira', 'Gabriel-Voicila', 'Vadim-Pushkarev', 'Roxana-Nasoi', 'Alexandru-Lupascu', 'Nicolae-Ghibu', 'Sami-Ben-Jamaa', 'Stefan-Gergely', 'avadanei-andrei', 'Toufi-Saliba', 'Sergiu-Traian-Vasilescu', 'Jean-Claude-Spillmann', 'Jason-Dearborn', 'Benjamin-Talin', 'Aaron-Payas', 'Adrian-Pop', 'Emiliyan-Enev', 'Sean-Braithwaite', 'Erhan-Korhaliller', 'Cornel-Vintila', 'Adrian-Sischin', 'Petre-Stroe', 'Vince-Meens', 'Darzan-Mihai', 'Adina-Popescu', 'Ralph-Liu', 'Pavel-Kravchenko', 'Dr-Danyal-Akarca', 'Kadar-Tamas', 'Emanuel-Clodeanu', 'Vali-Malinoiu', 'Irina-Scarlat', 'Artem-Chestnov', 'Simon-Mcdermott', 'Felix-Crisan', 'Pascal-B-van-Knijff', 'Fabio-Canesin', 'Mihaela-Ulieru', 'Vlad-Trifa', 'Ioana-Frincu', 'Soumya-Basu', 'Antonio-Eram', 'Adam-Vaziri', 'Sebastian-Cochinescu', 'Crenguta-Leaua', 'Elliott-Hall', 'Andrei-Nagy', 'Iulian-Matache', 'Fernando-Martinho', 'Matthias-Sheikh-Mende', 'Maksym-Vysochanskiy', 'Oron-Barber']

for name in names:
    speaker = baseurl + name
    page = requests.get(speaker)
    if(page.status_code == 200):
        soup = BeautifulSoup(page.content, 'html.parser')
        html = soup.findAll(class_= 'linkedin')
        a = html[1].find_all('a', href=True)
        href = a[0]['href']
        print(href)