from flask import Flask, render_template, abort

app = Flask(__name__)

# Simulando posts (depois pode trocar por SQL Database)
posts = [
    {
        "id": 1,
        "title": "Bem-vindo ao meu Blog na Azure",
        "content": "Este blog está rodando em um Azure App Service usando Python e Flask."
    },
    {
        "id": 2,
        "title": "Escalabilidade na Nuvem",
        "content": "A Azure permite escalar aplicações facilmente usando App Service."
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run()
