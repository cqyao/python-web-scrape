import requests
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema

print("Enter URL for article: ")

URL = input()
try:
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	# Replace with tag and class name
	article = soup.find_all('p', class_="Paragraph_wrapper__6w7GG")

	print("Enter file name to save: ")
	file_n = input() + ".txt"
	# Open file with write only access
	w_file = open(file_n, "w")
	for text in article:
		w_file.write(text.text)
		w_file.write("\n\n")
except:
	print("Error occurred. Enter valid link!")


