# Personalized Order Status Email Generator

This application generates personalized and interactive emails to provide order status updates for Shopify orders. It uses the Shopify API to retrieve order details and employs an AI agent from Lyzr's Agent Framework to compose the emails.

## Features

- Retrieve order details from Shopify
- Generate interactive emails for order status updates
- User-friendly interface with a dropdown to select order numbers

## Requirements

- Python 3.7+
- Shopify API credentials
- Lyzr API credentials
- Solara

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Shopify and Lyzr credentials:
    ```sh
    SHOPIFY_TOKEN=<your_shopify_token>
    SHOPIFY_MERCHANT=<your_shopify_merchant>
    ```

## Usage

1. Activate your virtual environment if not already activated:
    ```sh
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

2. Run the application:
    ```sh
    solara run app.py
    ```

3. Open your web browser and navigate to the provided local server address.

4. Select an order number from the dropdown and click the "Generate" button to generate the interactive email.

## Project Structure

- `main.py`: The main application script.
- `agents.py`: Contains the functions to create the environment, agent, and task using Lyzr's Agent Framework.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: File containing environment variables for Shopify and Lyzr API credentials (not included in the repository).

## Dependencies

- solara
- solara.lab
- python-dotenv
- ShopifyAPI
- Lyzr's Agent Framework

## Example

To run the application, make sure your `.env` file is correctly configured with your Shopify and Lyzr credentials. Start the application and follow the usage instructions to generate personalized order status emails.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Solara](https://github.com/widgetti/solara) for the UI components
- [Shopify API](https://shopify.dev/api) for order retrieval
- [Lyzr](https://docs.lyzr.ai/introduction) for the Agent Framework
