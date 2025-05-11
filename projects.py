class Project:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        bullets: list = [],
        bullet_colors: list = [],
        image_path: str = "",
    ):
        self.id = id
        self.name = name
        self.description = description
        self.bullets = bullets
        self.bullet_colors = bullet_colors
        self.image_path = image_path


my_projects = []

my_projects.append(
    Project(
        id=0,
        name="Sim Racing Pedals",
        description="I created 3D printed sim-racing pedals",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="moose.png",
    )
)
