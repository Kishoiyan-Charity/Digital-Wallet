# **Digital Wallet Application**

## Overview
This Digital Wallet application is built with **Django** and **Python**, allowing users to securely manage their finances by storing, sending, and receiving funds. Users can link bank accounts, add cards, view transaction history, and monitor their balance—all through a simple and intuitive web interface.

## Features
- **Secure Transactions**: Transfer funds safely between users.
- **Account Linking**: Connect multiple bank accounts and cards for easy management.
- **Transaction History**: Access a detailed history of all transactions.
- **Notifications**: Get alerts for every transaction.
- **Balance Monitoring**: Track available balance in real-time.
- **User Authentication**: Secure login and registration with Django's built-in authentication.

## Installation

### Prerequisites
- **Python 3.8+**
- **Django 4.x**
- **SQLite** (default database for local development, can be replaced with PostgreSQL or MySQL for production)
  
## Clone the Repository:
- git clone https://github.com/Kishoiyan-Charity/Digital-Wallet.git
   cd Digital-Wallet

  ## Create a Virtual Environment:
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

  ## Install Dependencies:
- pip install -r requirements.txt

## Run Migrations:
- python manage.py migrate

## Create a Superuser (for admin access):
- python manage.py createsuperuser

## Start the Development Server:
- python manage.py runserver




  
