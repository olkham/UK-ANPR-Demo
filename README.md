# Code deployment
## Table of contents
- [Code deployment](#code-deployment)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Local inference](#local-inference)
  - [Troubleshooting](#troubleshooting)


## Introduction

Example of an ANPR model trained on UK number plates.

Note: This is only the detection part, it does not do the OCR part.

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/)

## Installation

1. Install [prerequisites](#prerequisites). You may also need to 
   [install pip](https://pip.pypa.io/en/stable/installation/). For example, on Ubuntu 
   execute the following command to install Python and pip:

   ```
   sudo apt install python3-dev python3-pip
   ```
   If you already have installed pip before, make sure it is up to date by doing:

   ```
   pip install --upgrade pip
   ```

2. Create a clean virtual environment: <a name="virtual-env-creation"></a>

   One of the possible ways for creating a virtual environment is to use `virtualenv`:

   ```
   python -m pip install virtualenv
   python -m virtualenv <directory_for_environment>
   ```

   Before starting to work inside the virtual environment, it should be activated:

   On Linux and macOS:

   ```
   source <directory_for_environment>/bin/activate
   ```

   On Windows:

   ```
   .\<directory_for_environment>\Scripts\activate
   ```

   Please make sure that the environment contains 
   [wheel](https://pypi.org/project/wheel/) by calling the following command:

   ```
   python -m pip install wheel
   ```

   > **NOTE**: On Linux and macOS, you may need to type `python3` instead of `python`.


3. Install requirements in the environment:

   ```
   python -m pip install -r requirements.txt
   ```

   
## Usage
### Local inference
Make sure to activate your virtual environment

1. Edit `inferece_demo.py` to specify your media source. Use an index for cameras or supply a path to a video file. Then run!
   ```
   python inference_demo.py
   ```

## Troubleshooting


1. If you use Anaconda as environment manager, please consider that OpenVINO has 
   limited [Conda support](https://docs.openvino.ai/2021.4/openvino_docs_install_guides_installing_openvino_conda.html). 
   It is still possible to use `conda` to create and activate your python environment, 
   but in that case please use only `pip` (rather than `conda`) as a package manager 
   for installing packages in your environment.

2. If you have problems when you try to use the `pip install` command, please update 
   pip version as per the following command:
   ```
   python -m pip install --upgrade pip
   ```
