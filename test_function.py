# content of test_sample.py

import pytest
import bs4
from bs4 import BeautifulSoup
from function import extract_id, extract_published, extract_title, extract_city, extract_price, extract_url

@pytest.fixture
def div():
    html = open("./annonces/informatique.html", "r")
    soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")
    div = soup.find(name="div", attrs={"class":"row"})
    return div

@pytest.fixture
def div2():
    html = open("./annonces/test.html", "r")
    soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")
    div = soup.find(name="div", attrs={"class":"row"})
    return div

@pytest.fixture
def div3():
    html = open("./annonces/test2.html", "r")
    soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")
    div = soup.find(name="div", attrs={"class":"row"})
    return div

def test_extract_id(div):
    assert extract_id(div) == "987654"

def test_bad_extract_id(div2):
    assert extract_id(div2) == "Nothing_found"

def test_extract_published(div):
    assert extract_published(div) == 0

def test_bad_extract_published(div2):
    assert extract_published(div2) == "Nothing_found"

def test_extract_published_with_text_not_expected(div3):
    assert extract_published(div3) == "Nothing_found"

def test_extract_title(div):
    assert extract_title(div) == "Titre de l'annonce 1"

def test_bad_extract_title(div2):
    assert extract_title(div2) == "Nothing_found"

def test_extract_city(div):
    assert extract_city(div) == "Paris (75)"

def test_bad_extract_city(div2):
    assert extract_city(div2) == "Nothing_found"

def test_extract_price(div):
    assert extract_price(div) == 233

def test_bad_extract_price(div2):
    assert extract_price(div2) == "Nothing_found"

def test_extract_url(div):
    assert extract_url(div) == "annonce1.html"

def test_bad_extract_url(div2):
    assert extract_url(div2) == "Nothing_found"
