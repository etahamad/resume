import fitz
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Line

def generate_pdf(output_filename="Omar_Hamad_Resume.pdf"):
    # Letter size: 612 x 792 pt
    # Tight, clean margins to maximize printable area and eliminate awkward whitespace
    margin_x = 28
    margin_y = 24
    content_width = 612 - 2 * margin_x  # 556 pt

    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=margin_x,
        rightMargin=margin_x,
        topMargin=margin_y,
        bottomMargin=margin_y
    )

    styles = getSampleStyleSheet()

    # STRICTLY MONOCHROME (black & grayscale only)
    name_style = ParagraphStyle(
        'ResumeName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        alignment=1, # Centered
        textColor=colors.black,
        spaceAfter=3
    )

    # EXACTLY ONE SINGLE LINE: pipe-separated, zero bullet dots
    contact_style = ParagraphStyle(
        'ResumeContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.5,
        alignment=1, # Centered
        textColor=colors.HexColor('#111111'),
        spaceAfter=5
    )

    section_heading_style = ParagraphStyle(
        'ResumeSectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.black,
        spaceBefore=5,
        spaceAfter=1
    )

    job_title_left = ParagraphStyle(
        'JobTitleLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=10.5,
        textColor=colors.black
    )

    job_title_right = ParagraphStyle(
        'JobTitleRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=10.5,
        alignment=2, # Right
        textColor=colors.black
    )

    job_sub_left = ParagraphStyle(
        'JobSubLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.0,
        leading=9.5,
        textColor=colors.HexColor('#333333')
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.1,
        leading=10.5,
        leftIndent=10,
        firstLineIndent=-7,
        textColor=colors.HexColor('#111111'),
        spaceBefore=1.0,
        spaceAfter=1.0
    )

    skill_category_style = ParagraphStyle(
        'SkillCategory',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.6,
        textColor=colors.HexColor('#111111'),
        spaceBefore=1.5,
        spaceAfter=1.5
    )

    story = []

    # 1. Header: Name
    story.append(Paragraph("<b>Omar Hamad</b>", name_style))

    # 2. Contact info: STRICTLY ONE LINE with pipes
    contact_text = (
        '10th of Ramadan City, Egypt | '
        '+20 101 573 8110 | '
        '+1 202 780 3114 | '
        '<a href="mailto:etatldr@gmail.com" color="#111111"><u>etatldr@gmail.com</u></a> | '
        '<a href="https://etahamad.com" color="#111111"><u>etahamad.com</u></a> | '
        '<a href="https://www.linkedin.com/in/omgr" color="#111111"><u>linkedin.com/in/omgr</u></a> | '
        '<a href="https://github.com/etahamad" color="#111111"><u>github.com/etahamad</u></a>'
    )
    story.append(Paragraph(contact_text, contact_style))

    def make_section_header(title):
        elements = []
        elements.append(Paragraph(f"<b>{title.upper()}</b>", section_heading_style))
        d = Drawing(content_width, 1.5)
        d.add(Line(0, 0.5, content_width, 0.5, strokeColor=colors.black, strokeWidth=0.6))
        elements.append(d)
        elements.append(Spacer(1, 2))
        return elements

    def make_role_header(company, role, dates, location):
        t = Table(
            [
                [Paragraph(f"<b>{company}</b> | <b>{role}</b>", job_title_left), Paragraph(f"<b>{dates}</b>", job_title_right)],
                [Paragraph(f"<i>{location}</i>", job_sub_left), Paragraph("", job_title_right)]
            ],
            colWidths=[content_width * 0.72, content_width * 0.28]
        )
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ]))
        return [t]

    # --- WORK EXPERIENCE ---
    story.extend(make_section_header("WORK EXPERIENCE"))

    # Role 1: Coca-Cola HBC
    story.extend(make_role_header(
        "Coca-Cola HBC",
        "Azure DevOps Engineer",
        "04.2026 - Present",
        "New Cairo, Egypt (Hybrid)"
    ))
    coca_bullets = [
        "Designed and maintained enterprise YAML CI/CD pipelines and deployment templates in Azure DevOps, accelerating delivery velocity by 45% and reducing failures by 35%.",
        "Automated workflows with PowerShell, Bash, and REST APIs, integrating Azure DevOps with ServiceNow and Power BI to synchronize telemetry and save 25+ hours weekly.",
        "Administered Azure DevOps organizations, repos, service connections, and RBAC across 15+ engineering teams, standardizing IaC configurations to 99.5% compliance.",
        "Orchestrated release processes across environments, conducting systematic root cause analyses (RCA) and dashboards that cut MTTR by 50% with 99.9% uptime."
    ]
    for b in coca_bullets:
        story.append(Paragraph(f"-&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 2))

    # Role 2: IQVIA
    story.extend(make_role_header(
        "IQVIA",
        "DevOps Engineer",
        "03.2025 - 04.2026",
        "New Cairo, Egypt"
    ))
    iqvia_bullets = [
        "Led end-to-end infrastructure migration for a government healthcare system serving 4M+ users across staging and production, provisioning 42+ servers and migrating 500GB+ databases within 3 months.",
        "Migrated a custom on-premises datacenter to Microsoft Azure within 1 month, configuring 6 core servers, firewalls, load balancers, and 20+ services for high availability.",
        "Engineered centralized CI/CD pipelines and GitOps workflows using Jenkins, ArgoCD, and Ansible across 200+ hybrid Linux servers, cutting deployment time by 65%.",
        "Deployed Grafana, Prometheus, and the ELK Stack to monitor 20+ critical applications and Kubernetes clusters, managing 15,000+ log events/min and driving MTTR reduction.",
        "Provided 24/7 on-call production support (resolving 50+ P0/L2 incidents with &lt;30 min MTTR); ran monthly DR drills and runbooks that reduced repeat incidents by 40%."
    ]
    for b in iqvia_bullets:
        story.append(Paragraph(f"-&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 2))

    # Role 3: Transforma Studios
    story.extend(make_role_header(
        "Transforma Studios",
        "Software Engineer L3",
        "03.2024 - 12.2024",
        "New York, United States (Remote)"
    ))
    transforma_bullets = [
        "Architected high-throughput backend microservices and RESTful APIs using .NET, C#, Go (Gin, GORM), PostgreSQL, EF Core, and Redis, ensuring sub-second response times.",
        "Architected data models and backend services for an academic platform, enabling course management, office hours scheduling, and administrative workflows.",
        "Built real-time stock processing engine using RabbitMQ and Go, integrated OpenAI APIs for automation, and deployed zero-downtime Kubernetes services via Traefik."
    ]
    for b in transforma_bullets:
        story.append(Paragraph(f"-&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 2))

    # Role 4: 3Sixty
    story.extend(make_role_header(
        "3Sixty",
        "DevOps & Systems Engineer",
        "08.2023 - 01.2024",
        "Georgia, United States (Remote)"
    ))
    three_sixty_bullets = [
        "Developed NetSuite process automations via SuiteScript 2.1 API, delivering a 60x acceleration in billing cycles and financial report generation.",
        'Engineered real-time uptime monitoring portal (<a href="https://status.3sixtydental.com" color="#111111"><u>status.3sixtydental.com</u></a>) and led full-stack engineering of a QMS platform with Vue.js and Go (GORM).',
        "Managed multi-cloud infrastructure across Azure, AWS, and GCP, optimizing resource provisioning, cloud spend, and automating HR data synchronization."
    ]
    for b in three_sixty_bullets:
        story.append(Paragraph(f"-&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 2))

    # --- EDUCATION ---
    story.extend(make_section_header("EDUCATION"))
    edu_header = make_role_header(
        "Future Academy",
        "Bachelor of Computer Science",
        "2019 - 2023",
        "Cairo, Egypt"
    )
    story.extend(edu_header)
    edu_bullets = [
        "GPA: 3.24 / 4.0 | Graduation Project: Excellent (A+) | Head of DevOps Engineer at Google Developer Student Clubs (GDSC FA) for 2 years."
    ]
    for b in edu_bullets:
        story.append(Paragraph(f"-&nbsp; {b}", bullet_style))
    story.append(Spacer(1, 2))

    # --- SKILLS ---
    story.extend(make_section_header("SKILLS"))
    skills_data = [
        ("DevOps & CI/CD", "Azure DevOps (Pipelines, Repos, Boards, Artifacts), YAML Pipelines, CI/CD, Jenkins, GitHub Actions, ArgoCD (GitOps), Helm, CircleCI"),
        ("Automation & Scripting", "PowerShell, Bash Scripting, Python, REST APIs, Workflow Automation, Platform Administration"),
        ("Cloud & Infrastructure as Code", "Microsoft Azure, AWS, GCP, Infrastructure as Code (IaC), Terraform, Azure Bicep, Ansible, CloudFormation, Cloud Operations"),
        ("Enterprise Tools & Observability", "ServiceNow Integration, Power BI Dashboards, Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), Azure Monitor, Log Analytics"),
        ("Containers & Platform Engineering", "Docker, Kubernetes (AKS/K8s), Traefik, Nginx, Apache Web Server, Linux/Unix Administration, Platform Engineering"),
        ("Methodologies & Databases", "Git, GitFlow, Agile, Scrum, SAFe, DevSecOps, Microservices, RabbitMQ, Redis, SQL (PostgreSQL, MySQL), Database Migration")
    ]
    for cat, items in skills_data:
        story.append(Paragraph(f"<b>{cat}:</b> {items}", skill_category_style))

    doc.build(story)
    print(f"Resume generated successfully at {output_filename}")

if __name__ == "__main__":
    generate_pdf()
