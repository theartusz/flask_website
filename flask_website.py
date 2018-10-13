from flask import Flask

# store flask aplication into variable
app = Flask(__name__)

# / is decorator pointing to homepage
@app.route('/')
def home():
    return "Homepage is here!"

# to create 'about' subpage
@app.route('/about/')
def about():
    return 'Webpage content is here!'

if __name__ == '__main__':
    app.run(debug=True)