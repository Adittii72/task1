## Task 1: Court-Data Fetcher
Hello! This is my submission for Task 1 of the internship assignment.
The goal was to build a small web app that lets you look up Indian court case information. This application serves as a fully functional prototype that demonstrates all the core architectural components required by the assignment.

## Key Features
* **Modern & Responsive UI:** A clean, professional, and mobile-friendly user interface built with enhanced CSS.
* **Dynamic Mock Results:** The application accepts any case type, number, and year and dynamically generates realistic-looking results.
* [cite_start]**Database Persistence:** Every search query and its corresponding result is successfully stored in a PostgreSQL database. [cite: 1]
* [cite_start]**PDF Download Link:** The results include a link to download a sample judgment or order PDF. [cite: 1]


## The Tech Stack (Tools I Used)
* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS
* **Web Scraping (Investigation Phase):** Selenium

## Getting Started (Setup Guide)
Want to run this on your own machine? Here’s how to get set up in a few minutes.
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Adittii72/task1.git
    cd task1
    ```

2.  **Set Up Your Virtual Environment**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```
    
3.  **Install the Dependencies**
    *(Make sure you have run `pip freeze > requirements.txt` in your terminal first to create the file.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Your Database**
    * You'll need PostgreSQL installed and running.
    * Create a new database for the project: `CREATE DATABASE court_data;`
    * Finally, open `task1/config/settings.py` and put your PostgreSQL password in the `PASSWORD` field.

5.  **Run the Database Migrations**
    This command sets up the tables in your new database.
    ```bash
    python manage.py migrate
    ```

6.  **Start the Server!**
    ```bash
    python manage.py runserver
    ```

7.  **Check it Out**
    Open your favorite web browser and head to `http://127.0.0.1:8000/`.

## How to Use It
Once the server is running, navigate to the homepage. The form will be blank. Enter any case type, number, and year into the fields and click the "Search Case" button. The page will reload and display dynamic, mock results based on your input.


### The Challenge: The Live Scraper

My first goal was to pull data directly from the live eCourts portals. I spent a good amount of time building a scraper with Selenium to automate this process. However, I discovered that the portals are protected by some very effective anti-bot security. No matter which scraping technique I tried (from simple clicks to patient waits and even JavaScript injections), the site's security would block the script.

### The Pivot: A Pragmatic Solution

After a thorough investigation, I realized that getting past this was a much bigger challenge than the assignment likely intended. [cite_start]The assignment notes that "Partial completion is okay Just document limitations in README"[cite: 1]. With that in mind, I made a professional, pragmatic decision to build out the entire rest of the application using a "mock" backend.

### The Result: A Complete MVP

This pivot allowed me to successfully build and demonstrate a fully functional Minimum Viable Product (MVP). [cite_start]The final application you see here has a working user interface, a robust Django backend, and a PostgreSQL database for storing all queries and results[cite: 1]. It fulfills all the architectural requirements of the task, with the live scraping component being the only limitation, which has been documented here.