
import pyodbc
from flask import Flask, request, redirect

SERVER = 'DESKTOP-3F4V5CM\SQLEXPRESS'
DATABASE = 'ProiectMunteanuDragos'
USERNAME = 'sa'
PASSWORD = 'MercesLetifer*03'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};ENCRYPT=NO'
SQL_QUERY = """
SELECT TOP 1000
    ANGAJATI.AngajatiID,
    ANGAJATI.Nume,
    ANGAJATI.Prenume,
    ANGAJATI.CNP,
    ANGAJATI.Strada,
    ANGAJATI.Numar,
    ANGAJATI.Oras,
    ANGAJATI.Judet,
    ANGAJATI.Sex,
    ANGAJATI.DataNasterii,
    ANGAJATI.Salariu,
    ANGAJATI.MANAGERID
    
FROM ANGAJATI
ORDER BY ANGAJATI.AngajatiID;
"""
SQL_QUERY1 = """
SELECT TOP 1000
    AGENTIMOBILIAR.ID,
    AGENTIMOBILIAR.AngajatiID,
    AGENTIMOBILIAR.NumarContracte,
    AGENTIMOBILIAR.ZonaActivare,
    AGENTIMOBILIAR.IDManager
    
FROM AGENTIMOBILIAR
ORDER BY AGENTIMOBILIAR.ID;
"""
def fetch_records():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    conn.close()
    return records

def insert_record(record):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO ANGAJATI (Nume, Prenume, CNP, Strada, Numar, Oras, Judet, Sex, DataNasterii, Salariu, MANAGERID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, record)
    conn.commit()
    conn.close()

def delete_record(angajati_id):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ANGAJATI WHERE AngajatiID = ?", angajati_id)
    conn.commit()
    conn.close()
def fetch_records1():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY1)
    records1 = cursor.fetchall()
    conn.close()
    return records1

