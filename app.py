from flask import Flask, render_template, request

from controllers.merchants_controller import merchants_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.budgets_controller import budgets_blueprint
from controllers.months_controller import months_blueprint

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(budgets_blueprint)
app.register_blueprint(months_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/preferences")
def prefs():
    return render_template('preferences.html')

if __name__ == '__main__':
    app.run()