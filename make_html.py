import numpy as np
import pandas as pd

from src.papers import Paper
from src.sessions import Session

# specifiy the order of sessions
session_names = [
    "Fri-M-T-1",
    "Fri-M-T-2",
    "Fri-A-T-1",
    "Fri-A-T-2",
    "Fri-A-IND",
    "Sat-M-PLEN-1",
    "Sat-M-PLEN-2",
    "Sat-M-O-1",
    "Sat-M-O-2",
    "Sat-M-SS",
    "Sat-M-P-1",
    "Sat-M-P-2",
    "Sat-M-P-3",
    "Sat-M-P-4",
    "Sat-M-YF",
    "Sat-A-O-1",
    "Sat-A-O-2",
    "Sat-A-SS",
    "Sat-A-P-1",
    "Sat-A-P-2",
    "Sat-E-IND",
    "Sat-E-SS",
    "Sun-M-PLEN-1",
    "Sun-M-PLEN-2",
    "Sun-M-O-1",
    "Sun-M-O-2",
    "Sun-M-SF",
    "Sun-M-P-1",
    "Sun-M-P-2",
    "Sun-A-O-1",
    "Sun-A-O-2",
    "Sun-A-SF",
    "Sun-A-P-1",
    "Sun-A-P-2",
    "Sun-A-P-3",
]

css = """
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        a {
            text-decoration: none;
        }

        body {
            max-width: 1000px;
            padding: 0 10px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        .page-title {
            text-align: center;
            font-size: xx-large;
            font-weight: bold;
        }


        .toc {
            margin: 20px 0;
            font-weight: bold;
        }
        .toc-date {
            font-weight: bold;
            font-size: x-large;
            line-height: 2em;
        }
        .toc-date a {
            color: inherit;
        }
        .toc-entry {
            line-height: 1.7em;
            font-size: large;
        }
        .toc-entry-time {
            display: inline-block;
            width: 110px;
        }

        .date {
            font-weight: bold;
            font-size: x-large;
            margin: 50px auto;
            text-align: center;
        }

        .paper {
            margin: 20px 0;
        }

        .paper .title {
            margin: 2px 0;
            font-weight: bold;
        }


        .session {
            background-color: rgba(0, 0, 0, 0.2);;
            font-weight: bold;
            border-color: rgba(0, 0, 0, 0.7);
            line-height: 1.3em;
            border-width: 1pt 1pt 1pt 2px;
            border-style: solid;
            padding: 5px 15px;
            margin: 30px 0 30px 0;
        }

        .session.w-presenter {
            background-color: rgba(0, 0, 0, 0.15);;
            border-width: 1pt 1pt 1pt 2px;
            border-color: rgba(0, 0, 0, 0.4);
        }
    </style>
"""


def read_sessions(path_to_excel, sheet_name):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name, dtype={"Room": str})
    df = df.replace(np.nan, "", regex=True)
    sessions = {}
    for idx, row in df.iterrows():
        if row["Time"] == "":
            continue
        session = Session(
            name=row["Session"],
            type=row["Type"],
            papers=[],
            topic=row["Topic"],
            chair=row["Chair"],
            time=row["Time"],
            toc_time=row["ToC Time"],
            room=row["Room"],
            presenter=row["Presenter"],
            organizer=row["Organizer"],
        )
        sessions[session.name] = session
    return sessions


def read_papers(path_to_excel, sheet_name):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name)
    df = df.replace(np.nan, "", regex=True)
    papers = []
    for idx, row in df.iterrows():
        if row["Session"] == "":
            continue
        paper = Paper(
            title=row["Title"],
            session=row["Session"],
            present_id=row["Present ID"],
            time=row.get("Time", ""),
            authors=row.get("Authors", ""),
            presenter=row.get("Presenter", ""),
            paper_id=row.get("Paper ID", ""),
        )
        papers.append(paper)
    return papers


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Make html from the technical program excel file")
    parser.add_argument("--excel", help="path to the input technical program excel file")
    parser.add_argument("--html", help="path to the output html file")
    args = parser.parse_args()

    sessions = read_sessions(args.excel, sheet_name="metadata")
    papers = []
    for sheet_name in [
        "poster",
        "oral",
        "special session",
        "industry forum",
        "student forum",
        "young forum",
    ]:
        papers.extend(read_papers(args.excel, sheet_name=sheet_name))

    for paper in papers:
        sessions[paper.session].papers.append(paper)

    with open(args.html, "w") as f:
        f.write(f"""<html> <!DOCTYPE html><head>{css}</head><body>""")
        f.write('<div class="page-title"> NCMMSC 2023 Programme Book </div>')

        # table of content
        f.write('<div class="toc">')
        for name in session_names:
            # Make a date in ToC entry before all the sessions of that day
            if name == "Fri-M-T-1":
                f.write("""<div class="toc-date"><a href="#1208">Friday, December 8th</a></div>""")
            if name == "Sat-M-PLEN-1":
                f.write(
                    """<div class="toc-date"><a href="#1209">Saturday, December 9th</a></div>"""
                )
            if name == "Sun-M-PLEN-1":
                f.write("""<div class="toc-date"><a href="#1210">Sunday, December 10th</a></div>""")
            session = sessions[name]
            f.write(session.toc_entry_in_html)
        f.write("</div>")

        for name in session_names:
            # Make a date in content before all the sessions of that day
            if name == "Fri-M-T-1":
                f.write("""<div class="date" id="1208">Friday, December 8th</div>""")
            if name == "Sat-M-PLEN-1":
                f.write("""<div class="date" id="1209">Saturday, December 9th</div>""")
            if name == "Sun-M-PLEN-1":
                f.write("""<div class="date" id="1210">Sunday, December 10th</div>""")
            session = sessions[name]
            f.write(session.html)
            f.write("\n")
            for paper in session.papers:
                f.write(paper.html)
                f.write("\n")
        f.write("</body></html>")
