# ⚡ Multi-threaded Python Port Scanner

A fast and efficient network utility written in Python for scanning open ports on a target host. This tool leverages **multi-threading** to significantly reduce the scanning time compared to traditional single-threaded scanners.

---

## ✨ Features

* **Multi-threading:** Utilizes Python's `threading` module to check multiple ports concurrently.
* **Custom Range:** Supports defining a specific starting and ending port for the scan.
* **Clear Output:** Clearly reports open, closed, and filtered ports.
* **Simple Syntax:** Easy to run from the command line with minimal arguments.

---

## 🚀 Installation

This scanner relies only on standard Python libraries (like `socket` and `threading`), so no extra packages are required!

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/shravanitin21/python-port-scanner.git](https://github.com/shravanitin21/python-port-scanner.git)
    cd python-port-scanner
    ```
2.  **Ensure Python is installed:** (Python 3.x required)

---

## 🛠️ Usage

The script requires three command-line arguments: the **Target IP Address**, the **Starting Port**, and the **Ending Port**.

### Basic Syntax

```bash
python Project1.py <target_ip> <start_port> <end_port>
