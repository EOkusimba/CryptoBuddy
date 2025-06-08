#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Predefined Crypto Data
# This dictionary stores our cryptocurrency data.
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9/10
    },
    "Algorand": {
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 9.5/10
    }
}



# In[ ]:


# 2. Chatbot Logic and Advice Rules
def get_cryptobuddy_response(user_query):
    """
    Processes the user's query and returns a response from CryptoBuddy.
    """
    user_query = user_query.lower()  # Make the query case-insensitive

    # Rule for help
    if "help" in user_query:
        return (
            "Of course! You can ask me questions like:\n"
            "- 'Which crypto should I buy for long-term growth?'\n"
            "- 'What is the most sustainable coin?'\n"
            "- 'Which crypto is trending up?'\n"
            "- 'Which crypto do you provide advice on'"
        )

    # Rule for advice
    if "advice" in user_query or "advise" in user_query:
        response = "Here are the coins and their sustainability scores:\n"
        for coin, data in crypto_db.items():
            response += f"- {coin}: {data['sustainability_score'] * 10}/10\n"
        return response

    # Rule for sustainability
    if "sustainable" in user_query or "eco-friendly" in user_query:
        # Find the coin with the highest sustainability score
        recommendation = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"For sustainability, check out {recommendation}!  It’s eco-friendly and has great potential!"

    # Rule for trending up
    if "trending up" in user_query or "rising" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            return f"The following coins are currently trending up: {', '.join(trending_coins)}."
        else:
            return "None of the coins in my database are currently trending up."

    # Rule for long-term growth (combining profitability and sustainability)
    if "long-term growth" in user_query or "long term" in user_query:
         # Prioritize coins with rising trend, high/medium market cap, and high sustainability
        best_choice = None
        highest_score = -1

        for coin, data in crypto_db.items():
            score = 0
            if data["price_trend"] == "rising":
                score += 3
            if data["market_cap"] in ["high", "medium"]:
                score += 2
            if data["sustainability_score"] > 7/10:
                score += 4

            if score > highest_score:
                highest_score = score
                best_choice = coin

        if best_choice:
            return f"{best_choice} looks promising for long-term growth, with a rising trend and a top-tier sustainability score!"
        else:
            return "I couldn't find a perfect match for long-term growth right now."

    # General query about a specific crypto
    for coin in crypto_db:
        if coin.lower() in user_query:
            details = crypto_db[coin]
            return (f"Here's the scoop on {coin}:\n"
                    f"  - Price Trend: {details['price_trend'].capitalize()}\n"
                    f"  - Market Cap: {details['market_cap'].capitalize()}\n"
                    f"  - Energy Use: {details['energy_use'].capitalize()}\n"
                    f"  - Sustainability Score: {details['sustainability_score'] * 10}/10")

    return "I'm not sure how to answer that. Try asking for 'help' to see what I can do."



# In[3]:


# 3. Test Your Bot - Interactive Session
def start_chatbot():
    """
    Initiates the conversation with CryptoBuddy.
    """
    # Design the Chatbot’s Personality
    bot_name = "CryptoBuddy"
    print("-" * 50)
    print(f"Welcome to {bot_name}!")
    print("-" * 50)
    print("Hey there! Let’s find you a green and growing crypto!\n")
    print("You can ask me things like: \n'Which crypto should I buy for long-term growth?' or '\nWhat's the most sustainable coin?' \n\nType 'help' for more options or 'quit' to exit.")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print(f"{bot_name}: Goodbye! Happy investing!")
            break
        response = get_cryptobuddy_response(user_input)
        print(f"{bot_name}: {response}")

# Main execution block
if __name__ == "__main__":
    start_chatbot()


# In[ ]:




