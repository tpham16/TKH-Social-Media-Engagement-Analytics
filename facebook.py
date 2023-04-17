import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the website to be scraped
url = 'https://www.facebook.com/theknowledgehouse/'
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the data from the parsed HTML using CSS selectors
likes = soup.find("span",class_ ='.x1e558r4')
#comments = soup.find_all().text
#shares = soup.find_all().text
#reposts = soup.find_all().text

# Print the extracted data
print('Likes:', likes)
#print('Comments:', comments)
##print('Shares:', shares)
#print('Reposts:', reposts)