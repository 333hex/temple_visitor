from app import app

@app.route("/")
def home():
    return "Temple Visitor Home Page"