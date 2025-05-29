# InventoryManagement

**InventoryManagement** is a web-based application built with **Python**, **Django**, **HTML5**, and **CSS**. It offers a simple yet effective way to manage inventory items with user authentication, role-based access, and activity tracking.

## Features

- **User Authentication**
  - Login / Logout
  - User Registration

- **Role-Based Access Control**
  - Viewer (User): Can only view data
  - Editor (Staff): Can create, update, and delete items

- **Inventory CRUD**
  - Add, view, update, and delete inventory records (Editor only)

- **Activity Logging**
  - Displays who added or updated each item
  - Shows when each change was made

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/InventoryManagement.git
   cd InventoryManagement

2. **Set up a virtual environment and activate it (I used anaconda)**
   ```bash
   create -n myenv
   conda activate myenv

3. **Install django**
   ```bash
   pip install django

4. **Run the development server**
   ```bash
   python manage.py runserver

4. **Open your browser and go to 'http://127.0.0.1:8000'**

### Demo Accounts

You can use the following dummy users to test the app:

**Editor 1 Account**  
- Employee ID: LP001  
- Password: Yousef01

**Editor 2 Account**  
- Employee ID: LP002  
- Password: Sarah01

**Viewer Account**  
- Employee ID: LP003  
- Password: QobyO001
