from flask import Blueprint, Flask, render_template, redirect, request
import datetime

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository



tags_blueprint = Blueprint("tags", __name__)

#INDEX
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

#CREATE
#POST '/tags'
@tags_blueprint.route("/tags", methods = ["POST"])
def create_tag():
    name=request.form['name']
    new_tag = Tag(name)
    tag_repository.save(new_tag)
    return redirect("/tags")


# DELETE
# DELETE '/tags/<id>
@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect('/tags')

# UPDATE

@tags_blueprint.route("/tags/<id>/deactivate", methods=["POST"])
def deactivate(id):
    tag_repository.deactivate(id)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/activate", methods=["POST"])
def activate(id):
    tag_repository.activate(id)
    return redirect("/tags")

# SHOW

@tags_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repository.select(id)
    transactions = transaction_repository.select_for_tags(id)
    total = transaction_repository.get_tag_total(id)
    return render_template("tags/show.html", tag=tag, transactions=transactions, total=total)