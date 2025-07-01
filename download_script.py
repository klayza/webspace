import requests
import os

def download_file(url, folder):
    """Downloads a file from a URL and saves it to a folder."""
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = url.split('/')[-1]
        filepath = os.path.join(folder, filename)

        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Successfully downloaded {filename} to {folder}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

if __name__ == "__main__":
    # The URL from the previous turn is a github page, let's get the raw content.
    file_url = "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md"
    download_folder = "/home/cw1a/Repos/webscrape"
    download_file(file_url, download_folder)
