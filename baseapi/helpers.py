import os
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import uuid

def save_pdf(params: dict):
    try:
        # Load the HTML template
        template = get_template("pdf.html")
        html = template.render(params)
        response = BytesIO()

        # Generate the PDF
        pdf_status = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

        if pdf_status.err:
            print("Error during PDF generation.")
            return '', False

        # Create a unique file name
        file_name = f"{uuid.uuid4()}.pdf"
        
        # Get the output path
        output_path = os.path.join(settings.MEDIA_ROOT, file_name)

        # Ensure the directory exists before saving the file
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        with open(output_path, 'wb+') as output_file:
            output_file.write(response.getvalue())

        print(f"Generated PDF file path: {output_path}")  # Add this line for debugging

        return file_name, True

    except Exception as e:
        print("Exception occurred during PDF generation:", e)
        return '', False
