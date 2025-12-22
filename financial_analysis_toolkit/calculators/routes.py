from flask import Blueprint, render_template, request
from calculators.logic import compound_interest, real_after_tax_rate, simple_interest, total_amount_simple_interest, compound_interest2

calculator_bp = Blueprint("calculators", __name__, template_folder="templates")



@calculator_bp.route("/compound_interest", methods=["GET", "POST"])
def compound_interest_calculator():
    result_nominal = result_real = None
    chart_data = {}

    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"]) / 100
        years = int(float(request.form["years"]))
        tax = float(request.form.get("tax", 0)) / 100
        inflation = float(request.form.get("inflation", 0)) / 100

        result_nominal = compound_interest(principal, rate, years)
        # result_nominal = compound_interest2(principal, rate, years, 4)
        real_rate = real_after_tax_rate(rate, tax, inflation)
        result_real = compound_interest(principal, real_rate, years)
        # result_real = compound_interest2(principal, real_rate, years, 4)


        chart_data = {
            "labels": [f"Year {i}" for i in range(years + 1)],
            "nominal": [compound_interest(principal, rate, i) for i in range(years + 1)],
            "real": [compound_interest(principal, real_rate, i) for i in range(years + 1)]
        }

    return render_template("compound_interest.html", result_nominal=result_nominal, result_real=result_real, chart_data=chart_data)

@calculator_bp.route("/simple_interest", methods=["GET","POST"])
def simple_interest_calculator():
    result_nominal = None
    chart_data = {}
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"]) / 100
        years = int(float(request.form["years"]))
        tax = float(request.form.get("tax", 0)) / 100
        inflation = float(request.form.get("inflation", 0)) / 100

        result_nominal = simple_interest(principal, rate, years)
        result_total = total_amount_simple_interest(principal, rate, years)
    return render_template("simple_interest.html",result_nominal = result_nominal, result_total = result_total)

@calculator_bp.route("/home", methods=["GET"])
def index():
    return render_template("index.html")
