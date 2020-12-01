from flask import Blueprint, render_template, redirect, request

from models.budget import Budget
import repositories.budget_repository as budget_repository

budgets_blueprint = Blueprint("budgets", __name__)

# INDEX
@budgets_blueprint.route("/budgets")
def budgets():
    budgets = budget_repository.select_all()
    if len(budgets):
        budget = budgets[0]
    else:
        budget = None
    return render_template("budgets/index.html", budget=budget)

# CREATE
@budgets_blueprint.route("/budgets", methods = ["POST"])
def create_budget():
    amount=request.form['amount']
    new_budget = Budget(amount)
    budget_repository.save(new_budget)
    return redirect("/budgets")

# DELETE

@budgets_blueprint.route("/budgets/<id>/delete", methods=["POST"])
def delete_budget(id):
    budget_repository.delete(id)
    return redirect("/budgets")



