from flask import Flask

app = Flask(__name__)



@app.get("/welcome")
def welcome():
    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.get("/welcome/<address>")
def welcome_home(address):
    html = f"<html><body><h1>Welcome {address}</h1></body></html>"
    return html

