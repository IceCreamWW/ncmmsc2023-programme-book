# NCMMSC2023 Programme Book Documentation

This documentation provides comprehensive guidance on creating the programme book in both PDF and HTML formats using our automated scripts. For your convenience, the project is hosted on Overleaf, accessible via the following link: [NCMMSC 2023 Programme Book Overleaf](https://www.overleaf.com/read/cwwchqqqxqcg#dc8408).

## Overview

This project facilitates the generation of the conference programme book in two formats: PDF and HTML. The process involves executing Python scripts that take session information from an Excel spreadsheet and compile it into the desired format. Below is a brief guide on how to create each version.

### Creating the PDF Programme Book

1. Execute the following command to generate LaTeX files for the programme book:

```bash
python make_tex.py --excel assets/TechnicalProgram.xlsx --workspace assets/Tex
```

2. After running the command, upload the generated files located in `assets/Tex` to your Overleaf project template.

### Creating the HTML Programme Book

1. To generate the HTML version of the programme book, run:

```bash
python make_html.py --excel assets/TechnicalProgram.xlsx --workspace assets/index.html
```

2. Then, ensure that the PDF files of the papers are placed in `assets/pdfs` so that the links in `assets/index.html` are functional.

## Detailed Instructions

### Step 1: Preparing the `TechnicalProgram.xlsx` File

Start by creating the `assets/TechnicalProgram.xlsx` file. This Excel file should contain all pertinent details regarding the conference sessions.

The following fields are utilized by the scripts. Fields not listed here are not required for the generation process:

#### Metadata Sheet:

- **Session:** Session ID
- **Topic:** Topic of the session
- **Room:** Location of the session
- **Type:** Type of session (e.g., Keynote, Workshop)
- **Time:** Timing of the session
- **Chair:** Chairperson of the session
- **ToC Time:** Time as displayed in the Table of Contents
- **Presenter:** Name of the presenter(s) (Optional for certain sessions like Plenary Sessions)
- **Organizer:** Name of the organizer(s) (Optional for specific sessions like Special Sessions)

#### Session Sheets:

- **Title:** Title of the paper
- **Session:** ID of the session the paper belongs to
- **Present ID:** Presentation ID within the session
- **Time:** Presentation time of the paper (Optional)
- **Authors:** Authors of the paper (Optional)
- **Presenter:** Presenter of the paper (Optional)
- **Paper ID:** ID of the paper (Optional)

### Step 2: Creating the Overleaf Template

You will need to read and prepare the Overleaf template accordingly. The `main.tex` file is the only document that needs to be manually created, where you should specify the date and order of each session.

### Steps for Generating the Programme Book

#### PDF Version:

run `python make_tex.py --excel assets/TechnicalProgram.xlsx --tex assets/Tex`, then upload the generated files located in `assets/Tex` to your Overleaf project template.


#### HTML Version:

run `python make_html.py --excel assets/TechnicalProgram.xlsx --html assets/index.html`, and place the PDF files of the papers in `assets/pdfs` for the links in `assets/index.html` to work correctly.
