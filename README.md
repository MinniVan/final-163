final-163

Our program has three modules. One to open and process the data (process_data.py), one that runs the program (program.py), and a script that prompts the user for their input (prompt_script.py) to help run the program. When running the program via the terminal we received an error regarding the space limit, as a result, a jupyter notebook is required to succesfully run the program.

Additionally, in order to run and reproduce our results all of these files will need to stored and ran in the same folder, that includes the jupyter notebook.

Our dataset has a .z extension. And it is a relatively large dataset therefore, our program will require the installation of h5py - a new library that we are implementing as a challenge for our project.

In addition to the h5py library, these will need to be installed:

numpy, pandas, matplotlib, and math libraries

in order to open, store, and manipulate our data.

Installing these said libraries is achieved by using the anaconda platform and typing "conda install" to install.

We share our original data via our google doc which contained an extremely large data set. However, now the original file needs to be renamed to 'larger_sample.z'

Link to BOTH the small sample and large sample: https://drive.google.com/drive/folders/1QJ2U1QGOa6pTFUmottlxUPvgBWUg5jG8?usp=sharing



If you choose the large data file then all the plots will have their y-axis plotted in the logarithimic scale. If you choose the small data file a normal graph will be plotted.


Again: TO RUN THE PROGRAM
    You must save BOTH the data sets from the
    google docs. On the same folder

    1) Ensure all the files are in the same folder
    2) Open Jupyter Lab or Jupyter NoteBook
    3) Selected the juypter notebook called
        run_program.ipynb
    4) Presh shift enter

    There are two files, smaller size and larger size.
    The program will ask you to choose which file you
    want to run. If you choose one, and you decide
    you want to run the other, you have to run the
    program again.

    Works best by just exiting from the notebook and
    loading Jupyter Lab again

TO reiterate, we were not able to run the program on terminal due
to the size of our data. But jupyter notebook said 'ok'