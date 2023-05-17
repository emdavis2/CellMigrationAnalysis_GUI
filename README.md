Cell Migration Analysis Repo for making a GUI
================
## Quick Summary:
The goal of this project is to analyze shape and motion data from movies of cells migrating and find correlations that can explain how the two are related and what unique behaviors are exhibited on different substrates in terms of material and stiffness that the cells are moving on. 

This repository contains the source data and code for analysis with the goal of building a GUI that allows users to easily run the analyses.


## How to Run:
Clone this repository and navigate to the folder of this repository on your computer (where the Docker file is located) and build the docker container by running:

```
docker build -t python_docker .
```

Now, run this container with the following: 

```
docker run -v $(pwd):/home/ -it python_docker bash
```
Note: you must be in the directory of this repo on your computer for this to work! `$(pwd)` should ultimately result in the path to this repo on your computer, as we want to port this repo on your local computer to /home/ in the virtual terminal. If running on a Windows machine, it may be necessary to actually type out the path to this repo on your computer instead of `$(pwd)`.

Now your terminal should be interactive with the docker container we have just built. We can use the Makefile to make the figures and fit the model to our data. To generate the autocorrelation figures for the cells migrating on glass, use:

```
make sentinels/ACF_figures_glass.txt
```

To do the same for soft gel, run:

```
make sentinels/ACF_figures_soft_gel.txt
```

And similarly for stiff gel, run:

```
make sentinels/ACF_figures_stiff_gel.txt
```

To generate figures of histograms and box plots and various other features of the data for all the regions, simply run:

```
make sentinels/cellshape_histogram.txt
```

These targets are sentinels since many plots are actually produced, however the text files do list the names of all the figures generated by these targets. The figures are saved in a folder called `figures` and the sentinels are located in a folder called `sentinels`.