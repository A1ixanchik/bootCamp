from bs4 import BeautifulSoup
with open('index.html', 'r') as file_html:
    content = file_html.read()
    print(content)
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())