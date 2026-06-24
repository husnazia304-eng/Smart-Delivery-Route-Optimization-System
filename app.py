from flask import Flask, render_template, request
from route_optimizer import a_star_search
from graph_data import city_graph, heuristic
from graph_visualizer import generate_graph_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    route = []
    total_cost = 0

    if request.method == 'POST':

        start = request.form['start']
        goal = request.form['goal']

        route, total_cost = a_star_search(
            city_graph,
            heuristic,
            start,
            goal
        )

    generate_graph_image(route)

    return render_template(
        'index.html',
        route=route,
        total_cost=total_cost
    )

if __name__ == '__main__':
    app.run(debug=True)