from flask import Blueprint, Flask, render_template, redirect, request
import datetime

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository





merchants_blueprint = Blueprint("merchants", __name__)

#INDEX
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)

#CREATE
#POST '/merchants'
@merchants_blueprint.route("/merchants", methods = ["POST"])
def create_merchant():
    name=request.form['name']
    new_merchant = Merchant(name)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")


#DELETE
#DELETE '/merchants/<id>
@merchants_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')

#UPDATE

@merchants_blueprint.route("/merchants/<id>/deactivate", methods=["POST"])
def deactivate(id):
    merchant_repository.deactivate(id)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/activate", methods=["POST"])
def activate(id):
    merchant_repository.activate(id)
    return redirect("/merchants")

# SHOW

@merchants_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.select_for_merchants(id)
    total = transaction_repository.get_merchant_total(id)
    return render_template("merchants/show.html", merchant=merchant, transactions=transactions, total=total)




