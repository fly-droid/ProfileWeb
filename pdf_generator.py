from fpdf import FPDF


def create_cv_pdf(static_data: dict, tailored_data, target_job_title: str, output_filename="Tailored_CV.pdf"):

    # Custom PDF class to add page numbers at the bottom
    class CV_PDF(FPDF):
        def footer(self):
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, f'Page {self.page_no()}', align='C')

    # Initialize PDF
    pdf = CV_PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Establish fixed margins and dimensions for math accuracy
    MARGIN = 15
    pdf.set_left_margin(MARGIN)
    pdf.set_right_margin(MARGIN)
    EFFECTIVE_WIDTH = 180  # 210mm (A4 width) - 30mm (margins)

    def safe_text(text):
        """Replaces unsupported bullets with standard dashes and strips bad characters."""
        if text is None:
            return ""
        # Replace unicode bullet with a standard keyboard dash
        text = str(text).replace('•', '-')
        # Ignore any other characters that would crash the Latin-1 font
        return text.encode('latin-1', 'ignore').decode('latin-1')

    def section_header(title):
        """Helper function to draw a styled section title with a horizontal line."""
        pdf.ln(4)
        pdf.set_font("Helvetica", style="B", size=12)
        pdf.set_text_color(44, 62, 80)  # Dark slate color
        pdf.cell(0, 6, title.upper(), ln=1)

        # Draw a light grey line under the title
        y = pdf.get_y()
        pdf.set_draw_color(200, 200, 200)
        pdf.line(MARGIN, y, MARGIN + EFFECTIVE_WIDTH, y)
        pdf.ln(3)
        pdf.set_text_color(0, 0, 0)  # Reset text color to black

    personal = static_data['personal_info']

    # ==========================================
    # 1. HEADER (Name & Contact Info)
    # ==========================================
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 10, safe_text(personal['name']), ln=1, align='C')

    pdf.set_font("Helvetica", size=14)
    pdf.set_text_color(41, 128, 185)  # Professional Blue
    pdf.cell(0, 6, safe_text(target_job_title), ln=1, align='C')
    pdf.ln(2)

    pdf.set_font("Helvetica", size=9)
    pdf.set_text_color(100, 100, 100)
    # Combine contact info into one clean line separated by pipes
    contact_str = f"{personal['email']}  |  {personal['phone']}  |  {personal['address']}"
    pdf.cell(0, 5, safe_text(contact_str), ln=1, align='C')
    pdf.ln(3)

    # Reset text color for the body
    pdf.set_text_color(0, 0, 0)

    # ==========================================
    # 2. PROFESSIONAL SUMMARY
    # ==========================================
    section_header("Professional Summary")
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(EFFECTIVE_WIDTH, 5, safe_text(tailored_data.summary))

    # ==========================================
    # 3. WORK EXPERIENCE
    # ==========================================
    section_header("Work Experience")
    for role in tailored_data.roles:
        # Job Title (Left aligned)
        pdf.set_font("Helvetica", style="B", size=11)
        pdf.cell(EFFECTIVE_WIDTH - 45, 6, safe_text(role.title), ln=0)

        # Dates (Right aligned on the same line)
        pdf.set_font("Helvetica", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(45, 6, safe_text(role.dates), ln=1, align='R')

        # Company Name
        pdf.set_font("Helvetica", style="B", size=10)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 5, safe_text(role.company), ln=1)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", size=10)

        # Bullets
        for bullet in role.tailored_bullets:
            pdf.set_x(MARGIN + 5)  # Indent the bullet points 5mm
            # Ensure the width is reduced by 5mm to account for the indent
            pdf.multi_cell(EFFECTIVE_WIDTH - 5, 5, safe_text(f"- {bullet}"))
        pdf.ln(3)

    # ==========================================
    # 4. TECHNICAL SKILLS
    # ==========================================
    section_header("Technical Skills")

    # Increased width from 45 to 55 to fit longer labels
    LABEL_WIDTH = 55

    for category, tools in static_data['master_skills'].items():
        # Failsafe: If we are within 35mm of the bottom, force a page break
        # so the label and the list stay together on the next page
        if pdf.get_y() > 260:
            pdf.add_page()

        pdf.set_font("Helvetica", style="B", size=10)
        pdf.cell(LABEL_WIDTH, 6, safe_text(category + ":"), ln=0)

        pdf.set_font("Helvetica", size=10)
        pdf.multi_cell(EFFECTIVE_WIDTH - LABEL_WIDTH, 6, safe_text(tools))
        pdf.ln(1.5)  # Add a tiny bit of breathing room between skill rows
    # ==========================================
    # 5. EDUCATION
    # ==========================================
    section_header("Education")
    for edu in static_data['education']:
        pdf.set_font("Helvetica", style="B", size=10)
        pdf.cell(EFFECTIVE_WIDTH - 45, 5, safe_text(edu['degree']), ln=0)

        pdf.set_font("Helvetica", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(45, 5, safe_text(edu['year']), ln=1, align='R')

        pdf.set_font("Helvetica", size=10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 5, safe_text(edu['institution']), ln=1)
        pdf.ln(2)

    # ==========================================
    # 6. CERTIFICATIONS & EXTRACURRICULAR
    # ==========================================
    section_header("Certifications & Extracurricular")
    pdf.set_font("Helvetica", size=10)
    for cert in static_data['certifications']:
        pdf.set_x(MARGIN + 5)
        pdf.multi_cell(EFFECTIVE_WIDTH - 5, 5, safe_text(f"- {cert}"))

    # ==========================================
    # 7. REFERENCES
    # ==========================================
    section_header("References")
    for ref in static_data['references']:
        pdf.set_font("Helvetica", style="B", size=10)
        pdf.cell(0, 5, safe_text(f"{ref['name']} - {ref['title']}"), ln=1)

        pdf.set_font("Helvetica", size=10)
        pdf.cell(0, 5, safe_text(
            f"{ref['company']}  |  {ref['phone']}  |  {ref['email']}"), ln=1)
        pdf.ln(2)

    pdf.output(output_filename)