def insert_record1(record1):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO AGENTIMOBILIAR (ID,AngajatiID, NumarContracte, ZonaActivare, IDManager)
    VALUES (?, ?, ?, ?, ?)
    """, record1)
    conn.commit()
    conn.close()

def delete_record1(id):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AGENTIMOBILIAR WHERE ID = ?", id)
    conn.commit()
    conn.close()
# Create a Flask app
app = Flask(__name__)

# Define a route to display the HTML table
@app.route('/')
def display_table():
    # Fetch records from SQL on every page refresh
    records = fetch_records()

    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>ANGAJATIID</th><th>NUME</th><th>Prenume</th><th>CNP</th><th>Strada</th><th>Numar</th><th>Oras</th><th>Judet</th><th>Sex</th><th>DataNasterii</th><th>Salariu</th><th>MANAGERID</th><th>Actions</th></tr>\n"
    for r in records:
        table_html += f"<tr><td>{r.AngajatiID}</td><td>{r.Nume}</td><td>{r.Prenume}</td><td>{r.CNP}</td><td>{r.Strada}</td><td>{r.Numar}</td><td>{r.Oras}</td><td>{r.Judet}</td><td>{r.Sex}</td><td>{r.DataNasterii}</td><td>{r.Salariu}</td><td>{r.MANAGERID}</td><td><a href='/delete/{r.AngajatiID}'>Delete</a> | <a href='/update/{r.AngajatiID}'>Update</a></td></tr>\n"
    table_html += "</table>"
    
    # Add insert button
    table_html += """
    <form action="/insert" method="GET">
        <input type="submit" value="Insert">
    </form>
    """
    
    records1 = fetch_records1()

    # Generate HTML table
    table1_html = "<table>\n"
    table1_html += "<tr><th>ID</th><th>AngajatiID</th><th>NumarContracte</th><th>ZonaActivare</th><th>IDManager</th><th>Actions</th></tr>\n"
    for r1 in records1:
        table1_html += f"<tr><td>{r1.ID}</td><td>{r1.AngajatiID}</td><td>{r1.NumarContracte}</td><td>{r1.ZonaActivare}</td><td>{r1.IDManager}</td><td><a href='/delete1/{r1.ID}'>Delete</a> | <a href='/update1/{r1.ID}'>Update</a></td></tr>\n"
    table1_html += "</table>"
    
    # Add insert button
    table1_html += """
    <form action="/insert1" method="GET">
        <input type="submit" value="Insert">
    </form>
    """
    button_html = "<form action='/execute_query1' method='GET'><input type='submit' value='Execute Query1'></form>\n"
    button_html += "<form action='/execute_query2' method='GET'><input type='submit' value='Execute Query2'></form>\n"
    button_html += "<form action='/execute_query3' method='GET'><input type='submit' value='Execute Query3'></form>\n"
    button_html += "<form action='/execute_query4' method='GET'><input type='submit' value='Execute Query4'></form>\n"
    button_html += "<form action='/execute_query5' method='GET'><input type='submit' value='Execute Query5'></form>\n"
    button_html += "<form action='/execute_query6' method='GET'><input type='submit' value='Execute Query6'></form>\n"
    button_html += "<form action='/execute_query7' method='GET'><input type='submit' value='Execute Query7'></form>\n"
    button_html += "<form action='/execute_query8' method='GET'><input type='submit' value='Execute Query8'></form>\n"
    button_html += "<form action='/execute_query9' method='GET'><input type='submit' value='Execute Query9'></form>\n"
    button_html += "<form action='/execute_query10' method='GET'><input type='submit' value='Execute Query10'></form>\n"
    # Define a route to handle executing a query
    
    
    return table_html+table1_html+button_html
@app.route('/execute_query1', methods=['GET'])
def execute_query():
    # Perform the query execution logic here
    query_sql = """
    SELECT
    a.AngajatiID,
    a.Nume,
    a.Prenume,
    a.Sex,
    a.Salariu,
    b.Sex AS ManagerSex,
    b.Salariu AS ManagerSalary
    FROM ANGAJATI a
    INNER JOIN [dbo].[ANGAJATI] b ON a.MANAGERID = b.AngajatiID
    WHERE a.Sex = 'F' AND a.Salariu > (SELECT AVG(Salariu) FROM [dbo].[ANGAJATI] WHERE Sex = 'M');
    """
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(query_sql)
    records = cursor.fetchall()
    conn.close()

    # Generate HTML response with query and textbox
    response_html = f"""
    <p>Query:</p>
    <pre>{query_sql}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,SEXUL,SALARIUL,SEXUL MANAGERULUI SI SALARIUL MANAGERULUI ANGAJATILOR DE SEX FEMININ CARE AU SALARIUL MAI MARE DECAT MEDIA SALARIILOR ANGAJATILOR DE SEX MASCULIN</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AngajatiID</th><th>Nume</th><th>Prenume</th><th>Sex</th><th>Salariu</th><th>ManagerSex</th><th>ManagerSalary</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AngajatiID}</td><td>{record.Nume}</td><td>{record.Prenume}</td><td>{record.Sex}</td><td>{record.Salariu}</td><td>{record.ManagerSex}</td><td>{record.ManagerSalary}</td></tr>\n"
    table_html += "</table>"

    response_html += table_html

    return response_html
