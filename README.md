# MathOCR (Reader of Math Images)

ECE 1885 Junior Design Project #3

Does OCR with math and does different functions after the math is recognized

main.py -> main code for the OCR, calls the different libraries that are used to perform the Math OCR tasks.

## Design Overview

In this Junior Design Project, the ultimate goal and purpose of this design is to preprocess and detect images of handwritten math using a math OCR library, and to get useful information about the math and perform different tasks and functions using the mathematical information from the image the user provides. 

My project idea is a reader for written mathematical equations that can automatically do calculations
for simple (and progressively more complex, depending on how much time I have) mathematical
equations. The project will utilize image processing techniques to do recognition of the different digits
and mathematical notations and symbols and be able to read mathematical notation to figure out what
the equation that the camera is reading is supposed to be. Image processing techniques and libraries
will be used to do the digit recognition and the symbol recognition to recognize the mathematical
notation, and the answer to the scanned mathematical expression will be automatically calculated and
outputted onto a screen.

## Prelimininary Design Verification



## Design Implementation


### Function 1 (Menu Option 1). Perform OCR on the math image and display the predicted math and LATEX code
This is done using a LATEX Math OCR library. The output of the OCR is displayed, both the raw LATEX code and the final image, which is the output of the LATEX code.  

### Function 2 (Menu Option 2.). Convert predicted LATEX code into SymPy code
The LATEX code from the previous output of the Math Image OCR is converted into SymPy code (for the purposes of automatically helping the user implement that math in Python), and the output is displayed to the user.
The conversion from LATEX code into SymPy code has been implemented with another Python library. 


### Function 3 (Menu Option 3). Do arithmetic using the user input (image of math) and solve the arithmetic
The SymPy code that is converted from the LATEX code can be evaluated to get an answer to SymPy numerical computations. Hence, this should theoretically result in the math in the input image being evaluated if it is an exact expression. The answer can be exported to a file. 

## Function 4 (Menu Option 4). Convert predicted LATEX code to Symbolic Python code and export

Converting the predicted LATEX code >> Symbolic Python AND exporting the Symbolic Python as a .py file.

### Function 5 (Menu Option 5). Convert predicted LATEX code to MATLAB code and export

### Function 6 (Menu Option 6). Export the direct LATEX code that is the output of the Math Image OCR

### Menu
A menu is provided to the user. The user can select which feature of this project that they would like to use. 


## Design Testing






## Summary, Conclusions, and Future Work









## Explanation of Organization of Project Files and Main Files of Interest


## Acknowledgements
Libraries that I used in this project

https://github.com/lukas-blecher/LaTeX-OCR

https://github.com/OrangeX4/latex2sympy/blob/master/README.md
