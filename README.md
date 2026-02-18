# OrangeHRM UI Automation (Python + Selenium + Behave BDD)

This repository contains a UI test automation project for the OrangeHRM demo application using **Python**, **Selenium WebDriver**, and **Behave (BDD with Gherkin)**.

My goal is to build a reusable automation framework (not just one-off scripts). I’m currently focusing on building solid foundations and learning BDD practices as I go. The BDD layer is intentionally kept simple at this stage and will be improved as the project grows.

**Target App (Demo):**
- URL: https://opensource-demo.orangehrmlive.com/

---

## Project Goals

- Build a maintainable UI automation framework using Page Object Model (POM)
- Use **Behave + Gherkin** to express scenarios in a readable format
- Centralize browser setup/teardown in Behave hooks (`environment.py`)
- Keep configuration outside the code (environment variables)
- Prepare the project for CI execution (later: reports, screenshots on failure, artifacts)

---

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- Behave (BDD)
- Pytest (present in the project history; current approach is Behave-first)
- python-dotenv (optional depending on how you manage env vars)

---

## Repository Structure (High Level)

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
├── tests/                          # Legacy / optional (Pytest-based)
├── requirements.txt
├── pytest.ini                      # Optional for Pytest (not required for Behave)
└── README.md
Note: At this stage, the main test execution path is Behave (Gherkin).
Some Pytest files may still exist from earlier experiments; I’m cleaning this up as the framework matures.

Setup
1) Create and activate a virtual environment
Windows (PowerShell):

bash
Copy
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS/Linux:

bash
Copy
python -m venv .venv
source .venv/bin/activate
2) Install dependencies
bash
Copy
pip install -r requirements.txt
Configuration (Environment Variables)
This project reads configuration from environment variables (recommended approach for CI and security).

Example variables:

ORANGE_URL
ORANGE_USERNAME
ORANGE_PASSWORD
Option A: Use a .env file locally (recommended for development)
Create a .env file in the project root (do not commit it):

env
Copy
ORANGE_URL=https://opensource-demo.orangehrmlive.com/
ORANGE_USERNAME=Admin
ORANGE_PASSWORD=admin123
Make sure .env is in .gitignore.

Option B: Export environment variables directly (useful for CI)
Windows PowerShell:

powershell
Copy
$env:ORANGE_URL="https://opensource-demo.orangehrmlive.com/"
$env:ORANGE_USERNAME="Admin"
$env:ORANGE_PASSWORD="admin123"
macOS/Linux:

bash
Copy
export ORANGE_URL="https://opensource-demo.orangehrmlive.com/"
export ORANGE_USERNAME="Admin"
export ORANGE_PASSWORD="admin123"
Running the Tests (Behave)
Run all feature files:

bash
Copy
behave
Run a specific feature:

bash
Copy
behave features/login.feature
What happens per scenario?
features/environment.py opens the browser before each scenario
The scenario steps run using features/steps/*.py
The browser closes after each scenario automatically
Current Coverage (Phase 1)
Login feature (BDD):

Successful login (valid credentials)
Unsuccessful login (invalid credentials)
Empty fields validation (“Required” messages)
The .feature file uses a Scenario Outline with an Examples table to run the same scenario with multiple credential sets.

Notes on BDD (Learning in Progress)
I am actively learning how to write better Gherkin and step definitions. My current focus is:

Keeping steps reusable and readable
Avoiding duplicated Selenium code in steps (pushing locators/actions into Page Objects)
Improving assertions with explicit waits and clearer validations
As the project evolves, I plan to improve:

Reporting (HTML/Allure)
Automatic screenshots on failure
Better tagging and selective execution
CI pipeline integration (GitHub Actions)
Next Steps (Phase 2)
Planned direction:

Expand coverage to core OrangeHRM flows (starting with PIM / employee management)
Add failure artifacts (screenshots) in after_step hook
Improve framework maintainability (clean structure, remove legacy tests, consistent naming)
Disclaimer
This project targets the public OrangeHRM demo site. The credentials are demo credentials and used only for educational/testing purposes.

Author
Maintained by: Sergio Solano - Automation Engineer
