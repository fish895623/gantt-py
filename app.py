from datetime import date
from typing import List

import gantt
from gantt import Project, Resource, Task


class Hello:
    def __init__(
        self,
        project_name: str,
        task_name: str,
        task_color: str,
        start_date: date,
        task_duration: int,
        resources: List[str],
        filename: str = 'home.html',
        depends_of: List[str] = [""],
    ):
        self.task_name = task_name
        self.start_date = start_date
        self.task_duration = task_duration
        self.project_name = project_name
        self.task_color = task_color
        self.depends_of = depends_of
        self.resources = resources
        self.filename = filename

        self.tasks: List[Task] = []
        self.proj: Project = Project(name=self.project_name)
        pass

    def task(self):
        self.tasks.append(
            gantt.Task(
                name=self.task_name,
                start=self.start_date,
                duration=self.task_duration,
                resources=[Resource(i) for i in self.resources],
            )
        )
        pass

    def register_task(self):
        for task in self.tasks:
            self.proj.add_task(task=task)

    def export(self):
        self.proj.make_svg_for_resources(
            filename=self.filename,
            today=date(2021, 1, 27),
            start=date(2021, 1, 20),
            end=date(2021, 4, 1),
        )


if __name__ == '__main__':
    gantt.define_font_attributes(
        fill='black', stroke='black', stroke_width=0, font_family='Verdana'
    )
    a = Hello(
        project_name='asdf',
        task_name='fff',
        task_color='#a3ddcb',
        start_date=date(2021, 1, 27),
        task_duration=2,
        resources=['hello', '123'],
    )
    a.task()
    a.register_task()
    a.export()
