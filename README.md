# CryptoBuddy

CryptoBuddy is an interactive Python chatbot that provides cryptocurrency advice using a predefined dataset. It responds to various user queries - ranging from sustainability-related questions to trending or long-term growth assessments - and even lists coin details along with their sustainability scores.

## Features

- **Predefined Crypto Database**: Contains details for Bitcoin, Ethereum, Cardano, Solana, and Algorand including price trends, market cap, energy use, and sustainability scores.
- **Interactive Chat Interface**: Type commands to receive tailored crypto advice.
- **Diverse Query Handling**:
  - **Help**: Displays guidance on what queries you can ask.
  - **Sustainability**: Recommends the most eco-friendly crypto.
  - **Trending**: Lists coins that are currently trending up.
  - **Long-Term Growth**: Identifies potential coins for long-term growth based on combined criteria.
  - **Crypto Listing**: When asked "Which crypto do you provide advice on", lists all coins along with their sustainability scores.
- **General Coin Details**: Provides a detailed "scoop" on a specified cryptocurrency if mentioned in your query.

## Prerequisites

- Python 3.x

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/CryptoBuddy.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd CryptoBuddy
    ```

## Usage

Run the chatbot using Python:

```bash
python CryptoBuddy.py
```

Upon launching, you'll be greeted with a welcome message along with instructions on how to interact:

- **Type `help`**: To see a list of sample queries.
- **Type `quit`**: To exit the program.
- **Ask specific queries**: Such as "Which crypto should I buy for long-term growth?", "What is the most sustainable coin?", "Which crypto is trending up?", or "Which crypto do you provide advice on" to get different responses.

## How It Works

- The chatbot reads user input via the command line.
- It handles queries by matching keywords and applying rules to select from the cryptocurrency database.
- Special commands yield tailored responses:
  - **Help Message**: Lists available commands.
  - **Sustainable Coin**: Recommends the coin with the highest sustainability score.
  - **Trending Coins**: Displays coins with a rising price trend.
  - **Long-Term Growth**: Computes and suggests the best candidate based on several factors.
  - **Coin Listing**: When asked "Which crypto do you provide advice on", it returns a list of all coins with their sustainability scores.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For significant changes, consider opening an issue to discuss your ideas first.

## License

This project is licensed under the [MIT License](LICENSE).
