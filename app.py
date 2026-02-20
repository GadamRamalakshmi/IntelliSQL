import streamlit as st
import sqlite3
import pandas as pd

# ------------------ INTELLIGENT NLP → SQL ------------------

def generate_sql(question):
    q = question.lower()

    if "all students" in q or "show students" in q:
        return "SELECT * FROM student"

    if "infosys" in q:
        return "SELECT * FROM student WHERE company='INFOSYS'"

    if "tcs" in q:
        return "SELECT * FROM student WHERE company='TCS'"

    if "wipro" in q:
        return "SELECT * FROM student WHERE company='WIPRO'"

    if "google" in q:
        return "SELECT * FROM student WHERE company='GOOGLE'"

    if "highest" in q or "maximum" in q or "top" in q:
        return "SELECT * FROM student ORDER BY marks DESC LIMIT 1"

    if "lowest" in q or "minimum" in q or "least" in q:
        return "SELECT * FROM student ORDER BY marks ASC LIMIT 1"

    if "average" in q:
        return "SELECT AVG(marks) AS average_marks FROM student"

    if "above" in q:
        number = ''.join(filter(str.isdigit, q))
        if number:
            return f"SELECT * FROM student WHERE marks > {number}"

    if "below" in q:
        number = ''.join(filter(str.isdigit, q))
        if number:
            return f"SELECT * FROM student WHERE marks < {number}"

    return "SELECT * FROM student"

# ------------------ SQL EXECUTION ------------------

def execute_sql(query):
    conn = sqlite3.connect("data.db")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# ------------------ UI ------------------

def home():
    st.title("Welcome to IntelliSQL")

def about():
    st.title("About IntelliSQL")
    st.write("Intelligent Natural Language to SQL Query System")

def query_page():
    st.title("Intelligent Query Assistance")

    question = st.text_input("Ask your question")

    if st.button("Generate & Execute"):
        sql = generate_sql(question)
        st.subheader("Generated SQL")
        st.code(sql)

        result = execute_sql(sql)
        st.subheader("Result")
        st.dataframe(result)

def main():
    st.sidebar.title("Navigation")

    pages = {
        "Home": home,
        "About": about,
        "Intelligent Query Assistance": query_page
    }

    choice = st.sidebar.radio("Go to", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()
