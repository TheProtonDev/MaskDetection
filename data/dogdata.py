import requests
import os

os.chdir('MaskDetectionData/classifications/Pet')

for i in range(0, 100):
    random_dog = requests.get("https://dog.ceo/api/breeds/image/random").json()['message']
    # Download dog pictures picture to pet folder using curl
    os.system(f'curl {random_dog} -o dog{i}.jpg 2> /dev/null')  # Redirect all curl output to null
    print(f"Downloading Dog #{i}")
print("Done!")
