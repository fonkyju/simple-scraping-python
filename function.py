# function.py

import regex

#####################
# extract_id function
#####################
def extract_id(div):
  try:
    target = div.find("a", attrs={"class": "title"})
    return target['id']
  except:
    return "Nothing_found"

#####################
# extract_published function
#####################
def extract_published(div):
  try:
    target = div.find("span", attrs={"class": "published"})

    today = regex.search(r"(nouveau)", target.text)
    otherday = [int(i) for i in target.text.split() if i.isdigit()]

    if(today):
      day = 0

    if(otherday):
      day = otherday[0]

    return day
  except:
    return "Nothing_found"

#####################
# extract_title function
#####################
def extract_title(div):
  try:
    target = div.find(name="a", attrs={"class":"title"})
    return target.text.strip()
  except:
    return "Nothing_found"


#####################
# extract_city function
#####################
def extract_city(div):
  try:
    target = div.find(name="div", attrs={"class":"location"})
    return target.text.strip()
  except:
    return "Nothing_found"


#####################
# extract_price function
#####################
def extract_price(div):
  try:
    target = div.find(name="span", attrs={"class":"price"})
    price = [int(i) for i in target.text.split() if i.isdigit()]
    return price[0]
  except:
    return "Nothing_found"

#####################
# extract_title function
#####################
def extract_url(div):
  try:
    target = div.find(name="a", attrs={"class":"title"})
    return target['href']
  except:
    return "Nothing_found"
