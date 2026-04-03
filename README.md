#  Regression Testing Tool for Software Versions

## 📌 Project Overview

The **Regression Testing Tool** is a Python-based automation utility designed to compare outputs between two different versions of a software program. It helps identify unintended changes or bugs introduced in newer versions by executing both versions with the same input and analyzing their outputs.

This project supports quality assurance processes and contributes to sustainable software development practices.

---

## 🎯 Objectives

* Automate comparison between software versions
* Detect regressions (unexpected output changes)
* Improve software reliability and consistency
* Reduce manual testing effort

---

## 🌍 Sustainable Development Goal (SDG)

This project aligns with **SDG 12 – Responsible Consumption and Production** by:

* Reducing software defects and rework
* Promoting efficient use of development resources
* Encouraging sustainable and reliable software delivery

---

## ⚙️ Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code
* **Libraries Used:**

  * `subprocess` (for executing scripts)
  * `os` (for file and directory handling)

---

## 📁 Project Structure

```
regression-testing-tool/
│
├── versions/
│   ├── v1.py              # Old version of software
│   └── v2.py              # New version of software
│
├── testcases/
│   └── input.txt          # Test input data
│
├── reports/
│   └── report.txt         # Generated output report
│
└── regression_tool.py     # Main script
```

---

## 🚀 Features

* Executes multiple software versions automatically
* Compares outputs line-by-line
* Generates PASS/FAIL results
* Produces a detailed report file
* Beginner-friendly and easy to extend

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```
git clone https://github.com/your-username/regression-testing-tool.git
cd regression-testing-tool
```

### Step 2: Run the Script

```
python regression_tool.py
```

> If `python` does not work:

```
python3 regression_tool.py
```

---

## 📊 Sample Output

### Terminal Output

```
Test 1: FAIL
Input: Hello World
Version1 Output: HELLO WORLD
Version2 Output: hello world
----------------------------------------
```

### Report File Output

The results are saved in:

```
reports/report.txt
```

---

## 🔍 How It Works

1. The tool creates two versions of a sample program
2. Reads test inputs from a file
3. Executes both versions using the same input
4. Captures outputs using Python’s subprocess module
5. Compares results and marks:

   * PASS → Outputs match
   * FAIL → Outputs differ
6. Saves detailed results into a report file

---

## 💡 Use Cases

* Software version comparison
* Continuous integration testing
* Debugging new updates
* Academic and learning purposes

---

## 🔮 Future Enhancements

* Graphical User Interface (GUI) using Tkinter
* Web-based dashboard using Flask
* Support for multiple programming languages
* Integration with CI/CD pipelines (GitHub Actions)
* Export reports to PDF/Excel

---

## 📈 Advantages

* Saves time in manual testing
* Improves accuracy of bug detection
* Easy to modify and extend
* Lightweight and efficient

---


