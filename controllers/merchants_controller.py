from flask import Blueprint, Flask, render_template, redirect, request

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

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
@merchants_blueprint.route("/merchants/<id>/change_status", methods=["POST"])
def change_status(id):
    merchant = merchant_repository.select(id)
    name = merchant.id
    new_merchant = Merchant(name, id)
    merchant_repository.change_active_status(new_merchant)
