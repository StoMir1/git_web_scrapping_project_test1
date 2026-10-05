from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

latest_news = soup.find('div', attrs={'class':'medium-widget blog-widget'})

#print('len latest news', len(latest_news))
#print(latest_news)

titles = latest_news.find_all('a')
times = latest_news.find_all('time')

# print(title)

# for item in titles:
#     print(item.get_text())
#     print(item.get('href'))
#     print('-'*30)

# for item in times:
#     print(item.get_text())
#     print('-'*30)

# ------------------------------------------------------------------------------------------

# upcoming_events = soup.find('div', attrs={'class':'medium-widget event-widget last'})

# event_titles = upcoming_events.find_all('a')
# event_times = upcoming_events.find_all('time')


# for item in event_titles:
#     print(item.get_text())
#     print(item.get('href'))
#     print('-'*30)

# for item in event_times:
#     print(item.get_text())
#     print('-'*30)


# -----------------------------------------------------------------------------------------------
# use_python_for = soup.find('div', attrs={'class':'medium-widget applications-widget last'})

# lists = use_python_for.find_all('li')
# inside = use_python_for.find_all('a')

# for item in lists:
#     print(item.get_text())
#     print(item.get('href'))
#     print('-'*30)

titles = soup.select('div.medium-widget.event-widget.last ul.menu li a')

for item in titles:
    print(item.get_text())