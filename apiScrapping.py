from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

def atrrExtractor(htmlElem, inData):
    return soup.findAll(htmlElem, attrs={"class":inData})

quotes1 = atrrExtractor("span","text")
authors1 = atrrExtractor("small","author")

file = open("scrapped.quotes.csv", "w")
writer = csv.writer(file)

#writer.writerow(["Quotes", "Authors"])

#for quote, author in zip(quotes, authors):
#    print(quote.text + " - " + author.text)
#    writer.writerow([quote.text, author.text])
#file.close()

def csvCreator(inData1, inData2):
    attrs1 = atrrExtractor("span",inData1)
    attrs2 = atrrExtractor("small",inData2)
    writer.writerow([inData1, inData2])

    for attr1, attr2 in zip(attrs1, attrs2):
        print(attr1.text + " - " + attr2.text)
        writer.writerow([attr1.text, attr2.text])
    file.close()

csvCreator("text", "author")