import fitz  # PyMuPDF
import gradio as gr

def extract_text_from_pdf(pdf_path, page_num):
    # Open the PDF document
    pdf_document = fitz.open(pdf_path)
    
    # Load the specified page (page_num - 1 because PyMuPDF page index starts at 0)
    page = pdf_document.load_page(page_num - 1)
    
    # Extract the text from the page
    text = page.get_text("text")
    
    pdf_document.close()
    
    return text

# Gradio interface function
def gradio_app(pdf_file, page_number):
    pdf_path = pdf_file.name
    extracted_text = extract_text_from_pdf(pdf_path, page_number)
    return extracted_text

# Interface setup
inputs = [
    gr.File(label="Upload PDF"),
    gr.Number(label="Page Number", value=1, precision=0)
]

outputs = gr.Textbox(label="Extracted Text")

# Launch the Gradio interface
gr.Interface(fn=gradio_app, inputs=inputs, outputs=outputs, 
             title="PDF Text Extraction",
             description="Upload a PDF and specify the page number to extract text using PyMuPDF.").launch()
