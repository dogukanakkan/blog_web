# app.py
from flask import Flask, render_template, redirect, url_for, request
from models import db, BlogPost
from controllers import BlogController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Veritabanı tablolarını uygulama başlamadan önce oluşturmak için
with app.app_context():
    db.create_all()

# Ana sayfa: Tüm blog yazılarını listeler
@app.route('/')
def index():
    controller = BlogController()
    posts = controller.get_all_posts()
    return render_template('index.html', posts=posts)

# Blog yazısı ekleme sayfası
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    controller = BlogController()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        controller.add_post(title, content)
        return redirect(url_for('index'))
    return render_template('new_post.html')

# Tekil blog yazısı görüntüleme sayfası
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    controller = BlogController()
    post = controller.get_post(post_id)
    return render_template('post.html', post=post)

# Blog yazısını silme
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    controller = BlogController()
    controller.delete_post(post_id)
    return redirect(url_for('index'))

# Blog yazısını güncelleme
@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    controller = BlogController()
    post = controller.get_post(post_id)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        controller.update_post(post_id, title, content)
        return redirect(url_for('post_detail', post_id=post_id))
    return render_template('new_post.html', post=post, update=True)

if __name__ == "__main__":
    app.run(debug=True)
