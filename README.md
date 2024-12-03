Here’s the translated and formatted README in English:  

---

# Real Estate Management System 📋🏡  

This project is a web application designed to manage real estate agents and employees, offering functionalities like inserting, updating, deleting, and querying data stored in a database.  

## 🛠️ **Features**  
1. **Home Page**:  
   - Navigate to various functionalities like insert, update, delete, and search records.  

2. **Database Queries**:  
   - Retrieve all employees.  
   - Retrieve employees with contracts above the average number in their manager's team.  

3. **Employee Management**:  
   - Add new employees.  
   - Update existing employee information.  
   - Delete employee records.  

4. **Real Estate Agent Management**:  
   - Add new real estate agents.  
   - Update existing agent details.  
   - Delete agent records.  

5. **Advanced Query**:  
   - Find employees who signed more contracts than the average in their manager's team.  

## 📚 **Technical Details**  
- **Backend**: Flask Framework.  
- **Database**: SQL Server, managed via `pyodbc`.  
- **Frontend**: Basic HTML forms.  
- **Deployment**: Runs locally on `http://0.0.0.0:5000`.  

## 💻 **Setup Guide**  

### Prerequisites:  
- Python 3.x installed.  
- SQL Server set up and a connection string for `pyodbc`.  

### Installation Steps:  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-url  
   cd your-project-folder  
   ```  

2. Install required dependencies:  
   ```bash  
   pip install flask pyodbc  
   ```  

3. Set up the database:  
   - Use the provided SQL schema to create tables:  
     - **Employees Table** (`ANGAJATI`)  
     - **Real Estate Agents Table** (`AGENTIMOBILIAR`)  

4. Update the connection string in the code:  
   ```python  
   connectionString = "Driver={SQL Server};Server=YOUR_SERVER;Database=YOUR_DB;Trusted_Connection=yes;"  
   ```  

5. Run the application:  
   ```bash  
   python app.py  
   ```  

6. Access the application in your browser:  
   ```  
   http://localhost:5000  
   ```  

## 🔗 **Key Routes**  

### Home Page:  
- Displays navigation links to core functionalities.  

### Employees Management:  
- `/insert` - Add a new employee.  
- `/update/<int:angajati_id>` - Update an existing employee.  
- `/delete/<int:angajati_id>` - Delete an employee.  

### Real Estate Agents Management:  
- `/insert1` - Add a new real estate agent.  
- `/update1/<int:id>` - Update an agent's information.  
- `/delete1/<int:id>` - Delete an agent.  

### Advanced Queries:  
- `/query/<query_text>` - Find employees who exceed the average contracts in their manager's team.  

## 🌟 **Code Structure**  
- **`app.py`**: The main file, defines routes and database interactions.  
- **HTML Templates**: Embedded in the code for forms and table displays.  
- **SQL Queries**: Handles CRUD operations and complex queries.  

## 🛡️ **Security Notes**  
- Use parameterized queries to prevent SQL injection.  
- Avoid hardcoding sensitive credentials (e.g., connection string).  

## 🚀 **Future Improvements**  
- Implement user authentication.  
- Enhance UI using frameworks like Bootstrap.  
- Add API endpoints for easier integration.  

## ✨ **Contributors**  
This project is developed by [Dragos Munteanu]. Open for collaboration!  

---  

Let me know if you'd like any adjustments or additions. 😊
![image](https://github.com/user-attachments/assets/1b2c8c55-de3d-435d-8f81-89404062dc47)

