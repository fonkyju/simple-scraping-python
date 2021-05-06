import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
from rich import print
from rich.console import Console
from rich.table import Table

from function import extract_id, extract_published, extract_title, extract_city, extract_price, extract_url

# general parameters
mySearches      = ["informatique.html", "multimedia.html"]
announcements   = []
host            = "http://www.monsite.fr/"
directory       = "annonces/"

# extract file parameters
max_results = 2 #pagination number
columns = ["id", "publie", "titre", "ville", "prix", "url"]
sample_df = pd.DataFrame(columns = columns)


# scrapping code
# iterate on mySearches
for mySearch in mySearches:

  # generate mySearch Url
  urlToCrawl = host+directory+mySearch

  # iterate on pagination if exists
  for start in range(0, max_results, 1):
      urlToCrawlWithPagination = urlToCrawl+'?page=' + str(start)
      print("Work on : " + urlToCrawlWithPagination)

      page = requests.get(urlToCrawlWithPagination)
      time.sleep(1)  #ensuring at least 1 second between page grabs
      #soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
      soup = BeautifulSoup(page.text, "lxml")

      # get all announcements from page variable
      for div in soup.find_all(name="div", attrs={"class":"row"}):

        #creating an empty list to hold the data for each posting
        announcement = []

        #get id, published, title, city, price, url from announcement
        announcement.append(extract_id(div))
        announcement.append(str(extract_published(div)) + " jour(s)")
        announcement.append(extract_title(div))
        announcement.append(extract_city(div))
        announcement.append(str(extract_price(div)) + " €")
        announcement.append(host + extract_url(div))

        # check if announcement is already saved

        if(announcement not in announcements):
          announcements.append(announcement)


# generate csv files
if(len(announcements) > 0):
  for announcement in announcements:
    num = (len(sample_df) + 1)
    sample_df.loc[num] = announcement

  sample_df.to_csv("extract.csv", encoding="utf-8")


# Display results in console
if(len(announcements) > 0):

  table = Table()
  table.add_column("ID", justify="right", style="cyan", no_wrap=True)
  table.add_column("PUBLIE", justify="right", style="cyan", no_wrap=True)
  table.add_column("TITRE", style="magenta")
  table.add_column("VILLE", justify="left", style="green")
  table.add_column("PRIX", justify="right", style="green")
  table.add_column("URL", justify="left", style="green")

  for announcement in announcements:
    table.add_row(announcement[0], announcement[1], "[bold red]" + announcement[2] + "[/]", announcement[3], announcement[4], announcement[5])

  console = Console()
  console.print(table)
