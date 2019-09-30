from bs4 import BeautifulSoup
import requests
import random

output = open("output.txt","w")

# --------------------------------------------
# Replace Crimsons most Read with NYT top sellers
# --------------------------------------------

output.write("-----\nReplacing the most read articles on The Crimson with the NYT best seller list\n-----\n")

crimson_link = "https://www.thecrimson.com/"
crimson_response = requests.get(crimson_link, timeout=5)
crimson_content = BeautifulSoup(crimson_response.content, "html.parser")

mostRead = crimson_content.find_all("div", attrs={"class":"article-listitem-text"})

nyt_link = "https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction/"
nyt_response = requests.get(nyt_link, timeout=5)
nyt_content = BeautifulSoup(nyt_response.content, "html.parser")

names = nyt_content.find_all("h3", attrs={"itemprop":"name"})
authors = nyt_content.find_all("p", attrs={"itemprop":"author"})

for i in range(len(mostRead)):
	output.write("a: " + mostRead[i].text.strip() + "\nb: " + names[i].text + " " + authors[i].text + "\n\n")

# --------------------------------------------
# Replace "Harvard" with "Hahvahd"
# --------------------------------------------

output.write("-----\nReplacing \"Harvard\" with \"Hahvahd\"\n-----\n")

crimson_link = "https://www.thecrimson.com/"
crimson_response = requests.get(crimson_link, timeout=5)
crimson_content = BeautifulSoup(crimson_response.content, "html.parser")

mostRead = crimson_content.find_all("div", attrs={"class":"article-listitem-text"})
titles = []
for i in mostRead:
	titles.append(i.text.strip())

for i in titles:
	output.write("a: " + i + "\nb: " + i.replace("Harvard", "Hahvahd") + "\n\n")

# --------------------------------------------
# Put random things in quotations
# --------------------------------------------

output.write("-----\nPutting Random Food Items in Quotes\n-----\n")

flyby_link = "https://www.thecrimson.com/flyby/"
flyby_response = requests.get(flyby_link, timeout=5)
flyby_content = BeautifulSoup(flyby_response.content, "html.parser")

menu = flyby_content.find("section", attrs={"class":"widget widget-primary"})
items = menu.find_all("p")

for i in items:
	words = i.text.split(" ")
	index = random.randint(0, len(words) - 1)
	words[index] = "\"" + words[index] +"\""
	newItem = ""
	for j in words:
		newItem = newItem + j + " "
	output.write("a: " + i.text + "\nb: " + newItem + "\n\n")


