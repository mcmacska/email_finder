# Email finder

Email finder checks if a list of emails exists with the Whois API, via SMTP connection checks.

# Prerequisites

[Python 3](https://www.python.org/downloads/)

Register at the [whoisxmlapi](https://user.whoisxmlapi.com/products) website and get your API key.



# Install

    git clone https://github.com/mcmacska/email_finder.git
    cd email_finder/

# Usage
Write the email adresses in the emails_to_search.txt file line-by-line.

    python3 main.py API_KEY
