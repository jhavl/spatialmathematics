# A Tutorial on Spatial Mathematics

[![Powered by the Robotics Toolbox](https://raw.githubusercontent.com/petercorke/robotics-toolbox-python/master/.github/svg/rtb_powered.min.svg)](https://github.com/petercorke/robotics-toolbox-python)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/roboticstoolbox-python.svg)
[![QUT Centre for Robotics Open Source](https://github.com/qcr/qcr.github.io/raw/master/misc/badge.svg)](https://qcr.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**By Jesse Haviland and Peter Corke**

This repository contains a collection of Jupyter Notebooks exploring spatial mathematics and related applications. The notebooks are easily extensible to encourage experimentation.

## Contents

- [Synopsis](#1)
- [Python Setup Guide](#2)
- [Running Notebooks Locally](#3)
- [Running Notebooks on Google Colab](#4)
- [Acknowledgements](#6)

<br>

<a id='1'></a>

## Synopsis

Spatial mathematics is an important and foundational concepts in robotics -- how to represent the position and orientation of things (robots, cameras, widgets) in two or three dimensions. These representations form the foundation of professional practice in robotics and AI. This tutorial also introduces mathematical graphs which, combined with these representations, can be used to describe relative positions of places and objects -- search algorithms applied to such graphs is foundational to most robot navigation tasks.

<br>

<a id='2'></a>

## Python Setup Guide

The Notebooks are written using Python and we use several python packages. We recommend that you set up a virtual environment/Python environment manager. We provide a guide to setting up Conda below but feel free to use any alternative such as `virtualenv` or `venv`.

The Notebooks have been tested to run on Ubuntu, Windows and Mac OS with any currently supported version of Python (currently 3.7, 3.8 3.9 and 3.10).

### Conda Environment Setup Guide

Download `miniconda` from [here](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links) while choosing the link for your operating system and architecture.

Follow the Conda install instructions from [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#installation).

In the terminal, make a new `conda` environment. We called our environment `smtutorial` and recommend choosing Python version `3.10`

```bash
conda create --name smtutorial python=3.10
```

We need to activate our environment to use it

```bash
conda activate smtutorial
```

Check out this [link](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) for a handy Conda command cheat sheet. There is also a ~30 minute Conda Tutorial available [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

### Python Package Install Guide

We require several Python packages to run the Notebooks. You should activate the Conda environment before completing this stage.

We use IPython, Jupyter notebook, Robotics Toolbox for Python and associated packages

```bash
pip install ipython notebook "roboticstoolbox-python>=1.0.2" sympy
```

<br>

<a id='3'></a>

## Running Notebooks Locally

We have tested the Notebooks in the default Jupyter Notebook web interface and the VSCode Notebook extension.

### Clone the Repository

Firstly, you must clone the repository

```bash
git clone https://github.com/jhavl/spatialmathematics.git
cd dkt
```

### Running in the Jupyter Notebook Web Interface

In terminal, activate the conda environment, navigate to the repository folder and run

```bash
conda activate smtutorial
cd "path_to_repo/spatialmathematics"
jupyter-notebook
```

### Running in the VSCode Interface

Download and install VSCode from [here](https://code.visualstudio.com/).

Add the `Python` extension, see this [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (if not already installed).

Add the `Jupyter` extension, see this [link](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (if not already installed).

From VSCode, select `Open Folder...` and navigate to and select the repository folder. You may be prompted to select if you trust the contents of the folder. **Warning** If you decline to trust the folder, it is unlikely that you will be able to run any of the Notebooks.

After selecting the folder, choose which Notebook you would like to run from the Explorer menu on the left side of the screen.

Once a Notebook is open, you must select the kernel from the `Select Kernel` button in the top right side of the screen. Choose the conda environment we created earlier `smtutorial (Python 3.10.X)`.

<br>

<a id='4'></a>

## Running Notebooks on Google Colab

For the fastest and smoothest experience, it is recommended to run the Notebooks locally. However, most Notebooks can be run online on the Google Colab platform.

<br>

<a id='6'></a>

## Acknowledgements

This tutorial is supported by the Queensland University of Technology Centre for Robotics ([QCR](https://research.qut.edu.au/qcr/)).

<img src="https://github.com/jhavl/dkt/raw/main/img/qcr.png" width="500">

