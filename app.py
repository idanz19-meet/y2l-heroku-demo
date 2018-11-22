from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with class antagonisms. It has but established new classes, new conditions of oppression, new forms of struggle in place of the old ones.'

if __name__ == '__main__':
    app.run(debug=True)

