
class SkillCategory:
    """
    Category to hold skills
    """
    def __init__(self, title, skills: list = []):
        self.title = title
        self.skills = skills

skill_categories = []

# Category
skill_categories.append(
    SkillCategory(
        title = "Languages/Frameworks",
        skills = [
            "Python",
            "C",
            "Ruby",
            "MATLAB",
            "SQL",
            "C#",
            "HTML",
            "CSS",
            "JavaScript",
            "Java",
            "R",
        ]
    )
)

skill_categories.append(
    SkillCategory(
        title = "Preferred IDE's",
        skills = [
            "Visual Studio Code",
            "STM32CubeIDE",
            "Vim",
            "IntelliJ IDEA",
        ]
    )
)

skill_categories.append(
    SkillCategory(
        title = "Tools & Technologies",
        skills = [
            "Git",
            "GitHub",
            "Gitea",
            "Docker",
            "Virtual Box",
            "Linux",
        ]
    )
)

skill_categories.append(
    SkillCategory(
        title = "Operating Systems",
        skills = [
            "Windows",
            "Linux",
        ]
    )
)


skill_categories.append(
    SkillCategory(
        title = "Embedded Systems",
        skills = [
            "STM32",
            "Raspberry Pi",
            "Raspberry Pi Pico",
            "ADRV9009-ZU11EG",
            "Arduino Micro",
        ]
    )
)
# skill_categories.append(SkillCategory("Software Development", []))
# skill_categories.append(SkillCategory("Testing", []))
# skill_categories.append(SkillCategory("Other", []))
