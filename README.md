# OrangeHRM UI Automation (Python + Selenium + Behave BDD)

This repository contains a UI test automation project for the OrangeHRM demo application using **Python**, **Selenium WebDriver**, and **Behave (BDD with Gherkin)**.

My goal is to build a reusable automation framework. I’m currently focusing on building solid foundations and learning BDD practices as I go. The BDD layer is intentionally kept simple at this stage and will be improved as the project grows.

**Target App:**
- URL: https://opensource-demo.orangehrmlive.com/
---
## Project Goals

- Build a maintainable UI automation framework using Page Object Model (POM)
- Use **Behave + Gherkin** to express scenarios in a readable format
- Centralize browser setup/teardown in Behave hooks (`environment.py`)
- Keep configuration outside the code (environment variables)
- Prepare the project for CI execution (Soon: reports, screenshots on failure)

---

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- Behave (BDD)
- Pytest (present in the project history; current approach is Behave-first)
- python-dotenv (optional depending on how you manage env vars)

---
## Repository Structure

```text
.
├── src/
│   ├── core/
│   │   ├── driver_factory.py       # WebDriver creation/config
│   │   ├── base_page.py            # Common UI actions + waits
│   │   └── config.py               # Environment config helpers
│   └── pages/
│       └── login_page.py           # Page Object for Login page
│
├── features/
│   ├── environment.py              # Behave hooks (setup/teardown per scenario)
│   ├── login.feature               # Gherkin scenarios for login
│   └── steps/
│       └── login_steps.py          # Step definitions mapped to Gherkin steps
│
├── requirements.txt
└── README.md

```

Setup
1) Create and activate a virtual environment
Windows (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```
pip install -r requirements.txt
```

---
## Configuration

This project reads configuration from environment variables

## Running the Tests

Run all Feature files:

```
behave
```
Run a specific feature:

```
behave features/login.feature
```
## What happens per scenario?

features/environment.py opens the browser before each scenario
The scenario steps run using features/steps/*.py
The browser closes after each scenario automatically

## Disclaimer

This project targets the public OrangeHRM demo site. The credentials are demo credentials and used only for educational/testing purposes.


## Author

Maintained by: Sergio Solano - Automation Engineer

