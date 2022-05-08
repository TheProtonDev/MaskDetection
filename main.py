#!/usr/bin/python3
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os
from authorlib import AuthorLib
import colorama

while True:  # Start a loop for the main program
    # Load the model
    model = load_model("keras_model.h5")

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    os.system("clear")  # Erase all the output from loading the model
    AuthorLib("TheProtonDev", "Mask Detection Algorithm", "MAGENTA").output()
    
        
    def listImages():
        raw_cur_dir_contents = list(os.listdir())
        valid_cur_dir = []
        valid_images = [".png", ".jpg", ".jpeg", ".webp"]
        for file in raw_cur_dir_contents:
            for extension in valid_images:
                if file.find(extension) != -1:
                    valid_cur_dir.append(file)
        return valid_cur_dir

    def fileSelector():
        while True:
            filename = input(
                "File To Select (press enter to list files in directory or enter part of a filename) to search > "
            )
            if type(filename) == str:
                if (
                    filename.find(".") == -1
                ):  # If the user didn't enter a file extension
                    potential_matches = []
                    cur_dir_contents = listImages()
                    for file in cur_dir_contents:
                        if (
                            file.find(filename) != -1
                        ):  # If the part of the file the user entered matches part of the file name then add it to a list of potential matches
                            potential_matches.append(
                                file
                            )  # Add the file to the list of potential matches
                    counter = 0
                    for match in potential_matches:
                        counter += 1
                        print(f"#{counter}| {match}")
                    while True:
                        selector = input("Match To Select > ")
                        if selector == "":
                            break
                            continue
                        if selector != "":  # If not blank response
                            selected_match = potential_matches[int(selector) - 1]
                            return selected_match
                            break
                        else:
                            continue
                else:
                    print(os.path.exists(filename))
                    if os.path.exists(filename):
                        return filename
                    else:
                        os.system("clear")
                        AuthorLib("Zaden Maestas", "Mask Detection", "MAGENTA").output()
                        continue  # Restart loop

    filename = fileSelector()

    print(f"Selected {filename}")
    image = Image.open(filename)

    show = image.show()

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # Calculate detections
    mask = int(prediction[0][0] * 100)
    no_mask = int(prediction[0][1] * 100)
    pet = int(prediction[0][2] * 100)
    if (
        pet < 90
    ):  # The pet detection is extremely accurate for cats and dogs so if it is lower than 90%, completely ignore it
        print(
            colorama.Fore.WHITE + f"Analysis Output:",
            f"\nRaw Prediction: {prediction}\n",
            colorama.Fore.GREEN + f"Mask: {mask}%\n",
            colorama.Fore.RED + f"No Mask: {no_mask}%" + colorama.Fore.RESET,
        )
        if no_mask > 70:
            print(
                colorama.Fore.RED + "Final Determination: No Mask" + colorama.Fore.RESET
            )
        if mask > 70:
            print(
                colorama.Fore.GREEN
                + "Final Determination: Wearing Mask"
                + colorama.Fore.RESET
            )
        else:
            if pet < 90 and no_mask == 0:
                print(
                    colorama.Fore.GREEN
                    + "Final Determination: Wearing Mask"
                    + colorama.Fore.RESET
                )
    else:
        print(
            colorama.Fore.WHITE + f"Analysis Output:",
            f"\nRaw Prediction: {prediction}\n",
            colorama.Fore.GREEN + f"Mask: {mask}%\n",
            colorama.Fore.RED + f"No Mask: {no_mask}%\n",
            colorama.Fore.YELLOW + f"Pet: {pet}" + colorama.Fore.RESET,
        )
        print(colorama.Fore.YELLOW + "Final Determination: Pet" + colorama.Fore.RESET)
    retry = input("Press enter to retry or type 'exit' to exit > ")
    if retry == "":
        continue
    elif retry == "exit":
        ids = os.system('pgrep "display"')
        os.system(f"kill {ids}")
        exit()
