from flask import Flask , render_template ,redirect,url_for, request
from flask_assets import Bundle, Environment
from forms import RegistrationForm
from api_control import search_first
# from books_nlp import book_recom
from sklearn.externals import joblib
import pandas as pd
books = pd.read_csv('csv_files/books.csv',encoding = "ISO-8859-1")
cosine_sim_corpus = joblib.load('trained.pkl')
indices = pd.Series(books.index, index = map(lambda x:x.upper(),books['title']))
app = Flask(__name__)
app.config["SECRET_KEY"] = '8e62a758c0cc1f9c5c3eadab82a809fd'
js = Bundle('jquery.min.js','breakpoints.min.js','main.js','browser.min.js','util.js',output = 'gen/javas.js')
assets = Environment(app)
assets.register("main_js",js)
posts = [
{
'author': "wewr",
"title": "Harry Potter "
},
{
'author': "bvdfbdf",
"title": "Goblet of Fires"
}]
@app.route('/index')
def hello_world():
    return render_template("index.html",posts = posts)

@app.route('/')
@app.route('/',methods = ["POST"])
def login():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data == 'Pankaj Gaur' and form.email.data == 'admin@admin.com':
            return render_template("search.html",title = 'Login',form = form)
    return render_template("about.html",title = 'Login',form = form)
@app.route('/search')
def search():
    return render_template("index.html")


@app.route('/recommend',methods = ["POST"])
def recommend():
    if request.method == "POST":
        rawtext = request.form['rawtext']
        first = search_first(rawtext)

        idx = indices[rawtext]
        sim_scores = list(enumerate(cosine_sim_corpus[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]
        book_indices = [i[0] for i in sim_scores]
        pf = books.iloc[book_indices][['title','image_url']]

        plist1 = []
        plist2 = []
        plist3 = []

        for i in range(0,3):
            plist1.append({'title':pf.iloc[i]['title'],'image_url':pf.iloc[i]['image_url']})
        for i in range(3,6):
            plist2.append({'title':pf.iloc[i]['title'],'image_url':pf.iloc[i]['image_url']})
        for i in range(6,9):
            plist3.append({'title':pf.iloc[i]['title'],'image_url':pf.iloc[i]['image_url']})


        return render_template("search.html", plist1 = plist1,plist2 = plist2,plist3 = plist3,first = first)

if __name__ == "__main__":
    app.run(debug = True)
