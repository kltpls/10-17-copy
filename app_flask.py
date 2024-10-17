from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html', title='Home')


@app.route('/blog')
def blog_list():
    return render_template('blog.html', title="blog post")


@app.route('/about')
def about_page():
    return render_template('about_me.html', title="about me")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