@app.route('/execute_query2', methods=['GET'])
def execute_query2():
    sqlquery2 = """
    SELECT
    a.AngajatiID AS AgentID,
    a.Nume AS AgentName,
    a.Sex AS AgentSex,
    a.Salariu AS AgentSalary,
    b.Nume AS ManagerName,
    b.Sex AS ManagerSex,
    b.Salariu AS ManagerSalary
FROM [dbo].[ANGAJATI] a
INNER JOIN [dbo].[ANGAJATI] b ON a.MANAGERID = b.AngajatiID;
"""
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquery2)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquery2}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,SEXUL,SALARIUL,NUMELE COMPLET AL MANAGERULUI,SEXUL SI SALARIUL MANAGERULUI PENTRU TOTI AGENTII IMOBILIARI</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentSex</th><th>AgentSalary</th><th>ManagerName</th><th>ManagerSex</th><th>ManagerSalary</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentSex}</td><td>{record.AgentSalary}</td><td>{record.ManagerName}</td><td>{record.ManagerSex}</td><td>{record.ManagerSalary}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query3', methods=['GET'])
def execute_query3():
    sqlquery3 ="""
    SELECT
    b.AngajatiID AS ManagerID,
    b.Nume AS ManagerName,
    a.AngajatiID AS AgentID,
    c.Nume AS AgentName,
    a.NumarContracte AS AgentContracts
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE a.NumarContracte > 10;
"""
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquery3)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquery3}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,NUMARUL DE CONTRACTE ALE AGENTILOR IMOBILIARI SI NUMELE COMPLET AL MANAGERILOR ACESTORA PENTRU TOTI AGENTII IMOBILIARI CARE AU MAI MULTE DE 10 CONTRACTE</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>ManagerID</th><th>ManagerName</th><th>AgentID</th><th>AgentName</th><th>AgentContracts</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.ManagerID}</td><td>{record.ManagerName}</td><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentContracts}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query4', methods=['GET'])
def execute_query4():
    sqlquerry4 = """
    SELECT
    a.AngajatiID AS AgentID,
    c.Nume AS AgentName,
    c.DataNasterii AS AgentBirthdate,
    b.Nume AS ManagerName,
    b.DataNasterii AS ManagerBirthdate
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE c.DataNasterii > '1970-01-01';
"""
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry4)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry4}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,DATA NASTERII SI NUMELE COMPLET AL MANAGERULUI SI DATA NASTERII ACESTUIA PENTRU TOTI AGENTII IMOBILIARI CARE S-AU NASCUT DUPA 01.01.1990</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentBirthdate</th><th>ManagerName</th><th>ManagerBirthdate</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentBirthdate}</td><td>{record.ManagerName}</td><td>{record.ManagerBirthdate}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query5', methods=['GET'])
def execute_query5():
    sqlquerry5 = """
    SELECT
    a.AngajatiID AS AgentID,
    c.Nume AS AgentName,
    c.Salariu AS AgentSalary,
    b.Nume AS ManagerName,
    b.Salariu AS ManagerSalary
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE c.Salariu > b.Salariu;
"""
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry5)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry5}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET, SALARIUL SI NUMELE COMPLET AL MANAGERULUI SI SALARIUL ACESTUIA PENTRU TOTI AGENTII IMOBILIARI CARE AU SALARIUL MAI MARE DECAT SALARIUL MANAGERULUI LOR</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentSalary</th><th>ManagerName</th><th>ManagerSalary</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentSalary}</td><td>{record.ManagerName}</td><td>{record.ManagerSalary}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query6', methods=['GET'])
def execute_query6():
    sqlquerry6="""
    SELECT
    A.AngajatiID AS AgentID,
    C.Nume AS AgentName,
    a.NumarContracte AS AgentContracts,
    b.Nume AS ManagerName
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE a.NumarContracte = (
    SELECT MAX(NumarContracte)
    FROM [dbo].[AGENTIMOBILIAR]);
"""
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry6)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry6}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,NUMARUL DE CONTRACTE SI NUMELE COMPLET AL MANAGERULUI PENTRU AGENTUL IMOBILIAR CARE ARE CELE MAI MULTE CONTRACTE</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentContracts</th><th>ManagerName</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentContracts}</td><td>{record.ManagerName}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query7', methods=['GET'])
def execute_query7():
    sqlquerry7="""
    SELECT
    b.AngajatiID AS ManagerID,
    b.Nume AS ManagerName,
    COUNT(a.AngajatiID) AS SubordinateCount
FROM [dbo].[AGENTIMOBILIAR] a
RIGHT JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER join [dbo].[ANGAJATI] c on a.AngajatiID = c.AngajatiID
GROUP BY b.AngajatiID, b.Nume
HAVING COUNT(a.AngajatiID) > (
    SELECT AVG(SubordinateCount)
    FROM (
        SELECT COUNT(AngajatiID) AS SubordinateCount
        FROM [dbo].[AGENTIMOBILIAR]
        GROUP BY IDManager
    ) AS SubordinateCounts);
    """
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry7)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry7}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET SI NUMARUL DE SUBORDONATI AL MANAGERILOR CARE AU MAI MULTI SUBORDONATI DECIT MEDIA SUBORDONATILOR TUTUROR MANAGERILOR</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>ManagerID</th><th>ManagerName</th><th>SubordinateCount</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.ManagerID}</td><td>{record.ManagerName}</td><td>{record.SubordinateCount}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query8', methods=['GET'])
def execute_query8():
    sqlquerry8="""
    SELECT
    a.AngajatiID AS AgentID,
    c.Nume AS AgentName,
    c.DataNasterii AS AgentBirthdate,
    b.Nume AS ManagerName,
    b.DataNasterii AS ManagerBirthdate
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE b.Salariu < (
    SELECT AVG(Salariu)
    FROM [dbo].[ANGAJATI]);

    """
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry8)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry8}</pre>
    <p>SA SE AFISEZE NUMELE COMPLET,DATA NASTERII SI NUMELE COMPLET AL MANAGERULUI SI DATA NASTERII ACESTUIA PENTRU TOTI AGENTII IMOBILIARI CARE AU SALARIUL MAI MIC DECAT MEDIA SALARIILOR TUTUROR MANAGERILOR</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentBirthdate</th><th>ManagerName</th><th>ManagerBirthdate</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentBirthdate}</td><td>{record.ManagerName}</td><td>{record.ManagerBirthdate}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query9', methods=['GET'])
