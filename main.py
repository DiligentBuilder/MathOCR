# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image
from pix2text.cli import LatexOCR

from pix2tex.api import app

from keras.preprocessing import image

from latex2sympy2 import latex2sympy, latex2latex

import skimage as ski
print(ski.__version__)

import imageio as iio


def preprocessimage(img):
    # Downsampling the image
    preprocessedimg = ski.measure.block_reduce(img)
    return preprocessedimg

# function that exports the SymPy code stored into a string variable and creates a Python source code file
# Saves file of SymPy code wherever the user desires
def exportSymPyCode(SymPycode):
    with open("Python_SymPy_Code_File.py", "w") as file1:
        # writing SymPy code string to file
        file1.write(str(SymPycode))

# This function exports the LATEX code that is outputted from the Latex OCR to a LATEX file
def exportLATEXCode(LATEXcode):
    with open("LATEX_Code_File.tex", "w") as file2:
        # Writing LATEX ode string to file
        file2.write(str(LATEXcode))






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read in the image
    # JPEG format seems to work the best when inputting the images into the Math OCR
    #image = iio.imread("MathImage.jpg")
    # Downsample the image



    # Using the Latex OCR library
    img1 = Image.open('C:/Users/aaron/Downloads/ArithmeticMathOCRLowQuality.jpg')
    img2 = Image.open('C:/Users/aaron/Downloads/ArithmeticMathOCRLowQuality.jpg').convert('RGB')
    model = LatexOCR()
    print(app.predict(img1))

    preprocessedImage = preprocessimage(image.img_to_array(img2))

    model = LatexOCR()
    print(app.predict(preprocessedImage))

    prediction = app.predict(preprocessedImage)

    exportLATEXCode(prediction)

    prediction_sympy = latex2sympy(prediction)




    tex = r"\frac{d}{dx}(x^{2}+x)"
    # Or you can use '\mathrm{d}' to replace 'd'
    x = latex2sympy(tex)
    # => "Derivative(x**2 + x, x)"
    y = latex2latex(tex)
    # => "2 x + 1"

    print(x)
    print(y)

    exportSymPyCode(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
