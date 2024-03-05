from dataclasses import dataclass
from src.papers import Paper
from src.utils import process_tex

@dataclass
class Session:
    name: str
    type: str
    papers: list[Paper]
    topic: str
    chair: str
    time: str
    toc_time: str
    room: str
    presenter: str
    organizer: str

    @property
    def tex(self):
        return process_tex(
            r"\session{%s}{%s}{%s}{%s}{%s}{%s}{%s}{%s}{%s}"
            % (
                self.name,
                self.topic,
                self.room,
                self.type,
                self.time,
                self.toc_time,
                self.chair,
                self.presenter,
                self.organizer,
            )
        )

    @property
    def html(self):
        cls = "session" if not self.presenter else "session w-presenter"
        content = f"{self.name}: {self.topic}<br>Room: {self.room}<br>Type: {self.type}<br>{self.time}<br>"
        if self.presenter:
            content += f"Presenter: {self.presenter}<br>"
        if self.organizer:
            content += f"Organizer: {self.organizer}<br>"
        if self.chair:
            content += f"Chair: {self.chair}<br>"
        return f"""<div class="{cls}" id="{self.name}">{content}</div>"""

    @property
    def toc_entry_in_html(self):
        return f"""<div class="toc-entry"><span class="toc-entry-time">[{self.toc_time}]</span> <a href="#{self.name}">{self.name} - {self.topic}</a></div>"""

