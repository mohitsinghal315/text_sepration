This project demonstrates a Python script for extracting tables and text from PDF documents. It utilizes Camelot for table extraction and PyMuPDF (Fitz) for text extraction, ensuring accurate separation and display of extracted content.
Objective

The objective of this project is to:

    Extract tables from a PDF using Camelot.
    Extract text blocks from the same PDF using PyMuPDF (Fitz).
    Normalize the coordinates of extracted elements for consistency across different libraries.
    Remove text blocks that fall within detected table boundaries to ensure accurate text-table separation.
    Display the filtered text and detected tables in a Gradio interface for interactive exploration.

How It Works
Libraries Used

    Camelot: Used for extracting tables from PDFs.
    PyMuPDF (Fitz): Used for extracting text blocks from PDFs and converting coordinates.
    Pandas: Used for data manipulation, particularly for handling table data.
    Gradio: Used for creating interactive web interfaces to display extracted content.

Workflow

    Extract Tables Using Camelot:
        Camelot reads tables from the specified PDF file on the specified page.
        Bounding boxes of detected tables are collected to define their spatial locations.

    Extract Text Blocks Using PyMuPDF (Fitz):
        PyMuPDF opens the PDF file and extracts text blocks from the specified page.
        Each text block's bounding box and text content are stored for further processing.

    Normalize Coordinates:
        Convert Camelot's bottom-up coordinate system to PyMuPDF's top-down system.
        Adjust Y-coordinates of table bounding boxes to fit the PDF page's height in PyMuPDF.

    Text-Table Separation:
        Implement a method to check if each text block overlaps with any table's adjusted bounding box.
        Filter out text blocks that overlap with table areas to retain only non-table text.

    Gradio Interface:
        Display the filtered text and the detected tables side by side in a Gradio interface.
        Tables are presented using HTML formatting within the interface to ensure visibility and readability.


Install dependencies:

bash

    pip install -r requirements.txt

Running the Script

bash

python extract_pdf_content.py

Follow the prompts to upload a PDF file and specify the page number for processing.
Example Output

    Filtered text extracted from the specified page, excluding text within detected tables.
    Tables detected in the PDF displayed using HTML in the Gradio interface.









