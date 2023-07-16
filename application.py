from flask import Flask
from flask import render_template
from flask import request
from simple_recommender import get_recommendations

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Homepage')


@app.route('/recommender')
def recommender():
    form_data = dict(request.args)
    recommendations = get_recommendations()

    return render_template('recommendations.html',
                           movies=recommendations,
                           evaluation=form_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
