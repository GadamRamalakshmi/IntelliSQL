import sqlite3

def create_database():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        name TEXT,
        marks INTEGER,
        company TEXT
    )
    """)

    students = [
        (1,"Ravi",85,"INFOSYS"),
        (2,"Anita",90,"TCS"),
        (3,"Suresh",75,"INFOSYS"),
        (4,"Meena",88,"WIPRO"),
        (5,"Rahul",95,"GOOGLE")
    ]

    cur.executemany(
        "INSERT OR IGNORE INTO student VALUES (?,?,?,?)",
        students
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
