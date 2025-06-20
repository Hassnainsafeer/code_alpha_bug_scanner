import os

def scan_file(file_path):
    dangerous_keywords = ["eval(", "exec(", "os.system", "subprocess", "password=", "secret", "token"]
    issues_found = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            for keyword in dangerous_keywords:
                if keyword in line:
                    issues_found.append((idx + 1, line.strip(), keyword))

    return issues_found

def scan_directory(path):
    print(f"Scanning directory: {path}")
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith('.py'):
                full_path = os.path.join(root, name)
                print(f"\nChecking: {full_path}")
                issues = scan_file(full_path)
                if issues:
                    for line_no, code, keyword in issues:
                        print(f"[!] Line {line_no}: Found '{keyword}' ➜ {code}")
                else:
                    print("No issues found.")

# Set your path here
target_path = "./"  # Current directory
scan_directory(target_path)
