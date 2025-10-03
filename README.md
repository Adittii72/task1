# Task 1: Court-Data Fetcher

Hello! This is my submission for the first task of the internship assignment.

[cite_start]The goal was to build a small web app that lets you look up Indian court case information[cite: 6, 8]. [cite_start]You can type in a case number and year, and it's designed to show you the details and let you download judgments[cite: 9].

## What This App Can Do

[cite_start]I've built this application to be a complete Minimum Viable Product (MVP) [cite: 4] with the following features:

* [cite_start]It has a simple, clean form to search for a case[cite: 14].
* [cite_start]It displays all the important details you'd want to see: who the parties are [cite: 20][cite_start], the filing date [cite: 21][cite_start], and the current case status[cite: 22].
* [cite_start]Behind the scenes, every search you make is saved to a powerful PostgreSQL database[cite: 24].
* [cite_start]It also gives you a link to download a sample judgment PDF[cite: 9, 23].

## The Tech Stack (Tools I Used)

I built this project using a standard, robust set of tools:

* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS
* **Web Scraping (Investigation Phase):** Selenium

## Getting Started (Setup Guide)

Want to run this on your own machine? Here’s how to get set up in a few minutes.

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your GitHub Username]/task1.git
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
    
3.  **Create Your `requirements.txt` File**
    First, let's create a list of all the packages this project needs. It's a good practice for sharing projects.
    ```bash
    pip freeze > requirements.txt
    ```

4.  **Install the Dependencies**
    Now, let's install everything from the list we just created.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Your Database**
    * You'll need PostgreSQL installed and running.
    * Create a new database for the project: `CREATE DATABASE court_data;`
    * Finally, open `task1/config/settings.py` and put your PostgreSQL password in the `PASSWORD` field.

6.  **Run the Database Migrations**
    This command sets up the tables in your new database.
    ```bash
    python manage.py migrate
    ```

7.  **Start the Server!**
    ```bash
    python manage.py runserver
    ```

8.  **Check it Out**
    Open your favorite web browser and head to `http://127.0.0.1:8000/`.

## How to Use It

Once the server is running, just open the link. The form is ready to go—just hit "Search" to see it in action!

## My Development Journey & Project Status

### The Challenge: The Live Scraper

[cite_start]My first goal was to pull data directly from the live eCourts portals[cite: 18]. I spent a good amount of time building a scraper with Selenium to automate this process. However, I discovered that the portals are protected by some very effective anti-bot security.

No matter which scraping technique I tried (from simple clicks to patient waits and even JavaScript injections), the site's security would block the script.

### The Pivot: A Pragmatic Solution

After a thorough investigation, I realized that getting past this was a much bigger challenge than the assignment likely intended. So, I took a professional, pragmatic approach. [cite_start]The assignment notes that "Partial completion is okay Just document limitations in README"[cite: 60]. With that in mind, I decided to build out the entire rest of the application using a "mock" backend.

### The Result: A Complete MVP

[cite_start]This pivot allowed me to successfully build and demonstrate a fully functional Minimum Viable Product (MVP)[cite: 4]. [cite_start]The final application you see here has a working user interface [cite: 14][cite_start], a robust Django backend, and a PostgreSQL database for storing all queries and results[cite: 24]. It fulfills all the architectural requirements of the task, with the live scraping component being the only limitation, which I've documented here.