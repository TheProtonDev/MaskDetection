import selenium
from selenium.webdriver import Firefox
import os
from time import sleep

os.chdir("MaskDetectionData/classifications/No Mask/")

driver = Firefox()

driver.get("https://boredhumans.com/faces.php")

sleep(4)
for i in range(0, 100):
    print(f"Downloading Image: face{i}.png")
    generate_new_face_btn = driver.find_element_by_xpath('//*[@id="generate-text"]')

    generated_img = driver.find_element_by_xpath('//*[@id="model-output"]')
    generated_img.screenshot(f"face{i}.png")
    generate_new_face_btn.click()
    sleep(2)
print("Done!")
