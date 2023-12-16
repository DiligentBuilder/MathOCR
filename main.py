# Aaron Wang
# Math OCR
# ECE Junior Design Project #3

from PIL import Image
from pix2tex.cli import LatexOCR

from pix2tex.api import app

from keras.preprocessing import image

from latex2sympy2 import latex2sympy, latex2latex

from sympy import *

import skimage as ski

import asyncio

print(ski.__version__)

import imageio as iio


def preprocessimage(img):
    # Downsampling the image
    preprocessedimg = ski.measure.block_reduce(img)
    return preprocessedimg


# function that exports the SymPy code stored into a string variable and creates a Python source code file
# Saves file of SymPy code wherever the user desires
def exportSymPyCode(SymPycode):
    print("Exporting the SymPy code string to a Python file...")

    print("The file will be saved as \"Python_SymPy_Code_File.py\" in the Output folder")

    with open("./Output/Python_SymPy_Code_File.py", "w") as file1:
        # writing SymPy code string to file
        file1.write(str(SymPycode))


# This function exports the LATEX code that is outputted from the Latex OCR to a LATEX file
def exportLATEXCode(LATEXcode):
    print("Exporting the LATEX code string to a LATEX file...")

    print("The file will be saved as \"Latex_Code_File.tex\" in the Output folder")

    with open("./Output/LATEX_Code_File.tex", "w") as file2:
        # Writing LATEX code string to file

        file2.write(str(LATEXcode))


# Make the user select an option from a menu of options

# Returns the menu option
def menu():
    # display the menu and the menu options

    print("Menu")

    print("Here are the currently available menu options:")

    print("1. Perform OCR on the math image and display the predicted math and LATEX code")

    print("2. Convert LATEX code prediction into SymPy code")

    print("3. Do arithmetic using the math image and solve the arithmetic")

    print("4. Convert LATEX code prediction to SymPy code and export")

    print("5. Convert LATEX code prediction to MATLAB code and export")

    print("6. Export the direct LATEX code that is the output of the Math Image OCR")

    print("Which menu option would you like to select?")

    number = input("Enter a number: ")

    # get which menu option the user would like to select
    # get the user's input

    return number


# get the path to the input image of the math that the user would like to use
def getmathinputimage():
    print("Please enter the file path for the input math image")

    print("This should be a clear image that has clear math on it")

    print("For example, this could be an image of arithmetic, mathematical equation, mathematical expression, etc.")

    path = input("File path: ")

    return path


# calculate the arithmetic using the SymPy code converted from the LATEX code
# predicted from the math image that the user inputted

# Using the numerical evaluation in SymPy to calculate the arithmetic expression
def calculateArithmetic(SymPyCode):
    answer = N(SymPyCode)

    print("The answer to the arithmetic (according to the LATEX prediction) is")
    print(answer)

    print("Would you like to export the answer of the SymPy numerical evaluation it to a .txt file?")

    response = input("Y/N ")

    # read in char from the user

    if response == "Y" or response == "y":
        # Write the answer to an output file
        with open("./Output/answer.txt", "w") as file3:
            # writing the answer string to a file
            file3.write(str(answer))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Keep running the loop as long as the user would like until they quit

    # Implemented with infinite loop and break when the user decides to quit

    # Starts out with no prediction
    prediction = ""

    while True:

        # Ask the user what they would like to do
        # Ask the user to select an option from the menu
        userOption = menu()


        if userOption == '1':
            # Get the file path of the math image that the user would like to use as the input image
            userFilePath = getmathinputimage()

            # Read in the image
            # JPEG format seems to work the best when inputting the images into the Math OCR
            # image = iio.imread("MathImage.jpg")
            # Downsample the image

            # Using the Latex OCR library
            img = Image.open(userFilePath)
            model = LatexOCR()

            # Display the LATEX code
            print("Prediction is: ")
            print(model(img))

            prediction = model(img)
            # print(asyncio.run(app.predict(img1)))

            # Display the output image that is produced by the LATEX code when it is run

        img2 = Image.open('C:/Users/aaron/Downloads/ArithmeticMathOCRLowQuality.png').convert('RGB')

        preprocessedImage = preprocessimage(image.img_to_array(img2))

        model = LatexOCR()
        # print(asyncio.run(app.predict(preprocessedImage)))

        # prediction = app.predict(preprocessedImage)

        # print("Prediction is")

        # print(asyncio.run(prediction))

        # Export the LATEX code option
        if userOption == '6':
            if prediction == '':
                print("Sorry, no LATEX code prediction yet. Please input an image and run the OCR first. ")
            else:
                exportLATEXCode(prediction)

        # Convert LATEX code prediction to Sympy
        if userOption == '2':
            if prediction == '':
                print("Sorry, no LATEX code prediction yet. Please input an image and run the OCR first. ")
            else:
                # If there is a LATEX code prediction, convert it to SymPy
                prediction_sympy = latex2sympy(str(prediction))
                print("The Prediction, converted to SymPy code, is:")
                print(prediction_sympy)

        # Convert LATEX code prediction to Sympy AND export
        if userOption == '4':
            # Check if there is a LATEX code prediction
            if prediction == '':
                print("Sorry, no LATEX code prediction yet. Please input an image and run the OCR first. ")
            else:
                # if there is a LATEX code prediction, convert it to SymPy AND export
                prediction_sympy = latex2sympy(str(prediction))
                print("The Prediction, converted to SymPy code, is:")
                print(prediction_sympy)

                # Exporting
                exportSymPyCode(prediction_sympy)

    # Code for Testing purposes

    # tex = r"\frac{d}{dx}(x^{2}+x)"
    # # Or you can use '\mathrm{d}' to replace 'd'
    # x = latex2sympy(tex)
    # # => "Derivative(x**2 + x, x)"
    # y = latex2sympy(tex)
    # # => "2 x + 1"
    #
    # print(x)
    # print(y)
    #
    # exportSymPyCode(x)

        # Ask the user if they would like to quit
        print("Would you like to quit?")
        quit = input("Y/N ")

        if quit == 'Y' or quit == 'y':
            break



