# CS510 CW 6

**Author(s):** **CHANGEME**

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-06-YOURNAME.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-06-YOURNAME)

## Specification

1. Keeping your group of two (GROUPA), find another nearby group that you have not yet worked with (GROUPB). Link each other the repositories for the latest CW05, so that you can evaluate each other's code.
    * Open a Jupyter notebook: ```critique-GROUPA-GROUPB.ipynb```
    * Constructively critique GROUPB's code in your Jupyter notebook (in the GROUPA CW06 repository). Use the following questions as a guideline: Is it clear how the code is organized? Is the code properly documented with both docstrings and supplementary comments according to industry standards? Can you follow the algorithm of the code, i.e., what it is doing, and how? Do you see any suggestions for how to improve the code? Discuss your critique with the members of the other group.
    * Send each other your respective critique notebooks. Commit both your critique and their critique to your repository.
1. Work through the [Numpy/Pandas slides](http://slides.com/profdressel/numpy-and-pandas-overview) carefully. Be sure to use ```ipython3``` in a terminal to test how things work. Discuss amongst yourselves anything that is new or unclear.
1. Create a python module ```cplane-np.py```. Import the module ```abscplane.py``` in the repository. Create a new class ```ArrayComplexPlane``` that subclasses the abstract base class ```AbsComplexPlane```. Provide implementations for the requested methods similar to the last classwork, but instead use ```numpy``` arrays augmented with ```pandas``` labels to implement the 2D complex plane.  (Hint: Try to avoid using explicit ```for``` loops in your code. Instead use features of ```numpy``` to avoid ```for``` loops.)
1. Create a test module ```test_cplane-np.py``` that verifies that your implementation is correct.
1. In a Jupyter notebook ```cplane-np.ipynb``` provide a demonstration of how your class works (using small grids of points for clarity). Include a detailed discussion comparing this implementation with your previous implementation using vanilla python lists.
1. After your notebooks are complete, spell-checked, and professionally formatted properly, add and commit them to GitHub. Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having only one person from your edit the notebooks at a time, being sure to pull all changes before you start editing yourself.


## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

We beleive The new you method for creating the grid would be more useful and can be easily made comapre to the list-in-list method which we implented last time. Decaying the use of for loops and acquiring the power of Numpy library was the challenge that we conquer. 

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Sharon Kim, Ehsan Yaghmaei
