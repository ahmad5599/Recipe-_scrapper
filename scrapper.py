import requests
from bs4 import BeautifulSoup

def extract_reipe_data(soup):
  title = soup.find("h3",{"class","card__title elementFont__resetHeading"}).string.strip()
  link = soup.find("a")["href"]
  summary = soup.find("div",{"class":"card__summary elementFont__details--paragraphWithin margin-8-tb"}).string.strip()
  recBy = soup.find("span",{"class":"card__authorName"}).string
  rating = soup.find("span",{"class":"ratings-count elementFont__details"})
  if rating is not None:
    rating = rating.string.strip()
  else:
    rating = "No rating yet"
  return {
  'title':title,
  'by':recBy,
  'rating':rating,
  'summary':summary,
  'link':link,
  }


def extract_recipes(url):
  
  # just for my mental health
  print("Scrapping page")  
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")  
  results = soup.find_all("div" , {"class" : "card__detailsContainer-left"})
  
  recipes=[] 

  for result in results:
    recipe = extract_reipe_data(result)
    recipes.append(recipe)

  return recipes
    

def get_recipes(word):
  url = f"https://www.allrecipes.com/search/results/?search={word}"
  recipes = extract_recipes(url)
  return recipes

