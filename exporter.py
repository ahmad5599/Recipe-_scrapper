import csv

def save_to_file(recipes):
  file = open("recipes.csv",mode = "w")
  writer =csv.writer(file)
  writer.writerow(
    ["title",
    "by",
    "rating",
    "summary",
    "link"])
  for recipe in recipes:
    writer.writerow(list(recipe.values()))
  return 