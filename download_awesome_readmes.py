import os
import re
import requests
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
AWESOME_README_URL = "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md"
README_DIR = "awesome_readmes"
MAIN_README_PATH = os.path.join(README_DIR, "awesome_main_readme.md")

def download_file(url, local_path):
    """Downloads a file from a URL to a local path."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        with open(local_path, 'wb') as f:
            f.write(response.content)
        logging.info(f"Successfully downloaded {url} to {local_path}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
        return False

def extract_github_links(content):
    """Extracts GitHub repository links from the given content."""
    # Regex to find GitHub repo links in the format (https://github.com/user/repo)
    github_link_pattern = re.compile(r'https\://github\.com/([a-zA-Z0-9\-\_]+/[a-zA-Z0-9\-\_]+)')
    links = github_link_pattern.findall(content)
    # We use a set to store unique links to avoid duplicates
    unique_links = set(links)
    logging.info(f"Found {len(unique_links)} unique GitHub repository links.")
    return list(unique_links)

def main():
    """Main function to orchestrate the download and extraction process."""
    # Create the directory for READMEs if it doesn't exist
    if not os.path.exists(README_DIR):
        os.makedirs(README_DIR)
        logging.info(f"Created directory: {README_DIR}")

    # 1. Download the main awesome/readme.md file
    logging.info("Downloading the main awesome readme.md file...")
    if not download_file(AWESOME_README_URL, MAIN_README_PATH):
        logging.error("Could not download the main awesome readme.md. Aborting.")
        return

    # 2. Extract GitHub repo links from the file
    with open(MAIN_README_PATH, 'r', encoding='utf-8') as f:
        main_readme_content = f.read()
    
    github_repos = extract_github_links(main_readme_content)
    
    if not github_repos:
        logging.warning("No GitHub links found in the main readme.md file.")
        return

    # 3. Download each repository's README.md
    downloaded_count = 0
    for repo in github_repos:
        # Construct the raw README URL. We try a few common README filenames.
        possible_readme_names = ["README.md", "readme.md", "ReadMe.md"]
        repo_readme_url = ""
        for name in possible_readme_names:
            # Check which variation of the readme name is correct
            test_url = f"https://raw.githubusercontent.com/{repo}/master/{name}"
            try:
                res = requests.head(test_url, timeout=5)
                if res.status_code == 200:
                    repo_readme_url = test_url
                    break
            except requests.exceptions.RequestException:
                continue # Try the next name

        if not repo_readme_url:
            # If master branch didn't work, try main branch
            for name in possible_readme_names:
                test_url = f"https://raw.githubusercontent.com/{repo}/main/{name}"
                try:
                    res = requests.head(test_url, timeout=5)
                    if res.status_code == 200:
                        repo_readme_url = test_url
                        break
                except requests.exceptions.RequestException:
                    continue
        
        if not repo_readme_url:
            logging.warning(f"Could not find a README for repo: {repo}")
            continue

        # Define local path for the repo's README
        repo_name = repo.replace('/', '_')
        local_readme_path = os.path.join(README_DIR, f"{repo_name}.md")

        # Download the repo's README
        if download_file(repo_readme_url, local_readme_path):
            downloaded_count += 1

    logging.info(f"Finished. Downloaded {downloaded_count}/{len(github_repos)} README files.")

if __name__ == "__main__":
    main()
