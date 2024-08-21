# Staff Management System

## Description

The Staff Management System is a Django-based web application designed to manage Staff records. It allows administrators to perform Create, Read, Update and Delete operations on Staff initials, including details like first name, last name, email, phone number and depertment.

## Features

- **List Staff:** View a list of all Staff with their information.
- **Add Staff:** Add new staff to the system.
- **Update Staff:** Modify existing staff details.
- **Delete Staff:** Delete staff from the database.
- **Search Staff:** Search for staff based on various criteria (first name, last name, email, department, phone).

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML,Bootstrap
- **Database:** SQLite (default for Django development)
- **Version Control:** Git, GitHub

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aaustinoduor/StaffManager.git
   cd StaffManager
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` (login with superuser credentials).
- Use the provided views and forms to manage staff records.
- Navigate to `http://127.0.0.1:8000/` to view and interact with the Staff management interface.

## Contributing

Contributions are highly welcome.Should one be interested,you are encouraged to fork the repository and submit a pull request for any farther developments or enhancements.

## License

This project is licensed under [MIT License](https://opensource.org/licenses/MIT).

