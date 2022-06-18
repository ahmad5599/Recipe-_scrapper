from flask import Flask,render_template,redirect,request
from scrapper import get_recipes
app = Flask("RecipeScrapper")

db = {}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/recipe")
def recipe():
  word = request.args.get('word')
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      recipe = fromDb
    else:
      recipe = get_recipes(word)
      db[word] = recipe
  else:
    return redirect("/")

  return render_template( 
    "recipe.html",
    searchBy = word,
    resultNumber = len(recipe),
    recipes = recipe,
  )

app.run(host = "0.0.0.0")