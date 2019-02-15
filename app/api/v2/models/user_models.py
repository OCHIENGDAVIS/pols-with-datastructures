from app.api.v2.models.db import db_connection


class User():
    def __init__(self, _id, firstname, lastname, username, othername, email, password, phone, passpot, isPolitician, isAdmin):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.othername = othername
        self.email = email
        self.password = password
        self.phoneNumber = phone
        self.passportUrl = passpot
        self.isPolitician = isPolitician
        self.isAdmin = isAdmin

    @classmethod
    def save_user(cls, id, firstname, lastname, username, othername, email, password, phone, passport, ispolitician, is_admin):
        connection = db_connection()
        query = """
            INSERT INTO users (id, firstname, lastname, username, othername, email,password, phonNumber, passportUrl, isPolitician,isAdmin)
            VALUES(?, ?, ?,?,?,?,?,?,?,?, ?)
        """
        cursor = connection.cursor()
        cursor.execute(query, (id, firstname, lastname, username, othername, email,
                               password, phone, passport, ispolitician, is_admin))
        connection.commit()
        connection.close()

    @classmethod
    def user_exists(cls, id):
        connection = db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        result = cursor.execute(query, (id,))
        if result:
            row = result.fetchone()
            if row is not None:
                return True
        return False
