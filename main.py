from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>About Me Page</h1>"

@app.route("/about")
def aboutMe():
    return """<p>I am currently a student at North Seattle College and currently persuing a Full Stack Development 
    certificate. I am currently not sure what I want to do after that but I am keeping my eyes and options open. I grew
    up in Seattle and really love living here. I like to go to parks and beaches, most commonly I will go to Discovery Park 
    or will see some of the japanese gardens that are in south Seattle.</p>"""
if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))
# to jump back into the env just run : source venv/bin/activate