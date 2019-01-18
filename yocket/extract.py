import requests
import re
from bs4 import BeautifulSoup

r = requests.get('https://yocket.in/universities/all/masters-in-computer-science-engineering',
             auth=('mukundwagh@gmail.com','mukund@123'))
#print r.text

soup_page = BeautifulSoup(r.text,'html.parser')
container_page=soup_page.find_all('div',attrs={'class':'container'})
page_number = 1
for cont_page in container_page:
    univ_list_page = cont_page.find('div',{'id':'university_list'})
    if univ_list_page is not None:
        pages=univ_list_page.find('p')
        page_number=int(re.findall('\d+',pages.text)[2])


for pn in range(1,page_number):
    r = requests.get('https://yocket.in/universities/masters-in-computer-science-engineering',
                     auth=('mukundwagh@gmail.com', 'mukund@123'),params={'page' : pn})
    # print r.text

    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find_all('div', attrs={'class': 'container'})

    for cont in container:
        univ_list = cont.find('div', {'id': 'university_list'})
        if univ_list is not None:
            univ = univ_list.find_all('div', {'class': 'col-sm-10'})
            for u in univ:
                tag = u.find('a').text
                link = 'https://yocket.in'+ u.find('a').get('href')
                print link," : "+tag,": ",
                location = u.find('small').text
                print location,
                univ=requests.get(link)
                soup_univ = BeautifulSoup(univ.text,'html.parser')
                container_univ = soup_univ.find_all('span', {'class': 'label-round bg-success'})
                print " : "+container_univ[0].text

