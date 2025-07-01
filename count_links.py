import re

def count_github_links(filepath):
    """Counts the number of unique GitHub repository links in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find GitHub repo links (e.g., https://github.com/user/repo)
        # This will capture the user/repo part of the URL.
        regex = r"https://github\.com/([a-zA-Z0-9\-\_]+/[a-zA-Z0-9\-\_]+)"
        
        matches = re.findall(regex, content)
        
        # Use a set to store unique repository links
        unique_repos = set(matches)
        
        return len(unique_repos)

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    readme_path = "/home/cw1a/Repos/webscrape/readme.md"
    link_count = count_github_links(readme_path)
    print(f"Found {link_count} unique GitHub repository links.")
