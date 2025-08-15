# 🏨 Hotel Management System

This **Python** and **MySQL**-based Hotel Management System provides a comprehensive, menu-driven solution for managing hotel operations. It allows staff to efficiently handle room bookings, manage customer records, and process billing, all through a user-friendly interface. The system ensures data persistence and integrity by leveraging a **MySQL database** to store all critical information.

## ✨ Features

  * **Room Management**: Instantly check room availability, including details like room type and pricing.
  * **Booking Engine**: Seamlessly book rooms for customers and automatically update their status.
  * **Automated Billing**: Generate accurate bills based on room prices, simplifying the checkout process.
  * **Customer Database**: Access and view a complete list of customer records and their assigned rooms.
  * **Robust & Reliable**: Built on a MySQL database for persistent storage, ensuring all data is saved securely.
  * **User-Friendly**: Features a simple, menu-driven interface with comprehensive error handling to prevent common issues.

## 🛠️ Technology Stack

  * **Programming Language**: Python 3.x
  * **Database**: MySQL
  * **Python Library**: PyMySQL
  * **Development Environment**: Any Python IDE (e.g., VS Code, PyCharm) and a MySQL server (e.g., MySQL Workbench, XAMPP, or WAMP).

-----

## 🚀 Getting Started

Follow these steps to get the Hotel Management System up and running on your local machine.

### Prerequisites

Ensure you have Python 3.x and MySQL installed on your system.

### Installation

1.  **Clone the Repository**
    Start by cloning the project from GitHub using the command line:

    ```bash
    git clone https://github.com/Nikhil-Kumar-Shah/Hotel_Management_System.git
    cd Hotel_Management_System
    ```

2.  **Install Required Libraries**
    The project relies on the `PyMySQL` library to connect to the MySQL database. Install it using `pip`:

    ```bash
    pip install pymysql
    ```

3.  **Database Setup**
    Set up the database and its tables by executing the SQL commands provided in `Hotel_Management_System_database.txt`.

      * Open your MySQL environment (e.g., MySQL Workbench or a command-line interface).
      * Run the provided SQL script to create the `hotel_db` database and its tables (`rooms`, `customers`, and `billing`).

4.  **Configure Database Connection**
    Open the `Hotel_Management_System.py` file and update the database connection details to match your MySQL server's credentials:

    ```python
    conn = pymysql.connect(
        host="localhost",
        user="your_mysql_user", # Replace with your MySQL username
        password="your_mysql_password", # Replace with your MySQL password
        database="hotel_db"
    )
    ```

5.  **Run the Application**
    Once the setup is complete, you can start the application from your terminal:

    ```bash
    python Hotel_Management_System.py
    ```

    The main menu will be displayed, and you can begin managing the hotel.

-----

## 🖥️ Usage Guide

The application's menu-driven interface makes it easy to navigate. Simply enter the number corresponding to the action you want to perform and follow the on-screen instructions.

### Main Menu

  * `1` – **View Available Rooms**: Displays a list of all rooms that are currently not booked.
  * `2` – **Book a Room**: Guides you through the process of assigning a room to a customer.
  * `3` – **Generate Bill**: Calculates and displays the total bill for a customer.
  * `4` – **View Customers**: Shows a list of all customers, including their assigned room.
  * `5` – **Exit**: Closes the application.

-----

## 📂 Project Structure

```
Hotel_Management_System/
│
├── Hotel_Management_System.py        # Core application logic
├── Hotel_Management_System_database.txt # SQL script for database setup
└── README.md                         # Project documentation
```

-----

## 📜 Database Schema

The database is structured to support the application's core functions with three main tables:

**`rooms`**
Stores information about each room.

  * `RoomID`: Primary key, auto-incrementing.
  * `RoomType`: The type of room (e.g., 'Single', 'Double', 'Suite').
  * `Price`: The nightly cost of the room.
  * `Availability`: Status of the room (`'Available'` or `'Booked'`).

**`customers`**
Holds customer details and their room assignment.

  * `CustomerID`: Primary key, auto-incrementing.
  * `CustomerName`: The name of the customer.
  * `RoomID`: Foreign key referencing `rooms`, can be null if the customer has checked out.

**`billing`**
Manages billing records for customers.

  * `BillID`: Primary key, auto-incrementing.
  * `CustomerID`: Foreign key referencing `customers`.
  * `Amount`: The total amount of the bill.
  * `BillDate`: Timestamp of when the bill was generated.
