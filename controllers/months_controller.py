from flask import Blueprint, Flask, render_template, redirect, request
import datetime

months_blueprint = Blueprint("months", __name__)