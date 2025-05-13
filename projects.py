class Project:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        bullets: list = [],
        bullet_colors: list = [],
        image_path: str = "",
        video_link: str = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.bullets = bullets
        self.bullet_colors = bullet_colors
        self.image_path = image_path
        self.video_link = video_link


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
        image_path="simracing_pedals.png",
        video_link="https://youtu.be/AL3es1MB4ro?si=Uv6rZIEc8pcrCamo",
    )
)

my_projects.append(
    Project(
        id=1,
        name="Sim Racing Handbrake",
        description="I created a3D printed sim-racing handbrake",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="simracing_handbrake.png",
        video_link="https://youtu.be/dmfHwvvCK10?si=B28gp7n3u9sgrLMc",
    )
)

my_projects.append(
    Project(
        id=2,
        name="Sim Racing Shifter",
        description="I created a 3D printed sim-racing shifter",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="simracing_shifter.png",
        video_link="https://youtu.be/JAJKFBZnZKw?si=0lSRrN2TIkIIuYSD",
    )
)
