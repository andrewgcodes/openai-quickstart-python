import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        temp=float(request.form["temperature"])
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(animal),
            max_tokens=100,
            temperature=temp,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three creative taglines for a product.

Product: Diamonds
Taglines: [1] A diamond is forever. [2] shine bright like a diamond. [3] bedazzle the world.
Product: State Farm Insurance
Taglines: [1] Like a good neighbor State Farm Insurance is there. [2] Keep your peace of mind. [3] Here for you.
Product: Nike Athletic Clothing
Taglines: [1] Just Do It. [2] Find your greatness. [3] Greatness is not born, it is made.
Product: Dollar Shave Club
Taglines: [1] Shave time. Shave money. [2] A great shave for a few bucks a month. [3] Scratch off lottery tickets. Not your face

Product: {}
Taglines:""".format(
        animal.capitalize()
    )
