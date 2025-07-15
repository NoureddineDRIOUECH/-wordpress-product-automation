# WordPress Product Automation

This project is a Python script that automates the process of adding products to a WordPress website, particularly those using WooCommerce. It reads product data from JSON files and uses it to create new products.

## Features

*   **Automated Product Creation:** Automatically adds products to your WordPress site.
*   **Data-Driven:** Reads product information from JSON files, making it easy to manage your product data.
*   **Session Management:** Uses a `requests.Session` to maintain a connection with the WordPress site.

## Getting Started

### Prerequisites

*   Python 3.6+
*   `requests` library (`pip install requests`)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/wordpress-product-automation.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd wordpress-product-automation
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Configure your WordPress credentials:**
    Update the `connection.py` file with your WordPress username, password, and the URL of your website's admin login page.

2.  **Prepare your product data:**
    Create JSON files with your product data. You can use the existing `115-compact_data.json` and `151-onduleur-off-line_data.json` files as a template.

3.  **Run the script:**
    ```bash
    python main.py
    ```

## How It Works

The script is divided into several modules:

*   `connection.py`: Handles the connection to your WordPress site.
*   `createProduct.py`: Contains the logic for creating a new product.
*   `fillingForm.py`: Fills in the product creation form with the data from the JSON files.
*   `main.py`: The main script that orchestrates the entire process.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.
