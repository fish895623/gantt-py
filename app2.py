from datetime import date, timedelta
import gantt
from gantt import Resource, Task, Project, Milestone

from typing import List

gantt.define_font_attributes(
    fill='black', stroke='black', stroke_width=0, font_family='Verdana'
)

class Register:
    def __init__(self) -> None:
        self.Task = TaskRegister(self)
        pass

class ResourceRegister(Resource):
    def __init__(self, name, fullname=None):
        super().__init__(name, fullname)

class TaskRegister(Task):
    def __init__(
        self,
        name,
        start=None,
        stop=None,
        duration=None,
        depends_of=None,
        resources=None,
        percent_done=0,
        color=None,
        fullname=None,
        display=True,
        state='',
    ):
        super().__init__(
            name,
            start,
            stop,
            duration,
            depends_of,
            resources,
            percent_done,
            color,
            fullname,
            display,
            state,
        )

class ProjectRegister(Project):
    def __init__(self, name="", color=None):
        super().__init__(name, color)

class MilestoneRegister(Milestone):
    def __init__(
        self, name, start=None, depends_of=None, color=None, fullname=None, display=True,
    ):
        super().__init__(
            name, start, depends_of, color, fullname, display,
        )


class Gantt:
    def __init__(self) -> None:
        self.projects: Project
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
                depends_of=[self.tasks.index(i) for i in (depends_of or [])],
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
    Register
