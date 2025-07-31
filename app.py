from flask import Flask, render_template, make_response, request
import pdfkit
from PyPDF2 import PdfReader, PdfWriter
import io
import json

app = Flask(__name__)

@app.route("/pdf", methods=["POST"])
def generate_pdf():
    # ✅ Step 1: Parse JSON body
    data = request.get_json()

    if not data:
        return {"error": "Invalid or missing JSON"}, 400
    print(data)
    parsed_dict = json.loads(data.strip())
    # ✅ Step 2: Render HTML with Jinja2
    rendered = render_template("template.html", data=data)

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
