import subprocess
import os

# -------------------------------
# STEP 1: CREATE SAMPLE FILES
# -------------------------------

def setup_files():
    os.makedirs("versions", exist_ok=True)
    os.makedirs("testcases", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # Version 1
    with open("versions/v1.py", "w") as f:
        f.write("""def process(data):
    return data.upper()

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    print(process(input_data))
""")

    # Version 2 (changed behavior)
    with open("versions/v2.py", "w") as f:
        f.write("""def process(data):
    return data.lower()

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    print(process(input_data))
""")

    # Test cases
    with open("testcases/input.txt", "w") as f:
        f.write("""Hello World
Python Testing
Regression Check""")

# -------------------------------
# STEP 2: RUN SCRIPT FUNCTION
# -------------------------------

def run_script(script_path, input_data):
    try:
        result = subprocess.run(
            ["python", script_path],
            input=input_data,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)

# -------------------------------
# STEP 3: COMPARE OUTPUTS
# -------------------------------

def compare_outputs():
    with open("testcases/input.txt", "r") as f:
        test_cases = f.readlines()

    report = []

    for i, test in enumerate(test_cases):
        test = test.strip()

        out1 = run_script("versions/v1.py", test)
        out2 = run_script("versions/v2.py", test)

        if out1 == out2:
            status = "PASS"
        else:
            status = "FAIL"

        report_line = (
            f"Test {i+1}: {status}\n"
            f"Input: {test}\n"
            f"Version1 Output: {out1}\n"
            f"Version2 Output: {out2}\n"
            f"{'-'*40}\n"
        )

        report.append(report_line)

    # Save report
    with open("reports/report.txt", "w") as f:
        f.writelines(report)

    print("✅ Done! Check 'reports/report.txt'")

# -------------------------------
# MAIN EXECUTION
# -------------------------------

if __name__ == "__main__":
    setup_files()
    compare_outputs()
