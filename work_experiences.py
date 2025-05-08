


class WorkExperience:
    def __init__(self, position: str, company: str, location: str, start_date: str, end_date: str, bullets: list = []):
        self.position = position
        self.company = company
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.bullets = bullets



work_experiences = []
work_experiences.append(
    WorkExperience(
        position="Test Engineer II",
        company="Agile RF Systems, LLC",
        location="Berthoud, CO",
        start_date="Aug, 2023",
        end_date="Present",
        bullets=[
            "Wrote an extensive Python-based testing automation environment, controlling devices, data processing, and reporting",
            "Designed and implemented CI/CD pipelines to automate testing, deployment and production workflows",
            "Led the end-to-end design and testing of a production software package for controlling Phased Array devices (Python, C)",
            "Extensively worked with Linux environments, developing and deploying radar software on embedded Linux systems.",
            "Designed and validated firmware for STM32 microcontrollers in C, optimizing performance for embedded systems",
            "Engineered custom communication protocol for Phased Array Radar devices, optimizing transmission and reliability.",
            "Developed an internal asset-tracking web app using Python, improving data and documentation management.",            "Automated complex calibration procedures for Phased Array Radar devices, integrating a robot arm positioner for precision",
            "Designed electrical interfaces and created wiring diagrams/harness drawings for deliverable hardware",
            "Developed an extensive suite of test automation to streamline testing and validation for RF and embedded systems.",
            "Managed company-wide Git repositories, improving software collaboration across teams.",
            "Wrote and optimized firmware for multiple embedded systems, including phased array radar devices and test GSE",
        ]
    )
)


