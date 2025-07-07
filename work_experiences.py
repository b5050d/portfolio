class WorkExperience:
    def __init__(
        self,
        position: str,
        company: str,
        location: str,
        start_date: str,
        end_date: str,
        bullets: list = [],
    ):
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
            "Led design and testing of Production Software for controlling Phased Array Devices and Radar using Python and C",
            "Led Software Design of Controls, Signal Processing of Radar data using Docker-Compose (Podman) to deploy on RHEL",
            "Built extensive Python-based Test Automation environment for controlling devices, processing data, and report generation",
            "Built an extensive Python-based test automation environment for controlling devices, processing data, and report generation",
            "Attended course and earned FAA Part 107 License to fly drones for Test Automation purposes",
            "Automated Phased Array Radar calibration and test using robotic arm positioner for high-precision alignment",
            "Developed and optimized STM32/Linux firmware for radar PCBs and test ground support equipment (GSE)",
            "Engineered custom communication protocols for Phased Array Radar devices, optimizing transmission and reliability",
            "Built CI/CD pipelines to automate testing, deployment, and production workflows",
            "Developed an internal asset-tracking web app using Python, Flask, and Jinja2, improving data/documentation management",
            "Managed company-wide Git repositories, improving software collaboration across teams.",
            "Designed electrical interfaces and created wiring diagrams/harness drawings for deliverable hardware",
            "Worked with customers to iterate through design requirements for deliverable software systems",
            "Worked closely with systems engineers to translate requirements into software and hardware specifications",
        ],
    )
)

work_experiences.append(
    WorkExperience(
        position="Test Engineer",
        company="Blue Canyon Technologies",
        location="Lafayette, CO",
        start_date="Nov, 2022",
        end_date="Aug, 2023",
        bullets=[
            "Automated production and administrative tasks using Ruby, Python, and VBA to improve lab efficiency",
            "Developed utilities in Python and Ruby to automate routine oscilloscope captures and generate HTML reports.",
            "Used Ball Aerospace's COSMOS (Ruby) to create, modify, and debug automated test scripts for electrical hardware",
            "Performed functional testing on flight and GSE electrical hardware, ensuring compliance with specifications.",
            "Created software-driven automation concepts and presented scope-of-work, POCs, and cost estimates to leadership.",
        ],
    )
)

work_experiences.append(
    WorkExperience(
        position="Mechanical/Test Engineer",
        company="Microsoft",
        location="Fort Collins, CO",
        start_date="June, 2021",
        end_date="Nov, 2022",
        bullets=[
            "Developed machine-vision algorithms to automate object detection and camera targeting using motors.",
            "Automated sensor testing and data processing with Python, MATLAB, and Powershell, improving testing efficiency.",
            "Designed software applications for communication with testing equipment via NET, I2C, and serial connections.",
            "Built simple electrical systems to drive stepper motors, LEDs, microcontrollers, and read thermocouples.",
            "Designed and 3D-printed camera testing equipment to meet project specifications.",
        ],
    )
)
