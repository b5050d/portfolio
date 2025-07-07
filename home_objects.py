class Education:
    def __init__(
        self, title: str, institution: str, date: str, location: str, bullets: list = []
    ):
        self.title = title
        self.institution = institution
        self.date = date
        self.location = location
        self.bullets = bullets


educations = []
educations.append(
    Education(
        title="Master's of Science, Computer Science (GPA = 4.000)",
        institution="University of Colorado Boulder: College of Engineering and Applied Science",
        date="May, 2025",
        location="Boulder, CO",
        bullets=[
            "Earned\tGraduate Certificate in Artificial Intelligence\tas part of MSCS program"
        ],
    )
)
educations.append(
    Education(
        title="Google IT Automation",
        institution="Coursera Specialization offered by Google",
        date="July, 2022",
        location="Online",
    )
)
educations.append(
    Education(
        title="Bachelor of Science, Mechanical Engineering",
        institution="Colorado State University",
        date="May, 2021",
        location="Fort Collins, CO",
    )
)
educations.append(
    Education(
        title="FAA Part 107 License",
        institution="(trained at) Colorado State University",
        date="January, 2025",
        location="Fort Collins, CO",
    )
)
