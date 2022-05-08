import requests
import os

os.chdir("MaskDetectionData/classifications/Pet")

for i in range(0, 100):
    random_cat = requests.get("https://thatcopy.pw/catapi/rest/").json()["url"]
    # Download dog pictures picture to pet folder using curl
    os.system(
        f"curl {random_cat} -o cat{i}.jpg 2> /dev/null"
    )  # Redirect all curl output to null
    print(f"Downloading Cat #{i}")
print("Done!")