def execute_query9():
    return '''
    <form action="/execute_query9_confirm" method="POST">
        <label for="query_text">SA se afiseze Numele si Salariul tuturor angajatilor care au mai mult de 5 contracte incheiate si prenumele:</label>
        <input type="text" id="query_text" name="query_text">
        <input type="submit" value="Submit">
    </form>
    '''
@app.route('/execute_query9_confirm', methods=['POST'])
def execute_query9_confirm():
    query_text = request.form.get('query_text')
    sqlquerry9=f"""
    SELECT
    a.AngajatiID,
    c.Nume,
    c.Prenume,
    a.NumarContracte,
    a.ZonaActivare,
    b.Nume AS ManagerName
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] c ON a.AngajatiID = c.AngajatiID
WHERE c.Prenume = '{query_text}'
    AND a.NumarContracte > 5;

    """
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry9)
    records = cursor.fetchall()
    conn.close()

    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry9}</pre>
    <p>SA se afiseze Numele si Salariul tuturor angajatilor care au mai mult de 5 contracte incheiate si prenumele:{query_text}</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AngajatiID</th><th>Nume</th><th>Prenume</th><th>NumarContracte</th><th>ZonaActivare</th><th>ManagerName</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AngajatiID}</td><td>{record.Nume}</td><td>{record.Prenume}</td><td>{record.NumarContracte}</td><td>{record.ZonaActivare}</td><td>{record.ManagerName}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html
@app.route('/execute_query10', methods=['GET'])
def execute_query10():
    return '''
    <form action="/execute_query10_confirm" method="POST">
        <label for="query_text">SA se afiseze Numele si Numarul de Contracte tuturor angajatilor care au mai multe contracte decat media numarului de contracte incheiate din echipa managerului cu ID:</label>
        <input type="text" id="query_text" name="query_text">
        <input type="submit" value="Submit">
    </form>
    '''
