from flask import Blueprint, render_template, redirect, request

from models.budget import Budget
import repositories.budget_repository as budget_repository

budgets_blueprint = Blueprint("budgets", __name__)