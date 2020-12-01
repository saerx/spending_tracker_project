from flask import Blueprint, Flask, render_template, redirect, request

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

#INDEX
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    # transactions.sort(key=lambda r:r.trans_time, reverse=True)
    total = transaction_repository.get_decimalised_total()
    budget_alert = transaction_repository.budget_alerts()
    return render_template("transactions/index.html", transactions=transactions, total=total, budget_alert=budget_alert)

#NEW
#Get '/transactions/new'
@transactions_blueprint.route("/transactions/new", methods = ["GET"])
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", all_merchants=merchants, all_tags=tags)

#CREATE
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    #Grab the form data for tran_time, amount, merchant, and tag
    trans_time = request.form["trans_time"]
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    #select the merchant and tag using the repository
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    #creates a new Transaction object
    transaction = Transaction(amount, merchant, tag, trans_time)
    transaction_repository.save(transaction)

    return redirect('/transactions')