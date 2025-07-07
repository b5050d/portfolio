class Project:
    def __init__(
        self,
        id: int,
        name: str,
        oneline_description: str,
        description: str,
        bullets: list = [],
        bullet_colors: list = [],
        image_path: str = "",
        video_link: str = None,
        link_titles=[],
        links_raw=[],
    ):
        self.id = id
        self.name = name
        self.oneline_description = oneline_description
        self.description = description
        self.bullets = bullets
        self.bullet_colors = bullet_colors
        self.image_path = image_path
        self.video_link = video_link

        self.link_titles = link_titles
        self.links_raw = links_raw


my_projects = []

my_projects.append(
    Project(
        id=0,
        name="Sim Racing Pedals",
        oneline_description="I created 3D printed sim-racing pedals",
        description="As part of a challenge to beat the My Summer Car rally using all of my own sim racing equipment, I designed, fabricated and programmed sim racing pedals",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="simracing_pedals.png",
        video_link=r"https://www.youtube.com/embed/AL3es1MB4ro?si=5260cy6Y2z4P2MGV",
    )
)

my_projects.append(
    Project(
        id=1,
        name="Sim Racing Handbrake",
        oneline_description="I created a 3D printed sim racing handbrake",
        description="Continuing on the challenge to beat the My Summer Car Rally using all of my own sim racing equipment, I created a 3D printed handbrake",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="simracing_handbrake.png",
        video_link=r"https://www.youtube.com/embed/dmfHwvvCK10?si=9uHr-wbt9ZEYYtfk",
    )
)

my_projects.append(
    Project(
        id=2,
        name="Sim Racing Shifter",
        oneline_description="I created a 3D printed sim racing shifter",
        description="Continuing on the challenge to beat the My Summer Car Rally using all of my own sim racing equipment, I created a 3D printed shifter",
        bullets=[
            "3D Printing",
            "Embedded Systems",
            "Programming",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="simracing_shifter.png",
        video_link=r"https://www.youtube.com/embed/JAJKFBZnZKw?si=Zse9Rt6HsOvBeM81",
    )
)

my_projects.append(
    Project(
        id=3,
        name="Automated PNG to STL Generator (Cookie Cutter)",
        oneline_description="I created a tool to automatically generate 3D printable cookie cutters from PNG images",
        description="Find at > app.pngprint.me (link)\nThis tool takes a PNG image of a cookie cutter design and generates a 3D printable STL file. It uses OpenCV to process the image and extract the contours, which are then converted into a 3D model using the custom python utilities. For now, this can be found on my github, but I am actively working on it and will be making it more robust and easier to use.",
        bullets=[
            "Python",
            "STL-Files",
            "Image Processing",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="cookie_cutter_collage.png",
        link_titles=["GitHub Repo"],
        links_raw=["https://github.com/b5050d/stl_generation"],
    )
)

my_projects.append(
    Project(
        id=4,
        name="Portfolio Website",
        oneline_description="I created and self host my own portfolio website",
        description="You are here now! I made this site to host my projects and information about me for prospective employers, and just to share what I am up to. For this application, I used Flask, Tailwind CSS, HTML, python and bash scripts to create this CI/CD enabled web application that I self host on my own Raspberry Pi.",
        bullets=[
            "Flask",
            "Continuous Integration",
            "Continouous Deployment",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="portfolio.png",
        # video_link=r"https://www.youtube.com/embed/AL3es1MB4ro?si=5260cy6Y2z4P2MGV",
    )
)

my_projects.append(
    Project(
        id=5,
        name="Demo Ecommerce Website (Cookies)",
        oneline_description="I created a demonstration ecommerce website to sell homemade cookies",
        description="This demo site piggybacks off of my portfolio website and can be accessed at the endpoint /cookies",
        bullets=[
            "Flask",
            "Ecommerce",
            "Web Design",
        ],
        bullet_colors=["blue", "green", "yellow"],
        image_path="cookies_project.png",
    )
)
