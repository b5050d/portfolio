

class Project:
    def __init__(self, id: int, name: str, description: str, bullets: list = [], image_path: str = ""):
        self.id = id
        self.name = name
        self.description = description
        self.bullets = bullets
        self.image_path = image_path


my_projects = []

my_projects.append(
    Project(
        id = 0,
        name="Sim Racing Pedals",
        description="I created 3D printed sim-racing pedals",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        image_path="moose.jpg"
    )
)
