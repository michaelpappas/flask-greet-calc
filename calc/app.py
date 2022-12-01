from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/add")
def add():
    a = request.args.get("a")
    b = request.args.get("b")

    if a and b:
        return f"{int(a) + int(b)}"

    return render_template("add.html")

@app.get("/sub")
def sub():
    a = request.args.get("a")
    b = request.args.get("b")

    if a and b:
        return f"{int(b) - int(a)}"

    return render_template("sub.html")


@app.get("/mult")
def mult():
    a = request.args.get("a")
    b = request.args.get("b")

    if a and b:
        return f"{int(a) * int(b)}"

    return render_template("mult.html")

@app.get("/div")
def div():
    a = request.args.get("a")
    b = request.args.get("b")

    if a and b:
        return f"{int(a) / int(b)}"

    return render_template("div.html")



