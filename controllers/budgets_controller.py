from flask import Blueprint, render_template, redirect, request

from models.budget import Budget
import repositories.budget_repository as budget_repository

budgets_blueprint = Blueprint("budgets", __name__)

# INDEX
@budgets_blueprint.route("/budgets")
def budgets():
    budget = budget_repository.select_all()[0]
    return render_template("budgets/index.html", budget=budget)

# CREATE
@budgets_blueprint.route("/budgets", methods = ["POST"])
def create_budget():
    amount=request.form['amount']
    new_budget = Budget(amount)
    budget_repository.save(new_budget)
    return redirect("/budgets")


