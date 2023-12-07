from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://maps.google.com/?cid=8479880076324868533"

session = HTMLSession()
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"}
response = session.get(url, headers=headers)
response.html.render()
html_content = response.html.html
soup = BeautifulSoup(html_content, 'html.parser')
main_div = soup.find('div', {'role': 'main'})

if main_div:
    company_url_element = main_div.find('a', {'data-tooltip': 'Open website'})
    company_url = company_url_element.get('href') if company_url_element else None
    
    service_element = main_div.find('div', {'class': 'lMbq3e'}).find('div', {'class': 'fontBodyMedium'})
    following_sibling = service_element.find_next_sibling('div')
    service_var = following_sibling.text
    
    print("Company URL:", company_url.split("q=")[1].split("&opi")[0])
    print("Service Variable:", service_var)