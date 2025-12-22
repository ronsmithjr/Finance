# app.py
from flask import Flask, render_template
from calculators.routes import calculator_bp

app = Flask(__name__)
app.register_blueprint(calculator_bp)

@app.route("/")
def toolkit():
    categories = {
        "🧠 Core Analytical Modules": [
            "Real After-Tax Return Calculator",
            "Multi-Currency Swap Valuation Engine",
            "Scenario-Based Cash Flow Forecaster",
            "Benchmarking Dashboard",
        ],
        "📦 Export & Documentation Enhancers": [
            "Markdown + PDF Report Generator",
            "Excel Export with Conditional Formatting",
            "HTML Snapshot Builder",
        ],
        "📈 Visualization & UI Ideas": [
            "Interactive Curve Viewer",
            "FX Heatmap Generator",
            "Flask-Based Calculator Suite",
        ],
        "🧩 Integration & Automation Concepts": [
            "GitHub-Linked Audit Trail",
            "FastAPI Endpoint for Real-Time Valuation",
            "Jupyter Notebook Templates",
        ],
    }
    return render_template("index.html", categories=categories)

if __name__ == "__main__":
    app.run()
