# 📦 Product Explorer & Error-Resilient Logger

## 📌 Overview
In this project, I worked on **File Handling, API Integration, and Exception Handling in Python**.  
The main idea is to simulate a small real-world system that:
- Reads and writes data to files
- Fetches product data from an API
- Handles errors properly without crashing
- Logs errors into a file for tracking

---

## 🛠️ Technologies Used
- Python
- requests library (for API calls)
- File handling (`open`, read, write, append)
- Exception handling (`try-except-finally`)
- datetime module (for logging time)

---

## 📂 Project Files
part3_api_files.py # Main program
python_notes.txt # Notes file created using file handling
error_log.txt # Log file for storing errors
README.md # Documentation


---

## 🚀 Features Implemented

### ✅ Task 1 — File Read & Write
- Created a file `python_notes.txt`
- Wrote 5 lines using write mode
- Appended extra lines using append mode
- Read and printed all lines with numbering
- Counted total number of lines
- Implemented keyword search (case-insensitive)

---

### ✅ Task 2 — API Integration
- Fetched product data from DummyJSON API
- Displayed product details in formatted output
- Filtered products with rating ≥ 4.5
- Sorted filtered products by price (descending)
- Fetched products by category (laptops)
- Sent a POST request to simulate adding a product

---

### ✅ Task 3 — Exception Handling
- Created a safe divide function to avoid crashes
- Handled:
  - ZeroDivisionError
  - TypeError
- Implemented safe file reader using try-except-finally
- Wrapped API calls with exception handling:
  - ConnectionError
  - Timeout
  - General exceptions
- Added input validation loop for product lookup

---

### ✅ Task 4 — Logging System
- Created `error_log.txt` file
- Logged errors with timestamp using datetime
- Logged:
  - Connection errors
  - HTTP errors (like 404)
- Demonstrated logging by triggering errors
- Printed full log file content at the end

---

## ▶️ How to Run

1. Install required library:
2. Run the program:


---

## 📊 Output Includes
- File read/write operations output
- API product data display
- Filtered and sorted product list
- Laptop category products
- Safe division test results
- File reading results
- Product lookup system
- Error log entries

---

## ⚠️ Notes
- DummyJSON API is a test API, so POST request is simulated
- `error_log.txt` content will change based on runtime errors
- Exception handling is used throughout the program to avoid crashes
- Code includes simple comments explaining logic

---

## 📎 Submission Checklist
- ✔ Python file (`part3_api_files.py`)
- ✔ `python_notes.txt` included
- ✔ `error_log.txt` included
- ✔ All 4 tasks implemented
- ✔ Outputs visible
- ✔ Code well-commented
- ✔ Repository is public

---

## 👨‍💻 Author
Sakthivel R
