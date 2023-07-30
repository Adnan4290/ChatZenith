# ChatZenith - Chat Application

ChatZenith is a Python Flask-based chat application that allows users to communicate with each other in real-time. This README provides instructions on how to install the application on your system and how to import the database into XAMPP.

## Installation

To install ChatZenith on your system, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/Adnan4290/ChatZenith.git
```

2. Navigate to the project directory:

```
cd ChatZenith
```

3. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```
pip3 install -r requirements.txt
```

## Database Setup

Before running the application, you need to import the database into XAMPP. Follow these steps:

1. Open XAMPP and start the Apache and MySQL modules.

2. Open your web browser and go to `http://localhost/phpmyadmin`.

3. Log in to phpMyAdmin using your credentials.

4. Create a new database named `ChatZenith_db`.

5. Click on the newly created database, then click on the "Import" tab.

6. Click on the "Choose File" button and select the `ChatZenith_db.sql` file from the `database` folder in the project directory.

7. Click the "Go" button to import the database.

## Running the Application

To run the ChatZenith application, execute the following command:

```
python3 main.py
```

Once the application is running, open your web browser and visit `http://localhost:5000` to access ChatZenith.


