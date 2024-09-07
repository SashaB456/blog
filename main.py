from flask import Flask, redirect, render_template, request
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")
@app.route('/post/category')
def post_category():
    return render_template("post_category.html", categories_list=db.getCategories())
@app.route('/post/view')
def post_view():
    return render_template("post_view.html", posts_list=db.getPosts())
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/post/category/<id>', methods=["GET", "POST"])
def posts_in_category(id):
    if request.method == "POST":
        post_text = request.form.get("text_input")
        if len(post_text) > 0:
            db.addPosts(id, post_text)
            return redirect(f'/post/category/{id}')
    
    return render_template("post_categories.html", posts_list=db.getPostsInCategories(id), name=db.getCategoryByID(id)[0])


app.run(debug=True, host="0.0.0.0")
