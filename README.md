
# 📊 Flask CRUD Application for Employee & Real Estate Agents Management 🏠

Această aplicație Flask permite gestionarea înregistrărilor pentru angajați și agenți imobiliari într-o bază de date SQL Server. Aplicația implementează operații CRUD (Create, Read, Update, Delete) pentru ambele tipuri de date, precum și un raport de interogare care afișează informații relevante despre contractele angajaților.

## 🛠️ Funcționalități

- **Vizualizarea Angajaților**: Afișează lista angajaților din baza de date.
- **Interogare Personalizată**: Afișează angajații care au mai multe contracte decât media contractelor din echipa unui manager specificat.
- **Actualizarea Angajaților**: Permite modificarea datelor unui angajat existent.
- **Inserarea Angajaților**: Permite adăugarea unui nou angajat în baza de date.
- **Ștergerea Angajaților**: Permite ștergerea unui angajat existent din baza de date.
- **Vizualizarea Agenților Imobiliari**: Afișează lista agenților imobiliari din baza de date.
- **Actualizarea Agenților Imobiliari**: Permite modificarea datelor unui agent imobiliar existent.
- **Inserarea Agenților Imobiliari**: Permite adăugarea unui nou agent imobiliar.
- **Ștergerea Agenților Imobiliari**: Permite ștergerea unui agent imobiliar existent.

---

## 🖥️ Tehnologii Folosite

- **Flask** - Framework web Python.
- **pyodbc** - Pentru interacționarea cu baza de date SQL Server.
- **HTML/CSS** - Pentru interfețele de utilizator.
- **SQL Server** - Baza de date pentru stocarea datelor.

---

## 🚀 Cum să Rulezi Aplicația

1. **Clonează repository-ul**:
   ```bash
   git clone https://github.com/username/flask-crud-app.git
   cd flask-crud-app
   ```

2. **Instalează dependențele**:
   Asigură-te că ai instalat Python 3 și pip. Apoi, instalează toate dependențele necesare:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setează conexiunea la baza de date**:
   Asigură-te că baza de date SQL Server este configurată corect și actualizează `connectionString` în cod cu detaliile conexiunii tale.

4. **Rularea aplicației**:
   În directorul principal al proiectului, rulează serverul Flask:
   ```bash
   python app.py
   ```

   Aplicația va fi disponibilă la `http://localhost:5000`.

---

## 🌐 Endpoints Disponibile

### 1. **Pagina Principală** (`/`)
   - Vizualizează lista angajaților și agenților imobiliari.

### 2. **Angajați - Interogare** (`/angajati-query`)
   - Afișează angajații care au mai multe contracte decât media numărului de contracte din echipa managerului.

### 3. **Actualizare Angajat** (`/update/<int:angajati_id>`)
   - Permite actualizarea datelor unui angajat.

### 4. **Confirmare Actualizare Angajat** (`/update_confirm`, `/update_confirm1`)
   - Salvează modificările efectuate pentru un angajat sau agent imobiliar.

### 5. **Inserare Angajat** (`/insert`)
   - Permite inserarea unui nou angajat în baza de date.

### 6. **Inserare Agent Imobiliar** (`/insert1`)
   - Permite inserarea unui nou agent imobiliar.

### 7. **Ștergere Angajat** (`/delete/<int:angajati_id>`)
   - Permite ștergerea unui angajat din baza de date.

### 8. **Ștergere Agent Imobiliar** (`/delete1/<int:id>`)
   - Permite ștergerea unui agent imobiliar din baza de date.

---

## 📂 Structura Directorului

```
/flask-crud-app
|-- app.py             # Codul aplicației Flask
|-- requirements.txt   # Lista dependențelor
|-- templates/         # Folder pentru fișierele HTML
    |-- update_form.html  # Formularul de actualizare
    |-- insert_form.html  # Formularul de inserare
|-- static/            # Folder pentru fișiere statice (CSS, imagini etc.)
```

---

## 📝 Notițe

- Aplicația presupune că există două tabele principale în baza de date: **ANGAJATI** și **AGENTIMOBILIAR**, care sunt folosite pentru a stoca informațiile despre angajați și agenți imobiliari.
- Fiecare funcție pentru actualizare, inserare și ștergere folosește interfețe simple HTML pentru interacțiunea cu utilizatorul.
- Toate datele sunt gestionate într-o bază de date SQL Server folosind pyodbc pentru conectarea la baza de date.

---

## 📌 Probleme Cunoașterea

Dacă întâmpini vreo problemă sau ai sugestii pentru îmbunătățirea aplicației, nu ezita să creezi o problemă pe GitHub sau să contactezi dezvoltatorul. 🚀

---

👨‍💻 **Developed with ❤️ by Dragos Munteanu**

---
![image](https://github.com/user-attachments/assets/1b2c8c55-de3d-435d-8f81-89404062dc47)

