from dataclasses import dataclass
from src.utils import process_authors, process_tex

@dataclass
class Paper:
    time: str
    title: str
    authors: str
    session: str
    present_id: str
    presenter: str
    paper_id: str

    @property
    def tex(self):
        return process_tex(
            r"\paper{%s}{%s}{%s}{%s}{%s}{%s}"
            % (
                self.present_id,
                self.title,
                process_authors(self.authors),
                self.time.replace(" ", ""),
                self.presenter,
                self.paper_id,
            )
        )

    @property
    def html(self):
        authors = process_authors(self.authors)
        title = f"{self.present_id} {self.title}"
        content = authors if authors else f"Presenter: {self.presenter}"
        href = f'href="pdfs/{self.paper_id}.pdf" target="_blank"'
        title = f"<a {href}>{title}</a>" if self.paper_id else title
        return f"""<div class="paper">{self.time}<div class="title">{title}</div>{content}"""
