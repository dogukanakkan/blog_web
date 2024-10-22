# controllers.py
from models import BlogPost, db

class BlogController:
    def get_all_posts(self):
        return BlogPost.query.order_by(BlogPost.created_at.desc()).all()

    def get_post(self, post_id):
        return BlogPost.query.get(post_id)

    def add_post(self, title, content):
        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

    def update_post(self, post_id, title, content):
        post = BlogPost.query.get(post_id)
        if post:
            post.title = title
            post.content = content
            db.session.commit()

    def delete_post(self, post_id):
        post = BlogPost.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
