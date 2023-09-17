from flask import Flask, request, render_template, redirect, url_for
from tools import Ticket_system, style_css

# use this database to store you tickets if need as long time save
# NOTE: just remove the object that we are currently storing the value to the database
from database import TicketDatabase

app = Flask(__name__, static_url_path="/static")

ticket_system = Ticket_system()  # Create an instance of Ticket_system


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("desc")
        category = request.form.get("cate")
        obj = {"title": title, "description": description, "category": category}
        if request.form.get("action") == "view":
            return redirect(
                url_for("view_all_tickets")
            )  # Redirect to the view_all_tickets route
        if request.form.get("action") == "view":
            return redirect(url_for("view_all_tickets"))
        else:
            try:
                ticket_system.Create_ticket(
                    obj["title"], obj["description"], obj["category"]
                )  # Create a new ticket
            except:
                custom_css = style_css()  # Create an instance of the style_css class
                return custom_css.createStyle()
            return redirect(url_for("index"))  # Redirect back to the index route
    if request.method == "GET":
        return render_template("index.html")


@app.route("/view", methods=["GET"])
def view_all_tickets():
    tickets = ticket_system.view_ticket()
    return render_template("data.html", data=tickets)


if __name__ == "__main__":
    app.run(debug=True)
