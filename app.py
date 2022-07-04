from datetime import date
import gantt


class Hello:
    def __init__(
        self,
        project_name: str,
        task_name: str,
        task_color: str,
        start_date: date,
        task_duration: int,
        resources: list,
    ):
        self.task_name = task_name
        self.start_date = start_date
        self.task_duration = task_duration
        self.project_name = project_name
        self.task_color = task_color
        self.resources = resources

        self.resource_lists = []
        self.tasks = []
        pass

    def Task(self):
        gantt.Task(
            name=self.task_name,
            start=self.start_date,
            duration=self.task_duration,
            resources=self.resources,
        )
        pass


emp = ["Ben", "Alex"]

Ben = gantt.Resource("Ben")
Alex = gantt.Resource("Alex")

task1_project1 = gantt.Task(
    name="task1", start=date(2021, 1, 27), duration=13, resources=[Ben], color="#a3ddcb"
)
task2_project1 = gantt.Task(
    name="task2", start=date(2021, 2, 10), duration=8, resources=[Alex], color="#a3ddcb"
)
task3_project1 = gantt.Task(
    name="task3", start=date(2021, 2, 19), duration=10, resources=[Ben], color="#a3ddcb"
)
task4_project1 = gantt.Task(
    name="task4",
    start=date(2021, 3, 1),
    duration=12,
    resources=[Ben, Alex],
    color="#a3ddcb",
)

project_1 = gantt.Project(name="Project 1")


for task in [task1_project1, task2_project1, task3_project1, task4_project1]:
    project_1.add_task(task)

project_1.make_svg_for_resources(
    filename="hello.html",
    today=date(2021, 1, 27),
    start=date(2021, 1, 20),
    end=date(2021, 4, 1),
)
