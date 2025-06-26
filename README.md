### Library Management

library data stored

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app library_management
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
# Frappe-practice


# Frappe-Practice

# SQL Essentials – Frappe Practice
## 🔹 Normal SQL Path

**File Location:**
/doctype/medical_practice/medical_practice.py

**Message:**  
You can check this via the following link:  
👉 [http://localhost:8001/app/patient-visit](http://localhost:8001/app/patient-visit)

## 🔸 Qubic Query (Stored Procedure)

**File Location:**
/doctype/medical_practice/medical_practice.py

**Message:**  
Check this **in Desk only** (via Frappe backend interface)
