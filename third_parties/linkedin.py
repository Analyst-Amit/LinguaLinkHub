import os
import requests


def clean_json_response(data):
    cleaned_data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if cleaned_data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    cleaned_data = f'"""{cleaned_data}"""'

    return cleaned_data


def scrape_linkedin_profile(linkedin_profile_url: str = None):
    """
    Scrape information from linkedin, Provided a linkedin url.
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url["output"]}, headers=header_dic
    )

    if response.status_code == 200:
        return clean_json_response(response.json())
    else:
        print("Error fetching URL")