@app.route('/execute_query10_confirm', methods=['POST'])
def execute_query10_confirm():
    query_text = request.form.get('query_text')
    sqlquerry10=f"""
    SELECT
    a.AngajatiID AS AgentID,
    d.Nume AS AgentName,
    a.NumarContracte AS AgentContracts,
    b.Nume AS ManagerName
FROM [dbo].[AGENTIMOBILIAR] a
INNER JOIN [dbo].[ANGAJATI] b ON a.IDManager = b.AngajatiID
INNER JOIN [dbo].[ANGAJATI] d ON a.AngajatiID = d.AngajatiID
WHERE a.NumarContracte > (
    SELECT AVG(c.NumarContracte)
    FROM [dbo].[AGENTIMOBILIAR] c
    WHERE c.IDManager = {query_text}
)
AND a.IDManager = {query_text};

    """
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(sqlquerry10)
    records = cursor.fetchall()
    conn.close()
    
    response_html = f"""
    <p>Query:</p>
    <pre>{sqlquerry10}</pre>
    <p>SA se afiseze Numele si Numarul de Contracte tuturor angajatilor care au mai multe contracte decat media numarului de contracte incheiate din echipa managerului cu ID:{query_text}</p>
    <p>Query Result:</p>
    """
    # Generate HTML table
    table_html = "<table>\n"
    table_html += "<tr><th>AgentID</th><th>AgentName</th><th>AgentContracts</th><th>ManagerName</th></tr>\n"
    for record in records:
        table_html += f"<tr><td>{record.AgentID}</td><td>{record.AgentName}</td><td>{record.AgentContracts}</td><td>{record.ManagerName}</td></tr>\n"
    table_html += "</table>"
    
    response_html += table_html
    
    return response_html

# Define a route to handle record update
@app.route('/update/<int:angajati_id>', methods=['GET'])
def update_data(angajati_id):
    # Fetch the record from the database based on the AngajatiID
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ANGAJATI WHERE AngajatiID = ?", angajati_id)
    record = cursor.fetchone()
    conn.close()

    # Check if the record exists
    if record is None:
        return "Record not found"

    # Put the fetched data into a record
    record = {
        'angajati_id': record.AngajatiID,
        'name': record.Nume,
        'surname': record.Prenume,
        'cnp': record.CNP,
        'street': record.Strada,
        'number': record.Numar,
        'city': record.Oras,
        'county': record.Judet,
        'sex': record.Sex,
        'birth_date': record.DataNasterii,
        'salary': record.Salariu,
        'manager_id': record.MANAGERID
    }

    # Render the update form with the fetched data
    return """
    <html>
    <body>
    <h1>Update Record</h1>
    <form action="/update_confirm" method="POST">
        <input type="hidden" name="angajati_id" value="{angajati_id}">
        
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{name}" required><br><br>
        
        <label for="surname">Surname:</label>
        <input type="text" id="surname" name="surname" value="{surname}" required><br><br>
        
        <label for="cnp">CNP:</label>
        <input type="text" id="cnp" name="cnp" value="{cnp}" required><br><br>
        
        <label for="street">Street:</label>
        <input type="text" id="street" name="street" value="{street}" required><br><br>
        
        <label for="number">Number:</label>
        <input type="text" id="number" name="number" value="{number}" required><br><br>
        
        <label for="city">City:</label>
        <input type="text" id="city" name="city" value="{city}" required><br><br>
        
        <label for="county">County:</label>
        <input type="text" id="county" name="county" value="{county}" required><br><br>
        
        <label for="sex">Sex:</label>
        <input type="text" id="sex" name="sex" value="{sex}" required><br><br>
        
        <label for="salary">Salary:</label>
        <input type="text" id="salary" name="salary" value="{salary}" required><br><br>
        
        <label for="manager_id">ManagerID:</label>
        <input type="text" id="manager_id" name="manager_id" value="{manager_id}" required><br><br>
        
        <input type="submit" value="Update">
    </form>
    </body>
    </html>
    """.format(**record)
# Define a route to handle update confirmation
@app.route('/update_confirm', methods=['POST'])
def update_confirm():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    
    # Get all the form data
    angajati_id = request.form.get('angajati_id')
    name = request.form.get('name')
    surname = request.form.get('surname')
    cnp = request.form.get('cnp')
    street = request.form.get('street')
    number = request.form.get('number')
    city = request.form.get('city')
    county = request.form.get('county')
    sex = request.form.get('sex')
    salary = request.form.get('salary')
    manager_id = request.form.get('manager_id')
    
    
    # Update the record in the database
    SQL_UPDATE = f"""
    UPDATE ANGAJATI
    SET Nume = '{name}',
        Prenume = '{surname}',
        CNP = '{cnp}',
        Strada = '{street}',
        Numar = '{number}',
        Oras = '{city}',
        Judet = '{county}',
        Sex = '{sex}',
        Salariu = {salary},
        MANAGERID = {manager_id}
    WHERE AngajatiID = {angajati_id}
    """
    cursor.execute(SQL_UPDATE)
    conn.commit()
    
    return "Record updated successfully"

    
