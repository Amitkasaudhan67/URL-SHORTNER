# Install necessary packages
# pip install pyshorteners
# pip install pyperclip

import pyshorteners


def generate_short_url(long_url):
    # Create an instance of the Shortener class
    shortener = pyshorteners.Shortener()

    # Generate the shortened URL using TinyURL service
    short_url = shortener.tinyurl.short(long_url)

    # Output the shortened URL
    return short_url


if __name__ == "__main__":
    # Take user input for the long URL
    original_url = input("Please enter the URL you wish to shorten: ")

    # Generate and display the shortened URL
    shortened_url = generate_short_url(original_url)
    print(f"Your shortened URL is: {shortened_url}")
