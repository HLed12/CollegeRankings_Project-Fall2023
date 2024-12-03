from bs4 import BeautifulSoup

count = 0
with open('main.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    elements = soup.find_all('li', class_='item-list__ListItemStyled-sc-18yjqdy-1 boZDDO')
    for element in elements:
        if not element.find('aside'):
            print(element.find('h3').get_text().strip())
