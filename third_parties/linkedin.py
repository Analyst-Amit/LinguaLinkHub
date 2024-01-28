import os
import requests


def clean_text(raw_text):
    cleaned_text = " ".join(raw_text.split())

    cleaned_text = f'"""{cleaned_text}"""'

    return cleaned_text


def scrape_linkedin_profile(linkedin_profile_url: str = None):
    """
    Scrape information from linkedin, Provided a linkedin url.
    """
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url["output"]}, headers=header_dic
    # )
    response = requests.get(
        "https://gist.githubusercontent.com/Analyst-Amit/9932c9d6f7dc35abd58930fde87ecc62/raw/ee3af7560505653b0d59a5b85f5dddd783baab2f/amitgupta.md"
    )

    if response.status_code == 200:
        return clean_text(response.text)
    else:
        print("Error fetching URL")
