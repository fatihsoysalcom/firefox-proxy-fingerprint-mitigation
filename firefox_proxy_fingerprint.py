import requests
import os

# --- Configuration ---
# Replace with your actual proxy details
PROXY_USERNAME = os.environ.get('PROXY_USERNAME', 'your_username')
PROXY_PASSWORD = os.environ.get('PROXY_PASSWORD', 'your_password')
PROXY_HOST = os.environ.get('PROXY_HOST', 'your_proxy_host')
PROXY_PORT = os.environ.get('PROXY_PORT', 'your_proxy_port')

# The target URL to fetch
TARGET_URL = 'https://httpbin.org/ip'

# --- Proxy Setup ---
# Construct the proxy URL with authentication
# This format is common for requests library with username/password proxies
proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"

# Dictionary for proxy settings
proxies = {
    "http": proxy_url,
    "https": proxy_url,
}

# --- Main Logic ---
def fetch_with_proxy(url, proxy_settings):
    """Fetches a URL using the provided proxy settings."""
    try:
        # Make the HTTP GET request, passing the proxy configuration
        # The 'proxies' argument tells the requests library to route traffic through the specified proxies.
        # This is where the browser's (or in this case, the script's) network request is directed through the proxy.
        response = requests.get(url, proxies=proxy_settings, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print(f"Attempting to fetch {TARGET_URL} using proxy...")

    # Call the function to fetch the data using the configured proxy
    # The key aspect here is that the `requests` library handles the proxy authentication and routing.
    # For Firefox, this would be configured in its network settings, and the browser itself would make these requests.
    # This script simulates the network behavior.
    ip_info = fetch_with_proxy(TARGET_URL, proxies)

    if ip_info:
        print("Successfully fetched IP information:")
        print(f"Original IP (likely your local IP if not running in a container): {ip_info.get('origin')}")
        print("\nNote: For actual Firefox fingerprinting mitigation, you would configure these proxy settings within Firefox's network preferences.")
        print("This script demonstrates the network routing aspect, not the browser-specific fingerprinting details.")
    else:
        print("Failed to fetch IP information.")
