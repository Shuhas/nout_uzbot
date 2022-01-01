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
    PRIMARY KEY("id"), FOREIGN KEY("brand_id") REFERENCES "brand")""")
    cur.execute("""CREATE TABLE "user" ("id" INTEGER, "username" TEXT NOT NULL, "ism" TEXT NOT NULL,
    "raqam"	INTEGER NOT NULL, PRIMARY KEY("id"))""")
    con.commit()


def insert_into():
    cur.execute("""INSERT INTO brand (nomi) values ("Acer"), ("Asus"), ("Dell"), ("HP"), ("Lenovo"),
                ("MSI"), ("Razer"), ("Samsung"), ("LG"), ("Microsoft Surface"), ("Apple")""")
    con.commit()