# Define a route to handle record insertion
# Define a route to handle record insertion
@app.route('/insert', methods=['GET'])
def insert_data():
    return """
    <html>
    <body>
    <h1>Insert Record</h1>
    <form action="/insert_confirm" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="surname">Surname:</label>
        <input type="text" id="surname" name="surname" required><br><br>
        
        <label for="cnp">CNP:</label>
        <input type="text" id="cnp" name="cnp" required><br><br>
        
        <label for="street">Street:</label>
        <input type="text" id="street" name="street" required><br><br>
        
        <label for="number">Number:</label>
        <input type="text" id="number" name="number" required><br><br>
        
        <label for="city">City:</label>
        <input type="text" id="city" name="city" required><br><br>
        
        <label for="county">County:</label>
        <input type="text" id="county" name="county" required><br><br>
        
        <label for="sex">Sex:</label>
        <input type="text" id="sex" name="sex" required><br><br>
        
        <label for="birthdate">Birthdate:</label>
        <input type="text" id="birthdate" name="birthdate" required><br><br>
        
        <label for="salary">Salary:</label>
        <input type="text" id="salary" name="salary" required><br><br>
        
        <label for="manager_id">Manager ID:</label>
        <input type="text" id="manager_id" name="manager_id" required><br><br>
        
        <input type="submit" value="Insert">
    </form>
    </body>
    </html>
    """

# Define a route to handle record insertion confirmation
@app.route('/insert_confirm', methods=['POST'])
def insert_confirm():
    # Perform the record insertion logic here
    # ...
    # Example code to insert data into the database
    record = {
        "name": request.form.get("name"),
        "surname": request.form.get("surname"),
        "cnp": request.form.get("cnp"),
        "street": request.form.get("street"),
        "number": request.form.get("number"),
        "city": request.form.get("city"),
        "county": request.form.get("county"),
        "sex": request.form.get("sex"),
        "birthdate": request.form.get("birthdate"),
        "salary": request.form.get("salary"),
        "manager_id": request.form.get("manager_id")
    }
    
    # Establish a connection to the database
    conn = pyodbc.connect(connectionString)
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Prepare the SQL query
    sql = "INSERT INTO [dbo].[ANGAJATI] (Nume, Prenume, CNP, Strada, Numar, Oras, Judet, Sex, DataNasterii, Salariu, MANAGERID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    # Execute the SQL query with the record values
    cursor.execute(sql, (
        record["name"],
        record["surname"],
        record["cnp"],
        record["street"],
        record["number"],
        record["city"],
        record["county"],
        record["sex"],
        record["birthdate"],
        record["salary"],
        record["manager_id"]
    ))
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return "Record inserted successfully!"
# Define a route to handle record deletion
@app.route('/delete/<int:angajati_id>', methods=['GET'])
def delete_data(angajati_id):
    return """
    <html>
    <body>
    <h1>Are you sure?</h1>
    <form action="/delete_confirm/{}" method="POST">
        <input type="submit" value="Yes">
        <input type="button" value="No" onclick="window.location.href='/'">
    </form>
    </body>
    </html>
    """.format(angajati_id)

# Define a route to handle record deletion confirmation
@app.route('/delete_confirm/<int:angajati_id>', methods=['POST'])
def delete_confirm(angajati_id):
    delete_record(angajati_id)
    return "Record deleted successfully!"



