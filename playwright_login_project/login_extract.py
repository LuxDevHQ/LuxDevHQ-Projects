from datetime import datetime
import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"
OUTPUT_FILE = "extracted_data.csv"

def login_and_extract_data():
    records = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                page.goto(LOGIN_URL, timeout=30000)
            except PlaywrightTimeoutError:
                print("❌ Page did not load in time.")
                browser.close()
                return records

            page.fill("#username", USERNAME)
            page.fill("#password", PASSWORD)
            page.click("#submit")
            page.wait_for_load_state("networkidle")

            if "Logged In Successfully" not in page.text_content("body"):
                print("❌ Login may have failed. Success message not found.")
                browser.close()
                return records

            success_message = page.text_content(".post-title") or "Success message not found"
            record = {
                "page_title": page.title(),
                "page_url": page.url,
                "success_message": success_message.strip(),
                "page_text": (page.text_content("body") or "").strip(),
                "extracted_at": datetime.utcnow().isoformat(),
            }
            records.append(record)
            browser.close()
            print("✅ Login and extraction completed successfully.")
    except Exception as exc:
        print(f"❌ Failed during browser automation: {exc}")
    return records

def save_to_csv(records):
    if not records:
        print("⚠️ No records to save.")
        return
    df = pd.DataFrame(records)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Data saved to {OUTPUT_FILE}.")

def main():
    records = login_and_extract_data()
    save_to_csv(records)

if __name__ == "__main__":
    main()
