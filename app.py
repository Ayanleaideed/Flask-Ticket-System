from flask import Flask, request, render_template, redirect, url_for
from tools import Ticket_system, style_css

# Import the TicketDatabase class
from database import TicketDatabase

app = Flask(__name__, static_url_path="/static")

ticket_system = Ticket_system()
ticket_db = TicketDatabase()  # Create an instance of TicketDatabase


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("desc")
        category = request.form.get("cate")
        obj = {"title": title, "description": description, "category": category}

        if request.form.get("action") == "view":
            return redirect(url_for("view_all_tickets"))

        try:
            ticket_system.Create_ticket(
                obj["title"], obj["description"], obj["category"]
            )  # Create a new ticket
        except:
            custom_css = style_css()
            return custom_css.createStyle()

        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("index.html")


@app.route("/view", methods=["GET"])
def view_all_tickets():
    tickets = ticket_system.view_ticket()
    return render_template("data.html", data=tickets)


# Populate the ticket database with initial data
initial_tickets = [
    {
        "title": "New Feature Request",
        "description": "Requesting a new feature for the software.",
        "category": "Feature Request",
    },
    {
        "title": "Bug in Login Page",
        "description": "Users are unable to log in due to a bug.",
        "category": "Bug Report",
    },
    {
        "title": "Website Redesign Proposal",
        "description": "Proposal for redesigning the company website.",
        "category": "Design",
    },
    {
        "title": "Database Performance Issue",
        "description": "Database queries are slow, causing performance problems.",
        "category": "Performance",
    },
    {
        "title": "Software License Renewal",
        "description": "Renewal of software licenses for the upcoming year.",
        "category": "License",
    },
    {
        "title": "Hardware Replacement Request",
        "description": "Request to replace a malfunctioning hardware component.",
        "category": "Hardware",
    },
    {
        "title": "Training Request",
        "description": "Request for training on a specific software module.",
        "category": "Training",
    },
    {
        "title": "Website Content Update",
        "description": "Request to update content on the company website.",
        "category": "Content Update",
    },
    {
        "title": "Server Maintenance",
        "description": "Scheduled server maintenance tasks.",
        "category": "Maintenance",
    },
    {
        "title": "General Inquiry",
        "description": "General inquiry about the software product.",
        "category": "General",
    },
]

for ticket_data in initial_tickets:
    ticket_system.Create_ticket(
        ticket_data["title"], ticket_data["description"], ticket_data["category"]
    )

if __name__ == "__main__":
    app.run(debug=True)
