# TODO create main class and ticket Object
# TODO create a menu with all the features and functionality
from datetime import datetime as time
from flask import url_for
from Error import *


# ticket Object
class Ticket:
    def __init__(self, title, description, category, status="open"):
        self.title = title
        self.description = description
        self.category = category
        self.status = status
        self.time = time.now().strftime("%Y-%m-%d %H:%M:%S")


# The main class
class Ticket_system:
    def __init__(self) -> None:
        self.ticket = []

    # create a ticket
    def Create_ticket(self, title, description, category):
        if not title or not description or not category:
            raise NoValueException()
        create = Ticket(title, description, category)
        self.ticket.append(create)
        print("Ticket created Successfully!!")

    # view the current tickets
    def view_ticket(self):
        if not self.ticket:
            print("No tickets found....")
            return None
        else:
            tickets_list = []
            for i, ticket in enumerate(self.ticket, start=1):
                ticket_details = {
                    "Ticket": i,
                    "Title": ticket.title,
                    "Description": ticket.description,
                    "Category": ticket.category,
                    "Date": ticket.time,
                    "Status": ticket.status,
                }
                tickets_list.append(ticket_details)

        return tickets_list

    # update the status
    def update_ticket_status(self, ticket_num, status):
        if 1 <= ticket_num <= len(self.ticket):
            self.ticket[ticket_num - 1].status = status
            print("Ticket status updated successfully!")
        else:
            print("invalid ticket number!@!!")

    #  method to delete a current ticket
    def delete_ticket(self, ticket_num):
        if 1 <= ticket_num <= len(self.ticket):
            del self.ticket[ticket_num - 1]
            print("Ticket deleted Successfully!")
        else:
            print("Invalid ticket number")


class style_css:
    def __init__(self) -> None:
        self.style = (
            "<style>"
            "  .styled-container {"
            "      text-align: center;"
            "      font-family: cursive;"
            "      font-weight: bolder;"
            "      font-size: xx-large;"
            "  }"
            "  .back-button {"
            "      border: 2px solid #3498db;"
            "      padding: 10px 20px;"
            "      border-radius: 8px;"
            "      background-color: navy;"
            "      color: #3498db;"
            "      text-decoration: none;"
            "      position: relative;"
            "      border: none !important;"
            "  }"
            "  .back-button::before {"
            '      content: "\\2190";'
            "      position: absolute;"
            "      left: 0px;"
            "      top: 17px;"
            "  }"
            ".back-button:hover {"
            "opacity: 0.5s;"
            "transition: ease-in-out;"
            "background-color: black;"
            "color: white;"
            "  }"
            ".back-button:active {"
            "opacity: 1.5s;"
            "transition: ease-in-out;"
            "background-color: yellow;"
            "color: black;"
            "  }"
            "</style>"
            '<div class="styled-container">'
            "  <h1>Must Be a Value on The Title or Description or Category</h1>"
            '  <a class="back-button" href="' + url_for("index") + '">Back</a>'
            "</div>"
            '<div style="display: flex; justify-content: center; align-items: center; height: 90vh;">'
            '  <img style="max-width: 80%; height: auto;" src="static/css/cat.jpg" alt="No image">'
            "</div>"
        )

    def createStyle(self):
        return self.style
