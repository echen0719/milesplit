import requests
import time
from bs4 import BeautifulSoup

maxAthlete = 16268835
for i in range(1, maxAthlete + 1):
    athlete = "https://www.milesplit.com/athletes/{}".format(i)