# from flask import Flask, render_template, make_response
# import pdfkit
# from PyPDF2 import PdfReader, PdfWriter
# import io

# app = Flask(__name__)

# @app.route("/pdf")
# def generate_pdf():
    # data = {
    #     "name": "DHANUSH T S",
    #     "email": "tsdhanush169@gmail.com",
    #     "phone": "+91-7200281984",
    #     "linkedin": "https://www.linkedin.com/in/dhanush-t-s-734481271/",
    #     "github": "https://github.com/dhanush-ts",
    #     "profile_summary":
    #         "Data Scientist, Data Analyst, and Full Stack Developer with 2+ years of experience delivering 10+ data-driven applications and dashboards. Proven ability to increase process efficiency by up to 75% using AI and automation. Adept in Next.js, React.js, Django, and Python to build scalable and integrated data solutions.",
    #     "functional_areas": [
    #         "ML",
    #         "Full Stack Development",
    #         "Data Visualization",
    #         "Deep Learning",
    #         "Business",
    #         "DevOps"
    #     ],
    #     "technical_skills": [
    #         "<b>Advanced Excel</b> – Pivot Tables, Charts, Lookups, Power Query, Power Pivot (10+ dashboards)",
    #         "<b>Power BI</b> – ETL, DAX, Data Modeling, Reports, Dashboards (20+ visualizations)",
    #         "<b>SQL</b> – Complex queries, Joins, CTEs, Recursive CTEs, Window Functions (5000+ rows processed/day)",
    #         "<b>Python</b> – Django (DRF, Celery), ML pipelines, Data preprocessing (15+ models built)",
    #         "<b>Next.js & React.js</b> – Redux, SSR, Auth, API Integration, Hooks, SSG (10+ web apps deployed)"
    #     ],
    #     "project1_title": "Inventory Management System [Web Application & Data Analytics]",
    #     "project1_duration": "12/2024 – 01/2025",
    #     "project1_points": [
    #         "Reduced manual stock management effort by 90% using Vite.js and Django backend",
    #         "Tracked 1000+ products with QR scanning across 3+ inventory zones (kitchen, freezer, fridge)",
    #         "Forecasted weekly sales using 12 months of historical data, reducing raw waste by 30%",
    #         "Saved 10+ man-hours/week by automating admin tasks and real-time reporting"
    #     ],
    #     "project2_title": "AI-Powered Smart Classroom Automation [Web Application & ML]",
    #     "project2_duration": "06/2024 – 12/2024",
    #     "project2_points": [
    #         "Automated attendance for 200+ students using InsightFace, saving 20+ hours/month",
    #         "Increased engagement by 50% with real-time monitoring via YOLOv8 object detection",
    #         "Improved student performance by 45% through AI-driven personalized learning paths",
    #         "Reduced dropout rate by 30% and absenteeism by 35% with 60+ smart notifications sent/month"
    #     ],
    #     "achievements": [
    #         "Winner, Smart India Hackathon (National Level) – ₹1,00,000 prize, Top 5 among 500+ teams",
    #         "Winner, HackMeggedon at REC – ₹10,000 prize, out of 300+ teams",
    #         "Winner, CyberShield Hackathon – $330 prize, competed with 50+ elite teams",
    #         "Winner, Codeathon 2.0 – ₹10,000 prize, ranked 1st among 50+ colleges",
    #         "Winner, Park College Codeathon – ₹1,500 prize, from 600+ participants",
    #         "Winner, Conociothon – ₹1,000 prize, 1st among 100+ teams",
    #         "5+ additional coding competitions won in state-level symposiums"
    #     ],
    #     "volunteer_experience": [
    #         "Facilitated 100+ students' entry into the data field as Chennai CoE volunteer (since 2023)",
    #         "Created 50+ LinkedIn posts on ML & analytics, reaching 30,000+ impressions",
    #         "Mentored 30+ mentees via Topmate with 4.9★ avg. feedback rating for career support"
    #     ],
    #     "education": {
    #         "degree": "Bachelor of Technology [B.Tech] in Artificial Intelligence and Data Science",
    #         "duration": "08/2023 – Present",
    #         "institute": "Rajalakshmi Engineering College",
    #         "roles": "Tech Associate at DEVS Club, Tech-Ops at GDG; 3+ events coordinated; 2 technical talks delivered"
    #     }
    # }

#     rendered = render_template("template.html", data=data)
    
#     full_pdf = pdfkit.from_string(rendered, False)

#     # Slice only the first page using PyPDF2
#     pdf_reader = PdfReader(io.BytesIO(full_pdf))
#     pdf_writer = PdfWriter()

#     pdf_writer.add_page(pdf_reader.pages[0])  # only first page

#     # Write to bytes buffer
#     output_stream = io.BytesIO()
#     pdf_writer.write(output_stream)
#     output_stream.seek(0)

#     # Return sliced PDF
#     response = make_response(output_stream.read())
#     response.headers["Content-Type"] = "application/pdf"
#     # response.headers["Content-Disposition"] = "inline; filename=resume_one_page.pdf"
#     response.headers["Content-Disposition"] = "attachment; filename=resume_one_page.pdf"
#     return response

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, make_response, request
import pdfkit
from PyPDF2 import PdfReader, PdfWriter
import io

app = Flask(__name__)

@app.route("/pdf", methods=["POST"])
def generate_pdf():
    # ✅ Step 1: Parse JSON body
    data = request.get_json()

    if not data:
        return {"error": "Invalid or missing JSON"}, 400

    # ✅ Step 2: Render HTML with Jinja2
    rendered = render_template("template.html", data=data["data"])

    # ✅ Step 3: Generate full PDF
    full_pdf = pdfkit.from_string(rendered, False)

    # ✅ Step 4: Slice to only first page using PyPDF2
    pdf_reader = PdfReader(io.BytesIO(full_pdf))
    pdf_writer = PdfWriter()
    pdf_writer.add_page(pdf_reader.pages[0])

    output_stream = io.BytesIO()
    pdf_writer.write(output_stream)
    output_stream.seek(0)

    # ✅ Step 5: Return sliced PDF as downloadable file
    response = make_response(output_stream.read())
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=resume_one_page.pdf"
    return response

if __name__ == "__main__":
    app.run(debug=True)
