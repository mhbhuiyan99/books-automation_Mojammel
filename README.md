# Books to Scrape Automation Framework

## Project Overview

This project is an automated UI testing framework for the **Books to Scrape** demo website using **Playwright** and **Pytest**.

The framework validates the homepage, book navigation, hyperlinks, images, and book information consistency. It follows the **Page Object Model (POM)** to keep test logic reusable and maintainable.

Website under test:

https://books.toscrape.com

---

# Features

* Homepage validation
* Random book navigation validation
* Book data consistency validation
* Hyperlink validation
* Image validation
* HTML report generation
* Allure result generation
* GitHub Actions CI pipeline
* Page Object Model (POM)
* Reusable automation methods
* No hardcoded waits

---

# Tech Stack

* Python 3.12
* Playwright
* Pytest
* pytest-playwright
* pytest-html
* Allure Pytest
* GitHub Actions

---

# Installation Guide

Clone the repository.

```bash
git clone https://github.com/mhbhuiyan99/books-automation_Mojammel
cd books-automation_Mojammel
```

Create a virtual environment.

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install project dependencies.

```bash
pip install -r requirements.txt
```

Install Playwright browsers.

```bash
playwright install
```

---

# Environment Setup

Required software:

* Python 3.12 or later
* pip
* Git

Recommended:

* VS Code
* Playwright VS Code Extension

Verify installation.

```bash
python --version
pytest --version
playwright --version
```

---

# Running Tests

Run all tests.

```bash
pytest
```

Run tests with console output.

```bash
pytest -s
```

Run a specific test file.

```bash
pytest tests/test_homepage.py
```

---

# Project Structure

```
books-automation_Mojammel
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── pages/
│   └── home_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_book_navigation.py
│   ├── test_book_consistency.py
│   ├── test_images.py
│   └── test_broken_links.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Test Case Coverage

## Homepage Validation

* Verify homepage URL
* Verify page title
* Verify visible headings

---

## Random Book Navigation

* Select random books
* Open each book
* Verify navigation succeeds
* Verify book title is displayed

---

## Book Data Consistency

* Compare homepage book title with detail page title
* Compare homepage price with detail page price

---

## Hyperlink Validation

* Collect unique hyperlinks
* Verify each hyperlink returns HTTP status code 200

---

## Image Validation

* Verify image source exists
* Verify image alt attribute exists
* Verify image class contains `thumbnail`

---

# Report Generation Guide

## HTML Report

Generate HTML report.

```bash
pytest --html=reports/report.html
```

Open the generated report.

```
reports/report.html
```

---

## Allure Report

Generate Allure results.

```bash
pytest --alluredir=allure-results
```

Generate the report.

```bash
allure serve allure-results
```

or

```bash
allure generate allure-results --clean -o allure-report
```

Open the generated report.

```
allure-report/index.html
```

---

# GitHub Actions Setup

The project contains a GitHub Actions workflow located at:

```
.github/workflows/playwright.yml
```

The workflow performs the following steps:

1. Checkout repository
2. Install Python
3. Install project dependencies
4. Install Playwright browsers
5. Execute all tests
6. Generate HTML report
7. Generate Allure results
8. Upload execution artifacts

Uploaded artifacts include:

* HTML Report
* Allure Results

If configured in the future, the workflow can also upload:

* Screenshots
* Videos
* Trace files

---

# Design Decisions

The framework follows the **Page Object Model (POM)** to separate page interactions from test logic.

Key design choices:

* Reusable page methods
* Minimal duplicated code
* Clear test naming
* No hardcoded waits
* Playwright auto-waiting
* Modular test structure

---

# Known Limitations

* The project currently targets the Books to Scrape demo website only.
* Broken link validation requires network connectivity.
* Screenshots, videos, and Playwright trace files are not currently enabled but can be added if required.
* Randomized tests may select different books on different executions while validating the same functionality.

---

# CI/CD Pipeline

The GitHub Actions workflow automatically runs when:

* Code is pushed to the repository.
* A Pull Request is created.

The pipeline automatically:

* Installs dependencies
* Installs Playwright browsers
* Executes all tests
* Generates reports
* Uploads test artifacts

This ensures that every code change is automatically validated before integration.
