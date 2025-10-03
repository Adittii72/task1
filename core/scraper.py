import time
import random

def fetch_mock_case_details(case_type, case_number, year):
    """
    Simulates a web scraper by returning DYNAMIC mock case data
    based on the user's input.
    """
    print(f"--- MOCK SCRAPER: Simulating fetch for {case_type} {case_number}/{year} ---")
    
    # Simulate a network delay
    time.sleep(random.uniform(0.5, 1.0))

    # --- New: More dynamic mock data ---
    # We can randomize the status for more variety
    statuses = ["Pending for hearing", "Disposed", "Admitted", "Case Closed"]
    
    # Now the mock data uses the input from the form
    mock_data = {
        "parties_names": f"Petitioner for {case_type.upper()} {case_number} vs. Respondent",
        "filing_date": f"{random.randint(1, 28)}-{random.randint(1, 12)}-{year}",
        "next_hearing_date": f"{random.randint(1, 28)}-{random.randint(1, 12)}-2026",
        "case_status": random.choice(statuses),
        "judgment_url": "https://www.example.com/fake_judgment.pdf"
    }
    
    return mock_data