# 🦷 Dental World Jashore

[![Live Site](https://img.shields.io/badge/Live_Demo-Render-008080?style=for-the-badge\&logo=render)](https://dentalworldjashore.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge\&logo=django\&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)](https://www.mysql.com/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Media%20Storage-3448C5?style=for-the-badge\&logo=cloudinary\&logoColor=white)](https://cloudinary.com/)

A modern, dynamic **clinic management and appointment booking platform** developed for **Dental World Jashore**.

The platform allows patients to explore dental services, view dentist profiles, and request appointments online. Clinic administrators can manage website content, appointments, dentists, services, gallery images, and clinic information through a dedicated Django administration dashboard.

🔗 **Live Website:** https://dentalworldjashore.onrender.com

---

## 📸 Project Overview

**Dental World Jashore** is designed to provide a professional online presence for a dental clinic while simplifying appointment management and content administration.

The system combines a responsive frontend with a powerful Django backend, MySQL database, and Cloudinary-based media storage.

### 👥 User Roles

* **Patients**

  * Create an account
  * Log in securely
  * Browse dental services
  * View dentist profiles
  * Book appointments
  * Book appointments for family members
  * Select preferred dentists, services, dates, and times

* **Administrators / Staff**

  * Manage patients
  * Manage dentists
  * Manage dental services
  * Manage appointments
  * Manage clinic information
  * Upload and manage gallery images
  * Update social media links
  * Manage website content through Django Admin

---

## ✨ Key Features

### 📅 Smart Appointment Booking

Patients can request appointments by selecting:

* Patient
* Dentist
* Dental service
* Preferred date
* Preferred time
* Reason for appointment
* Additional notes

The system also supports appointment booking for family members.

---

### 🦷 Dentist Management

Administrators can dynamically manage dentist information, including:

* Doctor name
* Specialization
* Qualification
* Years of experience
* Biography
* Contact information
* Profile photo

Dentist information is displayed dynamically throughout the website.

---

### 💉 Dental Service Management

Dental services can be managed directly from the Django administration panel.

Each service can include:

* Service name
* Description
* Starting price
* Estimated treatment duration
* Service image/content

This allows clinic staff to update service information without modifying the source code.

---

### 🖼️ Clinic Gallery

The website includes a dynamic gallery for showcasing:

* Clinic facilities
* Treatment environments
* Events
* Dental procedures
* Successful treatments
* Other promotional photographs

Images are uploaded through the administration panel and stored using **Cloudinary**.

---

### 🏥 Dynamic Clinic Information

Administrators can update important clinic information from the Django Admin panel, including:

* Clinic name
* Logo
* Contact information
* Address
* Social media links
* Other website information

This makes the website easier to maintain without requiring code changes.

---

### 🔐 User Authentication

The platform provides authentication functionality for patients and staff.

Features include:

* User registration
* Login
* Logout
* Session management
* Protected user functionality

---

### 📊 Google Analytics

Google Analytics integration allows the clinic to monitor website activity and understand visitor behavior.

Administrators can use analytics data to monitor:

* Website visitors
* Traffic sources
* User activity
* Popular pages
* Overall website engagement

---

### 📱 Responsive Design

The website is designed to work across different screen sizes:

* 💻 Desktop
* 💻 Laptop
* 📱 Mobile
* 📟 Tablet

The interface uses responsive layouts, smooth scrolling, and dynamic navigation for a better user experience.

---

# 🛠️ Technology Stack

## Backend

* **Python 3.14**
* **Django 5.2**
* **PyMySQL**

## Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Vanilla JavaScript**

## Database

* **MySQL 8.0**

## Media Storage

* **Cloudinary**

## Deployment

* **Render**
* **Gunicorn**
* **WhiteNoise**

## Analytics

* **Google Analytics**

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      Patients       │
                    │                     │
                    │ • Register/Login    │
                    │ • View Services     │
                    │ • View Dentists     │
                    │ • Book Appointment  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Django Web App    │
                    │                     │
                    │ • Views             │
                    │ • Templates         │
                    │ • Authentication    │
                    │ • Appointment Logic │
                    └──────┬───────┬──────┘
                           │       │
                 ┌─────────┘       └─────────┐
                 ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │     MySQL       │         │   Cloudinary    │
        │                 │         │                 │
        │ • Patients      │         │ • Gallery       │
        │ • Dentists      │         │ • Doctor Photos │
        │ • Services      │         │ • Media Files   │
        │ • Appointments  │         └─────────────────┘
        └─────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │      Admin       │
                  │                  │
                  │   Django Admin   │
                  └──────────────────┘
```

---

# 📂 Project Structure

```text
DentalWorldJashore/
│
├── manage.py
├── requirements.txt
├── build.sh
├── README.md
├── .gitignore
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── clinic/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── appointments/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── services.html
│   ├── dentists.html
│   ├── gallery.html
│   └── appointments/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
│
└── media/
```

> The exact folder structure may vary depending on the final project configuration.

---

# 🚀 Local Setup & Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Inta-tech/your-repo-name.git
cd your-repo-name
```

Replace `your-repo-name` with the actual GitHub repository name.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

> Never upload your `.env` file or secret credentials to GitHub.

---

# 🗄️ Database Setup

Make sure MySQL is installed and running.

Create the database:

```sql
CREATE DATABASE dental_world_jashore;
```

Then run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 👤 Create an Admin Account

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:

```text
Username
Email
Password
```

Then start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# ☁️ Cloudinary Configuration

Cloudinary is used to store uploaded media files such as:

* Dentist profile photos
* Clinic gallery images
* Treatment images
* Other website media

The application uses Cloudinary so uploaded media does not need to be stored directly on the Render server filesystem.

Configure the following environment variables:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

# 🌐 Deployment

The application is deployed using **Render**.

Production architecture:

```text
                 Internet
                    │
                    ▼
              ┌───────────┐
              │   Render  │
              │           │
              │ Gunicorn  │
              │  Django   │
              └─────┬─────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    ┌───────────┐       ┌────────────┐
    │   MySQL   │       │ Cloudinary │
    │ Database  │       │   Media    │
    └───────────┘       └────────────┘
```

### Production Server

Gunicorn is used as the application server:

```bash
gunicorn config.wsgi:application
```

### Static Files

WhiteNoise is used to efficiently serve Django static files in production.

---

# 🔒 Security

The project follows standard Django security practices, including:

* Environment variables for sensitive credentials
* Django authentication
* CSRF protection
* Secure password hashing
* Database-backed sessions
* Protected administration interface
* Production configuration for secret keys

Sensitive information should never be committed to GitHub.

---

# 📈 Future Improvements

Potential future enhancements include:

* 🔔 Appointment confirmation notifications
* 📧 Email notifications
* 📱 SMS appointment reminders
* 💳 Online payment integration
* 📊 Advanced admin analytics dashboard
* 🗓️ Interactive dentist availability calendar
* 🧾 Digital treatment records
* 💊 Prescription management
* 🧑‍⚕️ Doctor-specific dashboards
* 📱 Progressive Web App (PWA) support
* 🔍 Advanced appointment search and filtering

---

# 🎯 Project Objectives

The main objectives of Dental World Jashore are to:

1. Provide a professional online presence for the dental clinic.
2. Allow patients to conveniently request appointments online.
3. Reduce manual appointment management.
4. Provide administrators with centralized content management.
5. Showcase dentists and dental services dynamically.
6. Provide an organized platform for managing clinic information.
7. Improve accessibility through a responsive web interface.

---

# 👨‍💻 Developer

**Inta-tech**

Computer Science & Engineering Student

GitHub:
https://github.com/Inta-tech

---

# 📄 License

This project was developed specifically for **Dental World Jashore**.

All rights reserved.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

🔗 **Live Website:**
https://dentalworldjashore.onrender.com
