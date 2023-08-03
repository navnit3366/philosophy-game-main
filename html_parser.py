import urllib.request
from bs4 import BeautifulSoup

#Create a Wikipedia link out of a wikipedia page name
def translate_to_url(page):
	return ('https://en.wikipedia.org/wiki/' + urllib.parse.quote(page))

#Get the raw source code from a url
def get_html_raw_source(url):
	return urllib.request.urlopen(url).read()

#Get the first link of a wikipedia page
def get_first_link(url, page, is_page):

	#Double check if the input is a page or url
	if is_page:
		url = translate_to_url(page)

	raw_html = get_html_raw_source(url)
	parsed = BeautifulSoup(raw_html, 'html.parser')

	#Find the body div element
	body_div = parsed.find_all(id='mw-content-text')[0]
	first_link = ('','')

	#Loop through all of the p elements in that div
	for p in body_div.find_all('p'):

		#Find the first p element which is a direct child of the div
		if p.parent == body_div:
			links = p.find_all('a')

			#Find the first link
			for link in links:
				if link.parent == p:
					first_link = (link.contents[0], 'https://en.wikipedia.org' + link.get('href'))
					break
			break

	#Return the first link
	return first_link