# Furni

## Overview
Furmi is a web application built using Python, Django, and Bootstrap. It provides a platform for users to browse and purchase furniture items. The application features user authentication, product listings, and a shopping cart.

## Features
- **User Authentication:** Register, login, and logout functionality.
- **Product Listings:** View detailed information about furniture items.
- **Shopping Cart:** Add items to the cart and manage the cart.
- **Responsive Design:** Mobile-friendly and responsive design using Bootstrap.

## Technologies Used
- **Python:** Programming language for backend development.
- **Django:** Web framework for building the application.
- **Bootstrap:** CSS framework for responsive design.

## Getting Started

### Prerequisites
Ensure you have the following installed on your local development machine:
- Python (v3.6 or higher)
- pip (Python package installer)
- virtualenv (for creating virtual environments)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/furmi.git
    ```

2. Navigate to the project directory:
    ```bash
    cd furmi
    ```

3. Create a virtual environment:
    ```bash
    virtualenv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project
To start the development server, run:
```bash
python manage.py runserver
```

### Applying Migrations
Before running the project, ensure the database migrations are applied:
```bash
python manage.py migrate
```

## Project Structure
```
furmi/
├── furmi/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
├── manage.py
├── requirements.txt
├── README.md
└── ...
```



## Contact
For any questions or feedback, please contact:
- Name: Ketan Pillai
- Email: ketanpillai@gmail.com



