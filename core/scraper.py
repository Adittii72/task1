import time
import random

def fetch_mock_case_details(case_type, case_number, year):
    """
    Simulates a web scraper by returning a hardcoded dictionary of case data.
    This function does not actually connect to the internet.
    """
    print(f"--- MOCK SCRAPER: Simulating fetch for {case_type} {case_number}/{year} ---")
    
    # Simulate a network delay
    time.sleep(random.uniform(0.5, 1.5))

    # Return a dictionary with data that matches the project requirements
    mock_data = {
        "parties_names": "State of Gemini vs. The People of Python",
        "filing_date": f"15-03-{year}",
        "next_hearing_date": "25-10-2025",
        "case_status": "Pending for hearing",
        "judgment_url": "https://www.example.com/fake_judgment.pdf"
    }
    
    return mock_data