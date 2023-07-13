import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(profile_url):
    # Send a GET request to the LinkedIn profile URL
    response = requests.get(profile_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information from the profile page
    name = soup.select_one('.pv-top-card-section__name').text.strip()
    about = soup.select_one('.pv-about-section .pv-about-section__summary-text').text.strip()
    job_title = soup.select_one('.pv-top-card-section__headline').text.strip()
    # Extract other relevant information as needed

    # Return the extracted data as a dictionary or any desired format
    profile_data = {
        'name': name,
        'about': about,
        'job_title': job_title,
        # Add more fields as needed
    }
    return profile_data

# Example usage
profile_url = 'https://www.linkedin.com/in/srijan-kamboj-74b528246/'
profile_data = scrape_linkedin_profile(profile_url)
print(profile_data)
