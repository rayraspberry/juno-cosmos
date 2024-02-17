# What's this for?

`juno-active-set-mintscan-scrape.py` will take the saved html from the `https://dev.mintscan.io/juno/validators` webpage and produce a Comma Separated version of most of the data including the validator `junovalop` address which was the purpose of developing the code
This code was created from a series of prompts to and a conversation with ChatGPT.

The `active_Set.txt` and `validator_set_ActiveAndInactive` files were created using a different process with `https://jsonquery.co.uk/`

## How to use `juno-active-set-mintscan-scrape.py`

To install Python on an `apt` package manager based Linux distribution like Debian or Ubuntu, you can follow these steps:

Update Package Index: Before installing any new software, it's a good practice to update the local package index. Open a terminal and run:

`sudo apt update`

Install Python: Debian typically comes with Python pre-installed, but you may want to ensure you have the latest version or a specific version installed. To install Python 3, you can run:

`sudo apt install python3`

Install pip (Python Package Installer): Pip is a package management system used to install and manage software packages written in Python. You can install it by running:

`sudo apt install python3-pip`

Install BeautifulSoup4 and Requests: These are Python libraries required for web scraping. You can install them using pip:
`sudo pip3 install beautifulsoup4 requests`

Write and Run the Script: Now, you can write your Python script as mentioned earlier and execute it using the Python interpreter. Create a new file (e.g., scrape.py) and paste the code into it. Then, run the script using Python 3:

`python3 juno-active-set-mintscan-scape.py junoval.html -o output-file.csv`
