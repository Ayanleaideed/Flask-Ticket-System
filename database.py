import sqlite3


class TicketDatabase:
    def __init__(self, db_name="ticket_system.db"):
        self.db_name = db_name
        # self.conn = sqlite3.connect(self.db_name)
        self.conn = sqlite3.connect("ticket_system.db", check_same_thread=False)

        self.create_table()

    def create_table(self):
        create_table_sql = """
          CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT
          )
        """
        self.conn.execute(create_table_sql)
        self.conn.commit()

    def insert_ticket(self, title, description, category):
        insert_sql = (
            "INSERT INTO tickets (title, description, category) VALUES (?, ?, ?)"
        )
        # Use a tuple to provide the values for the placeholders (?, ?, ?)
        self.conn.execute(insert_sql, (title, description, category))
        self.conn.commit()

    def view_tickets(self):
        view_sql = "SELECT * FROM tickets"
        cursor = self.conn.execute(view_sql)
        tickets = cursor.fetchall()
        return tickets

    def delete_Entry(self, id):
        delete_ticket = "DELETE FROM tickets WHERE id = ?"
        self.conn.execute(delete_ticket, (id,))
        # Reset the id sequence
        reset_sequence = "DELETE FROM sqlite_sequence WHERE name = 'tickets'"
        self.conn.execute(reset_sequence)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def admin(self, Pass):
        # NOTE: password to delete everything on the table is "YES"
        if Pass == "YES":
            count = self.view_tickets()
            try:
                for ticket in count:
                    self.delete_Entry(ticket[0])
                    # print(ticket[0])
            except:
                return []


db = TicketDatabase()
# db.insert_ticket("Test new Ticket", "Desc Testing", 'Systems')
# db.delete_Entry(1)
db.admin("YES")


# print(db.view_tickets())
# db.close()
