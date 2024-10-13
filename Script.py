import os
import requests


# This is the list of the countries i will be downloading flags for
countries = [
    "us", "ca", "gb", "de", "fr", "jp", "cn", "in", "br", "ru", "au", "za", "mx",
    "kr", "it", "es", "se", "no", "ch", "nl", "tr", "pl", "be", "ar", "cl", "pt",
    "sa", "eg", "ir", "th", "vn", "nz", "id", "ph", "my", "sg", "bd", "ng", "ke",
    "ua", "at", "dk", "fi","ps","gr", "ie", "hu", "cz", "ro", "sk"
]

# This is the path of the file where flags are saved
save_dir = r"C:\Datasets\Flags"

base_url = "https://flagcdn.com/w320/"



# This  is the function i used to download the flags, it goes by completing the URL and use the .png extension to save images


def download_flag(country_code):

    try:
        url = f"{base_url}{country_code}.png"


        response = requests.get(url, stream=True)

        if response.status_code == 200:

            filepath = os.path.join(save_dir, f"{country_code}.png")
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded flag for {country_code.upper()}")
        else:
            print(f"Failed to download flag for {country_code.upper()}")

    except Exception as e:
        print(f"An error occurred: {e}")



for country in countries:
    download_flag(country)

print("Download completed!")
