import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuration ---
COURT_URL = "https://services.ecourts.gov.in/ecourtindia_v6/"

def run_scraper():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    print(f"Navigating to: {COURT_URL}")
    driver.get(COURT_URL)
    
    try:
        # --- Step 1: Wait for and Click 'Case Status' using a JavaScript Click ---
        print("Waiting for the 'Case Status' link to be present on the page...")
        wait = WebDriverWait(driver, 10)
        
        # We will wait for the element to just be PRESENT, not necessarily clickable
        case_status_link = wait.until(
            EC.presence_of_element_located((By.ID, "left-menu-case-status"))
        )
        
        print("Found 'Case Status' link. Forcing click with JavaScript...")
        # This is the new method: we execute a script to click the element
        driver.execute_script("arguments[0].click();", case_status_link)

        # --- Step 2: Select a State from the dropdown ---
        print("Waiting for the State dropdown to be ready...")
        state_dropdown_element = wait.until(
            EC.presence_of_element_located((By.ID, "sess_state_code"))
        )

        state_dropdown = Select(state_dropdown_element)
        
        print("Selecting 'Delhi' from the State dropdown...")
        state_dropdown.select_by_visible_text("Delhi")
        
        print("Successfully navigated and selected the state.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        print("\nScript will close the browser in 20 seconds.")
        time.sleep(20)
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    run_scraper()