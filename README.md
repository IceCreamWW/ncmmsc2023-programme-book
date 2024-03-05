# NCMMSC2023 Programme Book

NCMMSC 2023 Programme Book Overleaf: https://www.overleaf.com/read/cwwchqqqxqcg#dc8408

## TL;DR

### 1. Make programme book pdf
run `python make_tex.py --excel assets/TechnicalProgram.xlsx --workspace assets/Tex`, and upload the files in `assets/Tex` to your overleaf template.
### 2. Make programme book html
run `python make_html.py --excel assets/TechnicalProgram.xlsx --workspace assets/index.html`, and place the paper pdf files under `assets/pdfs` to make the links in `assets/index.html` valid.

## Guidance for making a programme book
### Step 1: Make TechnicalProgram.xlsx
create the `assets/TechnicalProgram.xlsx`, this excel contains all information about the sessions of the conference.

Following are used fields in code, other fields in xlsx are not required
####  metadata sheet: 
1. Session: session id
2. Topic: session topic
3. Room: session room
4. Type: session type
5. Time: session time
6. Chair: session chair
7. ToC Time: time string shown in ToC
8. presenter: presenter name (optional, some sessions, e.g. Plenary Session, may have one group of presenter for each session)
9. organizer: organizer name (optional, some sessions, e.g. Special Session, may have organizer)

#### <session> sheets
1. Title: paper title
2. Session: session id of the paper
3. Present ID: presentation id in session
4. Time: paper presentation time, optional
5. Authors: paper authors (optional)
6. Presenter: paper presenter (optional)
7. Paper ID: paper id (optional)

### Step 2: Make overleaf template:
Read the overleaf template, only the `main.tex` should be created manually, i.e. specify the date and order for each session

### Step 3: Make programme book pdf:
run `python make_tex.py --excel assets/TechnicalProgram.xlsx --tex assets/Tex`, and upload the files in `assets/Tex` to your overleaf template.


### Step 4: Make programme book pdf:
run `python make_html.py --excel assets/TechnicalProgram.xlsx --html assets/index.html`, and place the paper pdf files under `assets/pdfs` to make the links in `assets/index.html` valid.

