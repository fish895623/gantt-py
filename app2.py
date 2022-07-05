from calendar import month
from datetime import date, timedelta
import gantt
from gantt import Resource, Task, Project, Milestone

from typing import List

gantt.define_font_attributes(
    fill='black', stroke='black', stroke_width=0, font_family='Verdana'
)


class Gantt:
    def __init__(self) -> None:
        self.projects: Project = None
        self.tasks: List[Task] = []

    def task(
        self,
        name,
        start: date,
        stop: date,
        resources: List[str] = None,
        depends_of: List[str] = None,
        duration=None,
        percent_done=0,
        color=None,
        fullname=None,
        display=True,
        state='',
    ):
        self.tasks.append(
            Task(
                name,
                start,
                stop,
                duration,
                # depends_of=[Task(name=i) for i in depends_of],
                percent_done=percent_done,
                color=color,
                fullname=fullname,
                display=display,
                state=state,
            )
        )

    def project(self, name):
        self.projects = Project(name=name)
        for _task in self.tasks:
            self.projects.add_task(_task)

    def export(self):
        self.projects.make_svg_for_tasks(
            filename='multiple_projects.svg',
            today=date.today(),
            start=date.today() - timedelta(weeks=2),
            end=date.today() + timedelta(weeks=4),
        )


if __name__ == '__main__':
    a = Gantt()
    a.task(
        name='Hello', resources=['hello'], start=date(2022, 7, 20), stop=date(2022, 7, 30),
    )
    a.task(
        name='hel2', resources=['hello2'], start=date(2021, 1, 27), stop=date(2021, 2, 26),
    )
    a.task(
        name='h22',
        resources=['hello', 'hello2'],
        start=date(2021, 1, 27),
        stop=date(2021, 3, 1),
    )
    a.project(name='asdfadsf')
    a.export()
