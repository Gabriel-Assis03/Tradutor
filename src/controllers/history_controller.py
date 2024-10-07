from flask import Blueprint, render_template, request
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def index():
    return HistoryModel.list_as_json()
