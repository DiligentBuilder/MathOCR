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

I have tested my installation of the LaTeX-OCR of the math images using the example math image that is provided in the GitHub of the OCR library. Below is the proof that the library works well with the example, at least:

Test image #1 I am using to test the pix2tex library (using existing library for the mathematical OCR functionality):
![ArithmeticMathOCRLowQuality](https://github.com/DiligentBuilder/MathOCR/assets/71938320/ef9e9895-76c4-4db8-9959-b368a81544bd)

Evidence that the Command Line Tool is working properly for Test Image #1:
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/a59adf89-32ba-448e-9316-a8691ab85bcd)


Test image #2 I am using to test the pix2tex library (using existing library for the mathematical OCR functionality):
![ThenevinMathExampleLowQuality](https://github.com/DiligentBuilder/MathOCR/assets/71938320/aea564b7-ad8c-425f-a7bd-0f14eecd59b1)

Evidence that the Command Line Tool is working properly for Test Image #2:

![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/c8abda77-02e7-4994-b9e5-7d9cbc61cc29)

Overleaf output (what the outputted LATEX code looks like when compiled by Overleaf):

LATEX output for Test Image #1
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/cfdcc2a7-08c1-4601-a7b9-02db44b45897)



LATEX output for Test Image #2

![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/74786958-7628-490e-9702-56d3a2003efc)










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

Here are tests on test images to show that the final system works well for detecting and calculating the handwritten math of different input image with simple arithmetic.

Here, I am testing all the functions that the system has implemented so far using several input images. Here are the current results of the testing.


Input image #1:

![ArithmeticMathOCRLowQuality](https://github.com/DiligentBuilder/MathOCR/assets/71938320/0b060520-917b-4f9e-94b2-1632cffeb0a0)

Going through the first menu option
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/f7e1888f-3a43-4aac-acc6-6ef1f3c31a3b)


Going through the second menu option
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/c60bc488-55c7-4df2-b14d-6d46e7c700c2)


Going through the third menu option

![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/245c9133-64f3-4626-a26a-53ffba6ab86a)

Going through the fourth menu option

![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/3b798417-54d3-47d8-ab2a-090b47fa1d24)

Going through the fifth menu option
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/d2f40a32-2b72-405c-8dc8-37a6b11e77d6)

Going through the sixth menu option
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/b4a44c7c-8326-4790-a43e-534011b20286)

Going through the seventh menu option (and quitting)
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/8825ea70-4601-42d7-8558-f091c324b4a9)






Auto-generated LATEX document outputted by program (compiled using Overleaf)

First page:
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/de3890a7-1516-4ab6-96e9-e17770a5fc86)


Second page:
![image](https://github.com/DiligentBuilder/MathOCR/assets/71938320/317648a4-4305-4f79-9655-24661052ff31)

















## Summary, Conclusions, and Future Work

Throughout this process, I have accomplished many things. I have learned how these libraries work, and I present the easy-to-use tool that applies different libraries, such as LaTeX-OCR and latex2sympy2, to form a cohesive and easy-to-use tool for the average end user. I have integrated and combined many libraries, functions, and tools on Python to create a cohesive, integrated, whole, and easily accessible and usable software OCR tool. This software Math OCR tool can be used by anyone who works with math equations regularly and would like to automate the process of writing out and implementing math equations in LATEX, MATLAB/Octave, C/C++, SymPy, etc. I hope that this tool can be the start to an effective way to automate the process of scanning both printed and typeset as well as handwritten math and implementing those same equations in popular and useful formats in programming languages that are necessary to implement those equations for a wide variety of fields and needs that use lots of mathematical equations, where it would be beneficial to have an automated process, in addition to the manual processes and verification already out there for implementing mathematical equations in different programming formats. 









## Explanation of Organization of Project Files and Main Files of Interest

main.py -- Main Source Code, all source code put into this file, including main code and functions that are implemented and called, libraries are imported here as well and used to help implement the functionalities needed for this project. 


## Acknowledgements
Libraries that I used in this project

https://github.com/lukas-blecher/LaTeX-OCR

https://github.com/OrangeX4/latex2sympy/blob/master/README.md