@app.route('/update1/<int:id>', methods=['GET'])
def update_data1(id):
    # Fetch the record from the database based on the ID
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AGENTIMOBILIAR WHERE ID = ?", id)
    record = cursor.fetchone()
    conn.close()

    # Check if the record exists
    if record is None:
        return "Record not found"

    # Put the fetched data into a record
    record = {
        'id': record.ID,
        'angajati_id': record.AngajatiID,
        'numar_contracte': record.NumarContracte,
        'zona_activare': record.ZonaActivare,
        'id_manager': record.IDManager
    }

    # Render the update form with the fetched data
    return """
    <html>
    <body>
    <h1>Update Record</h1>
    <form action="/update_confirm1" method="POST">
        <input type="hidden" name="id" value="{id}">
        
        <label for="angajati_id">AngajatiID:</label>
        <input type="text" id="angajati_id" name="angajati_id" value="{angajati_id}" required><br><br>
        
        <label for="numar_contracte">NumarContracte:</label>
        <input type="text" id="numar_contracte" name="numar_contracte" value="{numar_contracte}" required><br><br>
        
        <label for="zona_activare">ZonaActivare:</label>
        <input type="text" id="zona_activare" name="zona_activare" value="{zona_activare}" required><br><br>
        
        <label for="id_manager">IDManager:</label>
        <input type="text" id="id_manager" name="id_manager" value="{id_manager}" required><br><br>
        
        <input type="submit" value="Update">
    </form>
    </body>
    </html>
    """.format(**record)
@app.route('/update_confirm1', methods=['POST'])
def update_confirm1():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    
    # Get all the form data
    id = request.form.get('id')
    angajati_id = request.form.get('angajati_id')
    numar_contracte = request.form.get('numar_contracte')
    zona_activare = request.form.get('zona_activare')
    id_manager = request.form.get('id_manager')
    
    # Update the record in the database
    SQL_UPDATE = f"""
    UPDATE AGENTIMOBILIAR
    SET AngajatiID = {angajati_id},
        NumarContracte = {numar_contracte},
        ZonaActivare = '{zona_activare}',
        IDManager = {id_manager}
    WHERE ID = {id}
    """
    cursor.execute(SQL_UPDATE)
    conn.commit()
    
    return "Record updated successfully"
@app.route('/insert1', methods=['GET'])
def insert_data1():
    return """
    <html>
    <body>
    <h1>Insert Record</h1>
    <form action="/insert_confirm1" method="POST">
        <label for="angajati_id">AngajatiID:</label>
        <input type="text" id="angajati_id" name="angajati_id" required><br><br>
        
        <label for="numar_contracte">NumarContracte:</label>
        <input type="text" id="numar_contracte" name="numar_contracte" required><br><br>
        
        <label for="zona_activare">ZonaActivare:</label>
        <input type="text" id="zona_activare" name="zona_activare" required><br><br>
        
        <label for="id_manager">IDManager:</label>
        <input type="text" id="id_manager" name="id_manager" required><br><br>
        
        <input type="submit" value="Insert">
    </form>
    </body>
    </html>
    """
@app.route('/insert_confirm1', methods=['POST'])
def insert_confirm1():
    # Perform the record insertion logic here
    # ...
    # Example code to insert data into the database
    record = {
        "angajati_id": request.form.get("angajati_id"),
        "numar_contracte": request.form.get("numar_contracte"),
        "zona_activare": request.form.get("zona_activare"),
        "id_manager": request.form.get("id_manager")
    }
    
    # Establish a connection to the database
    conn = pyodbc.connect(connectionString)
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Prepare the SQL query
    sql = "INSERT INTO [dbo].[AGENTIMOBILIAR] (AngajatiID, NumarContracte, ZonaActivare, IDManager) VALUES (?, ?, ?, ?)"
    
    # Execute the SQL query with the record values
    cursor.execute(sql, (
        record["angajati_id"],
        record["numar_contracte"],
        record["zona_activare"],
        record["id_manager"]
    ))
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return "Record inserted successfully!"

@app.route('/delete1/<int:id>', methods=['GET'])
def delete_data1(id):
    return """
    <html>
    <body>
    <h1>Are you sure?</h1>
    <form action="/delete_confirm1/{}" method="POST">
        <input type="submit" value="Yes">
        <input type="button" value="No" onclick="window.location.href='/'">
    </form>
    </body>
    </html>
    """.format(id)

# Define a route to handle record deletion confirmation
@app.route('/delete_confirm1/<int:id>', methods=['POST'])
def delete_confirm1(id):
    delete_record1(id)
    return "Record deleted successfully!"


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    


