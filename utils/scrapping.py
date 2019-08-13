# -*- coding: utf-8 -*-
import pickle
import numpy as np
import os

import pickle
import numpy as np
import os
import spacy
from spacy import displacy
from collections import Counter
from bs4 import BeautifulSoup
import requests
import re

def url_to_string(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    title_tag = soup.find('h1')
    title = title_tag.text
    body_tag = soup.find_all('p')
    #errors found in websites, added everytime one if found:
    errors = ["Video Smart Player invented by Digiteka", "AdvertisementSupported by", "Advertisement"]
    body = []
    for p in body_tag:
        if p.text in errors:
            pass
        else:
            body.append(p.text)
            body.append("\n\n")
    #formatting errors found in websites, added everytime one if found:
    formatted_body = "".join(body).replace("\xa0", "").replace("\n\t", "").replace("/AP/SIPA","")
    formatted_text = title + "\n\n" + formatted_body

    return formatted_text
