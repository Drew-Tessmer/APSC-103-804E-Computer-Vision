from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Registered person
person =[]
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", person=person)
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    isMemberof = request.form.get("isMemberof")
    if not name or not isMemberof:
        return render_template("failure.html")
    else:
        person.append(f"{name} from {isMemberof}")
        return redirect("/registrants")

if __name__ == '__main__':
    app.run()
