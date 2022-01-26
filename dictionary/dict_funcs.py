from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup

def synonyms(term):

    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms - old code: css-1kg1yv8 eh475bn0

def antonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-1fsijta e1q3oo7j0'})
    return [span.text for span in soup.findAll('a', {'class': 'css-15bafsg eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms - old code: css-1kg1yv8 eh475bn0
