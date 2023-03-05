from flask import Flask, render_template, request, redirect
from flask_app.models.addresses_model import Address
from flask_app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=['POST'])
def create():
    if not Address.validator(request.form):
        return redirect('/')
    Address.create(request.form)
    return redirect('/success')

@app.route("/success")
def success():
    all_addresses = Address.get_all()
    return render_template("success.html", all_addresses=all_addresses)