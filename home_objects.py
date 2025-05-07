

class Education():
    def __init__(self, title: str, institution: str, date: str, location: str, bullets: list):
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
        ]
    )
)
