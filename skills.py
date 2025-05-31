class SkillCategory:
    """
    Category to hold skills
    """

    def __init__(self, title, skills: list = []):
        self.title = title
        self.skills = skills


skill_categories = []

skill_categories.append(
    SkillCategory(
        title="Specialized Software Skills",
        skills=[
            "Test Automation",
            "Robotics",
            "Computer Vision / Signal Processing",
            "Machine Learning",
            "Web Development (Flask, Jinja2)",
        ],
    )
)
# Category
skill_categories.append(
    SkillCategory(
        title="Languages (Proficient)",
        skills=[
            "Python",
            "C",
            "MATLAB",
            "HTML",
            "CSS",
        ],
    )
)
skill_categories.append(
    SkillCategory(
        title="Languages (Familiar with)",
        skills=[
            "Ruby",
            "SQL",
            "C#",
            "JavaScript",
            "Java",
            "R",
        ],
    )
)

skill_categories.append(
    SkillCategory(
        title="DevOps & Automation",
        skills=[
            "Continuous Integration (CI)",
            "Continuous Deployment (CD)",
            "Docker",
            "Prometheus",
            "Grafana",
            "GitHub Actions",
            "Git Hooks",
            "Bash",
        ],
    )
)

skill_categories.append(
    SkillCategory(
        title="Tools & Technologies",
        skills=["Git", "Linux (RHEL)", "VS Code", "STM32CubeIDE"],
    )
)


skill_categories.append(
    SkillCategory(
        title="Embedded Systems",
        skills=[
            "STM32",
            "Raspberry Pi",
            "Raspberry Pi Pico",
            "ADRV9009-ZU11EG",
            "Arduino Leo/Micro",
        ],
    )
)
# skill_categories.append(SkillCategory("Software Development", []))
# skill_categories.append(SkillCategory("Testing", []))
# skill_categories.append(SkillCategory("Other", []))
