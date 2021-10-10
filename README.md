# yerkeaiym_Assignment2_python
Assignment-2 - Scraping the data from website
# Title

Assignment 2 - Scraping the date cryptocurrencies


## Installation

 requests  

```bash
pip install requests
```

beautifulSoup
```bash
pip install  beautifulsoup4
```

## Usage

```from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

## Examples
>>>from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
