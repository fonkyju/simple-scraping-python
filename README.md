![CircleCI](https://img.shields.io/circleci/build/github/fonkyju/simple-scraping-python)
[![Blog](https://img.shields.io/badge/blog-news-yellowgreen)](https://www.julienkrier.fr/articles)
[![Twitter Follow](https://img.shields.io/twitter/follow/julienkrier?style=social)](https://twitter.com/julienkrier)


# Simple Scraping Python

This project is a simple example of web scraping which allows to crawl web pages with paginations and extract data from the target site.

For the example I created my own local vhost but we can of course crawl external urls.

This program :

1. Crawl url et Scrape content
2. Generate a CSV file of the scraped content
3. Display result in console with the [Rich Library](https://github.com/willmcgugan/rich)

## Installing

This project is coded with Python@3.9.4

Install all dependencies with `pip` or your favorite PyPi package manager.

```
pip install -r requirements.txt
```


## Usage

You need to change the web site parameters

```
host            = "http://www.monsite.fr/"
directory       = "annonces/"
mySearches      = ["informatique.html", "multimedia.html"]
max_results     = 2 # default pagination number
```


After this changes, simply run the `main.py`

```
python3 main.py
```
