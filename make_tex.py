import os
from src.sessions import Session
from src.papers import Paper

import numpy as np
import pandas as pd


def read_sessions(path_to_excel, sheet_name):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name, dtype={'Room': str})
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
    parser = argparse.ArgumentParser("Make tex files from the technical program excel file")
    parser.add_argument("--excel", help="path to the input technical program excel file")
    parser.add_argument("--tex", help="path to tex project root")
    args = parser.parse_args()

    sessions = read_sessions(args.excel, sheet_name="metadata")
    papers = []
    for sheet_name in ["poster", "oral", "special session", "industry forum", "student forum", "young forum"]:
        papers.extend(read_papers(args.excel, sheet_name=sheet_name))

    for paper in papers:
        sessions[paper.session].papers.append(paper)

    for session in sessions.values():
        path_to_tex = os.path.join(args.tex, session.type, session.name + ".tex")
        os.makedirs(os.path.dirname(path_to_tex), exist_ok=True)
        with open(path_to_tex, "w") as f:
            f.write(session.tex)
            f.write("\n")
            for paper in session.papers:
                f.write(paper.tex)
                f.write("\n")
