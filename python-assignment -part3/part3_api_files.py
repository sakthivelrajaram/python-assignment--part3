# ============================================
# Product Explorer & Logger (Student Version)
# ============================================

import requests
from datetime import datetime

# -------------------------------
# TASK 1 - FILE HANDLING
# -------------------------------

file_name = "python_notes.txt"

# writing basic notes into file
with open(file_name, "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    f.write("Topic 2: Lists are ordered and mutable.\n")
    f.write("Topic 3: Dictionaries store key-value pairs.\n")
    f.write("Topic 4: Loops automate repetitive tasks.\n")
    f.write("Topic 5: Exception handling prevents crashes.\n")

print("File created and written.")

# appending few more topics (extra learning)
with open(file_name, "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help reuse code.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")

print("Extra topics added.")

# reading file line by line
print("\nReading file content:")
lines = []

with open(file_name, "r", encoding="utf-8") as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(str(count) + ". " + line.strip())

print("Total lines:", count)

# simple keyword search
key = input("Enter a word to search: ").lower()
found = False

for line in lines:
    if key in line.lower():
        print("Matched:", line.strip())
        found = True

if not found:
    print("No match found for given keyword")

# -------------------------------
# LOGGER FUNCTION
# -------------------------------

def write_log(place, err_type, msg):
    # writing logs with time
    with open("error_log.txt", "a", encoding="utf-8") as f:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{t}] ERROR in {place}: {err_type} — {msg}\n")

# -------------------------------
# TASK 2 - API
# -------------------------------

base_url = "https://dummyjson.com/products"

# safe request function (to avoid crash if internet fails)
def get_data(url):
    try:
        r = requests.get(url, timeout=5)
        return r
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        write_log("get_data", "ConnectionError", "internet issue")
    except requests.exceptions.Timeout:
        print("Server taking too long")
        write_log("get_data", "Timeout", "slow response")
    except Exception as e:
        print("Some error:", e)
        write_log("get_data", "Exception", str(e))
    return None

# Step 1 - fetch products
print("\nFetching products...")

resp = get_data(base_url + "?limit=20")

products = []

if resp and resp.status_code == 200:
    data = resp.json()
    products = data["products"]

    print("\nID | Name | Price | Rating")
    for p in products:
        print(p["id"], "|", p["title"], "|", p["price"], "|", p["rating"])

print("Total products fetched:", len(products))

# Step 2 - filter
print("\nTop rated products (>=4.5):")

top_items = []
for p in products:
    if p["rating"] >= 4.5:
        top_items.append(p)

# sorting manually style
top_items.sort(key=lambda x: x["price"], reverse=True)

for p in top_items:
    print(p["title"], "- ₹", p["price"])

# Step 3 - category
print("\nLaptop category products:")

resp = get_data(base_url + "/category/laptops")

if resp and resp.status_code == 200:
    laptops = resp.json()["products"]
    for item in laptops:
        print(item["title"], ":", item["price"])

# Step 4 - POST request
print("\nTrying POST request...")

try:
    r = requests.post(
        base_url + "/add",
        json={
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "Created by me"
        },
        timeout=5
    )
    print("Response:", r.json())
except Exception as e:
    write_log("post_api", "Exception", str(e))

# -------------------------------
# TASK 3 - EXCEPTION HANDLING
# -------------------------------

# safe divide function
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid data types"

print("\nTesting divide function:")
print("Case 1:", safe_divide(10, 2))
print("Case 2:", safe_divide(10, 0))
print("Case 3:", safe_divide("ten", 2))

# file reader
def read_file_safe(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found:", name)
    finally:
        print("Tried reading file.")

print("\nReading existing file:")
print(read_file_safe("python_notes.txt"))

print("Trying missing file:")
print(read_file_safe("ghost.txt"))

# input loop
print("\nProduct lookup (type 'quit' to exit):")

while True:
    user = input("Enter product ID: ")

    if user.lower() == "quit":
        break

    if not user.isdigit():
        print("Enter valid number")
        continue

    pid = int(user)

    if pid < 1 or pid > 100:
        print("Out of range (1-100)")
        continue

    resp = get_data(base_url + "/" + str(pid))

    if resp:
        if resp.status_code == 404:
            print("Product not found")
            write_log("lookup", "HTTPError", "404 id " + str(pid))
        elif resp.status_code == 200:
            d = resp.json()
            print("Name:", d["title"], "| Price:", d["price"])

# -------------------------------
# TASK 4 - LOGGING DEMO
# -------------------------------

# forcing connection error
get_data("https://this-host-does-not-exist-xyz.com/api")

# forcing http error
resp = get_data(base_url + "/999")

if resp and resp.status_code != 200:
    write_log("fetch", "HTTPError", "wrong id 999")

# show log file
print("\nLog file content:")

try:
    with open("error_log.txt", "r") as f:
        print(f.read())
except:
    print("No logs yet")