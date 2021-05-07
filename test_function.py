# content of test_sample.py

import pytest
from bs4 import BeautifulSoup
from function import extract_id, extract_published, extract_title, extract_city, extract_price, extract_url

@pytest.fixture
def div():
    html = open("./annonces/informatique.html", "r")
    soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")
    div = soup.find(name="div", attrs={"class":"row"})
    return div

def test_extract_id(div):
    assert extract_id(div) == "987654"

def test_extract_published(div):
    assert extract_published(div) == 0

def test_extract_title(div):
    assert extract_title(div) == "Titre de l'annonce 1"

def test_extract_city(div):
    assert extract_city(div) == "Paris (75)"

def test_extract_price(div):
    assert extract_price(div) == 233

def test_extract_url(div):
    assert extract_url(div) == "annonce1.html"
