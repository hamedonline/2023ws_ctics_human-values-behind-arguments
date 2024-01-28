# Code Repository for CTiCS Course (University of Innsbruck, Winter Semester 2023)

## Introduction

This repository contains the code snippets and notebooks developed for the pro-seminar project of "Current Topics in Computer Science" course held in winter semester 2023, University of Innsbruck. All the codes are organized in folders corresponding to the parts of the project.

## Contributors & Tasks

General information about the contributors and their tasks are listed in the table below. Please note that each contributor may have helped in other parts of the project as well, but the table only reflects the main task that was agreed upon and assigned to each team member.

| Contributor | Task |
| ----------- | ---- |
| [Sebastian Pellizzari](https://github.com/sebko-p) | Report Organization (Paper) |
| [Hamed Homaeirad](https://github.com/hamedonline) | Exploratory Data Analysis (EDA) |
| [Jannis David Voigt](https://github.com/JannisVoigtUIBK) | Baseline for LLMs Prompting, ChatGPT-3.5 |
| [Peter Burger](https://github.com/peeterburger) | Prompting, Chain of Thought Experiments |
| [Elbaraa Elsaadany](https://github.com/Baraa-yusri) | Llama2 Experiments |

## Presentation Slides & Report (Paper)

The presentation slides and the report (paper) are available in the `presentation-slides` [(click to download presentation PDF)](./presentation-slides/CTiC_Presentation.pdf) and `report-paper` folders of the repository, respectively.

## Running the Code & Reproducing the Results

You may clone the repository to your local machine and run the codes. All of the codes & notebooks are written in Python programming language. Note that at-least Python version 3.9 is essential for a successful run. Additionally, required packages are listed in the `requirements.txt` file which makes it easier to create a virtual environment and avoid any dependency issues with your current Python installation.

### Virtual Environment

It is recommended to use a virtual environment for running the codes in order to avoid any dependency issues. You may refer to __Approach 2__ discussed in [this article](https://github.com/hamedonline/islab-course-material/blob/main/01_introduction/01.1_installing-python.ipynb) if you need help with creating a virtual environment.

Alternatively, you can use `pipenv` to create a virtual environment:

```bash
pip install pipenv
```

Then change the directory and navigate to the folder under which you would like to create a virtual environment for. This folder should have a `requirements.txt` file containing the required packages for the code to run.

```bash
pipenv install -r requirements.txt
```

Then you can activate the virtual environment:

```bash
pipenv shell
```

In case you've already activated the virtual environment, you can install new packages simply using `pip`:

```bash
pip install <package-name>
```

Or you may even install new packages without activating it, only by navigating to the virtual environment folder and using `pipenv install <package-name>`.

### Installing & Running Jupyter Lab

You can install jupyter lab inside the virtual environment using `pip`:

```bash
pip install jupyter jupyterlab
```

Having jupyter lab installed manually or via `requirements.txt`, you can run it from the virtual environment:

```bash
jupyter lab
```
