from facebook_page_scraper import Facebook_scraper
import pandas as pd

#instantiate the Facebook_scraper classas

page_name = "theknowledgehouse"
posts_count = 10
browser = "chrome"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 600 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

json_data = meta_ai.scrap_to_json()

pd.read_json(json_data).transpose()

facebook_data = pd.read_json(json_data).transpose()