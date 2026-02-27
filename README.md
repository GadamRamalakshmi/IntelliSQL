# IntelliSQL – Intelligent SQL Query Assistance

IntelliSQL is a web-based intelligent query system that allows users to interact with relational databases using simple natural language instead of writing complex SQL queries.  
The system converts user input into SQL statements and retrieves data dynamically from a database.

---

##  Live Deployment

🔗 **Live Application:**  
https://intellisql-ar9xxynks7v6swmsudvmqg.streamlit.app/

---

##  Features

- Natural language to SQL conversion  
- Intelligent Query Assistance  
- Highest / Lowest / Average marks detection  
- Company-based filtering (Infosys, TCS, Wipro, Google)  
- Above / Below marks filtering  
- Interactive Streamlit web interface  
- Lightweight SQLite database  

---

##  Technologies Used

- Python  
- Streamlit (Web Framework)  
- SQLite (Database)  
- Pandas (Data Handling)  

---

##  Project Structure

```
IntelliSQL/
│
├── app.py
├── sql.py
├── data.db
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Local Setup

Follow these steps to run IntelliSQL locally on your system:

### 1️.Clone the Repository

```bash
git clone https://github.com/GadamRamalakshmi/IntelliSQL.git
```

### 2️. Navigate to Project Folder

```bash
cd IntelliSQL
```

### 3️. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️. Run the Application

```bash
streamlit run app.py
```

The application will start and open automatically in your browser at:

http://localhost:8501

---

## How It Works

1. The user enters a query in simple English (natural language).  
2. The system processes the input using rule-based text matching.  
3. A corresponding SQL query is generated automatically.  
4. The SQL query is executed on a SQLite database.  
5. The results are retrieved and displayed in an interactive Streamlit interface.  

This workflow eliminates the need for users to manually write SQL commands.

---

##  Use Cases

- Students learning SQL and database concepts  
- Beginners practicing database querying  
- Academic mini and major projects  
- Demonstrating Natural Language Processing concepts  
- Lightweight intelligent database interfaces  

---

##  Future Enhancements

- Support for multi-table JOIN queries  
- Integration of AI-powered NLP models (LLMs)  
- Voice-to-SQL functionality  
- Cloud database integration (MySQL/PostgreSQL)  
- Graphical data visualization (charts and dashboards)  
- User authentication and role-based access control  

---

##  Author

**Ramalakshmi Gadam**  
B.Tech Final Year Project  
Intelligent Database Interface System  

---

##  Support

If you found this project useful, consider giving it a ⭐ on GitHub.
