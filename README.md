[![Blog](https://img.shields.io/badge/blog%20news-yellowgreen)](https://www.julienkrier.fr/)
[![Twitter Follow](https://img.shields.io/twitter/follow/julienkrier?style=social)](https://twitter.com/julienkrier)


# simple-scraping-python

This project is a simple example of web scraping which allows to crawl web pages with paginations and to extract data from the target site.

For the example I created my own local VHOST but we can of course crawl external urls.

## Installing

This project is coded with Python@3.9.4

Install all dependencies with `pip` or your favorite PyPi package manager.

```
pip install rich
```


## Usage

You need to change the web site parameters

```
host            = "http://www.monsite.fr/"
directory       = "annonces/"
mySearches      = ["informatique.html", "multimedia.html"]
max_results     = 2 # default pagination number
```


After this changes run the `main.py`

```
python3 main.py
```
