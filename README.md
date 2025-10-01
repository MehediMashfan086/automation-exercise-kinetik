automation_exercise_kinetik/
│
├── pages/ # Page Object Model (POM) classes
│ ├── base_page.py # Base class with common actions
│ ├── home_page.py # Homepage elements & actions
│ ├── products_page.py # Products listing/search page
│ ├── product_page.py # Single product details page
│ ├── cart_page.py # Cart and checkout page
│
├── tests/ # Test cases
│ ├── test_case_1_search_product.py
│ ├── test_case_2_add_to_cart.py
│
├── utils/ # Utility modules
│ ├── config.py # Environment setup (Base URL, browser)
│ ├── test_data.py # Centralized test data
│ ├── logger.py # Logging configuration
│
├── conftest.py # Pytest fixtures (browser setup, teardown)
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation

# Installation Guide

Follow these steps to set up the project locally:

### Clone the Repository

```bash
git clone https://github.com/MehediMashfan086/automation-exercise-kinetik.git
cd automation_exercise_kinetik
```

### Create a Virtual Environment

-> python -m venv venv

### Activate the environment:

# Windows

-> venv\Scripts\activate

# Mac/Linux

-> source venv/bin/activate

### Install Dependencies

-> pip install -r requirements.txt

### Install Playwright Browsers

-> playwright install

### Running Tests

# Run all tests:

-> pytest -v --html=report.html --self-contained-html

# Run a specific test file:

-> pytest tests/test_case_1_search_product.py
-> pytest tests/test_case_2_add_to_cart.py

# Run tests with logs:

-> pytest -s -v

# Run tests in parallel:

-> pytest -n 4

### Reports

# After running tests with:

-> pytest -v --html=report.html --self-contained-html

A report will be generated as report.html in the project root.
Open it in a browser to view detailed results.

### Test Cases

# Test Case 1: Search Products

1. Launch browser
2. Navigate to url
3. Verify homepage is visible
4. Click on Products
5. Verify All Products page is loaded
6. Enter product name in search box
7. Verify Searched Products section appears
8. Verify search results are displayed

# Test Case 2: Add Product to Cart

1. Launch browser
2. Navigate to url
3. Verify homepage is visible
4. Click on the first product (View Product)
5. Verify product detail page is visible
6. Set a custom quantity
7. Add product to cart
8. Open the cart
9. Verify the correct quantity is displayed
