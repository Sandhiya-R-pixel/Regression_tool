import subprocess
import difflib
import os

def run_script(script_name, input_data):
    try:
        result = subprocess.run(
            ["python", script_name],
            input=input_data,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def compare_outputs(output1, output2):
    diff = difflib.unified_diff(
        output1.splitlines(),
        output2.splitlines(),
        lineterm='',
        fromfile='Version1',
        tofile='Version2'
    )
    return "\n".join(diff)

def save_report(diff_result):
    os.makedirs("reports", exist_ok=True)
    with open("reports/report.txt", "w") as f:
        if diff_result:
            f.write("Differences Found:\n\n")
            f.write(diff_result)
        else:
            f.write("No differences found. Outputs are identical.")

def main():
    script_v1 = "version1.py"
    script_v2 = "version2.py"

    print("Enter input for test case:")
    user_input = input()

    output1 = run_script(script_v1, user_input)
    output2 = run_script(script_v2, user_input)

    diff_result = compare_outputs(output1, output2)
    save_report(diff_result)

    print("\n--- Output Version 1 ---")
    print(output1)

    print("\n--- Output Version 2 ---")
    print(output2)

    print("\nReport generated in 'reports/report.txt'")

if __name__ == "__main__":
    main()
