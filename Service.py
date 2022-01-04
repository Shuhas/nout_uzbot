import sqlite3

con = sqlite3.connect('databaza', check_same_thread=False)
cur = con.cursor()


def create_table():
    cur.execute("""CREATE TABLE "brand" ("id"	INTEGER, "nomi"	TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT));""")
    cur.execute("""CREATE TABLE "log" ("id"	INTEGER, "user_log"	TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT));""")
    cur.execute("""CREATE TABLE "noutbuk" ("id"	INTEGER, "brand_id"	TEXT NOT NULL, "nomi" TEXT NOT NULL,
    "cpu"	TEXT NOT NULL, "gpu"	TEXT NOT NULL, "ekran"	TEXT NOT NULL, "ram" TEXT NOT NULL,
    "rom"	TEXT NOT NULL, "narxi" INTEGER NOT NULL, "rang"	TEXT NOT NULL, "garant"	INTEGER NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT), FOREIGN KEY("brand_id") REFERENCES "brand");""")
    cur.execute("""CREATE TABLE "user" ("id" INTEGER, "user_id" INTEGER NOT NULL UNIQUE, "username" TEXT NOT NULL,
    "ism" TEXT, "raqam" INTEGER, PRIMARY KEY("id" AUTOINCREMENT));""")
    con.commit()


def insert_into():
    cur.execute("""INSERT INTO brand (nomi) values ("Acer"), ("Asus"), ("Dell"), ("HP"), ("Lenovo"),
                ("MSI"), ("Razer"), ("Samsung"), ("LG"), ("Microsoft Surface"), ("Apple");""")
    con.commit()

def get_one(pk):
    cur.execute(f"select * from user where user_id")
    root = cur.fetchone()
    return root


def create_user(user_id, username):
    sql = f"insert into user (user_id, username) values ({user_id}, '{username}')"
    cur.execute(sql)
    con.commit()
    return get_one(user_id)

