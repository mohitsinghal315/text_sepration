# import camelot

# # Path to your PDF file
# pdf_path = r"C:\Users\mohit\Desktop\Infineon-XC167_16-DS-v01_03-en.pdf"

# # Extract tables from the PDF
# tables = camelot.read_pdf(pdf_path, pages='25')

# # Get bounding boxes of tables
# table_bboxes = []
# for table in tables:
#     bbox = table._bbox
#     table_bboxes.append(bbox)





# import fitz  # PyMuPDF

# # Open the PDF
# pdf_document = fitz.open(pdf_path)

# # Extract text blocks and their bounding boxes
# text_blocks = []
# for page_num in range(24,25):
#     page = pdf_document.load_page(page_num)
#     blocks = page.get_text("blocks")
#     for block in blocks:
#         x0, y0, x1, y1, text = block[:5]
#         text_blocks.append((x0, y0, x1, y1, text))







# # Camelot bounding boxes (bottom-up) to PyMuPDF (top-down) conversion
# page_height = pdf_document[0].rect.height
# normalized_table_bboxes = []
# for bbox in table_bboxes:
#     x0, y0, x1, y1 = bbox
#     normalized_bbox = (x0, page_height - y1, x1, page_height - y0)
#     normalized_table_bboxes.append(normalized_bbox)





# # Function to check if a text block is within a table bounding box
# def is_within(bbox1, bbox2):
#     x0, y0, x1, y1 = bbox1
#     X0, Y0, X1, Y1 = bbox2
#     return x0 >= X0 and y0 >= Y0 and x1 <= X1 and y1 <= Y1

# # Remove text blocks within table bounding boxes
# filtered_text_blocks = []
# for block in text_blocks:
#     if not any(is_within(block[:4], table_bbox) for table_bbox in normalized_table_bboxes):
#         filtered_text_blocks.append(block)

# # Output filtered text blocks
# for block in filtered_text_blocks:
#     print(block[4])  # Print the remaining text













# import gradio as gr
# import camelot
# import fitz  # PyMuPDF

# def process_pdf(pdf_file, page_number):
#     # Extract tables from the PDF using Camelot
#     tables = camelot.read_pdf(pdf_file.name, pages=str(page_number))

#     # Get bounding boxes of tables
#     table_bboxes = []
#     for table in tables:
#         bbox = table._bbox
#         table_bboxes.append(bbox)

#     # Open the PDF using PyMuPDF
#     pdf_document = fitz.open(pdf_file.name)

#     # Extract text blocks and their bounding boxes
#     text_blocks = []
#     page = pdf_document.load_page(page_number - 1)
#     blocks = page.get_text("blocks")
#     for block in blocks:
#         x0, y0, x1, y1, text = block[:5]
#         text_blocks.append((x0, y0, x1, y1, text))

#     # Camelot bounding boxes (bottom-up) to PyMuPDF (top-down) conversion
#     page_height = pdf_document[0].rect.height
#     normalized_table_bboxes = []
#     for bbox in table_bboxes:
#         x0, y0, x1, y1 = bbox
#         normalized_bbox = (x0, page_height - y1, x1, page_height - y0)
#         normalized_table_bboxes.append(normalized_bbox)

#     # Function to check if a text block is within a table bounding box
#     def is_within(bbox1, bbox2):
#         x0, y0, x1, y1 = bbox1
#         X0, Y0, X1, Y1 = bbox2
#         return x0 >= X0 and y0 >= Y0 and x1 <= X1 and y1 <= Y1

#     # Remove text blocks within table bounding boxes
#     filtered_text_blocks = []
#     for block in text_blocks:
#         if not any(is_within(block[:4], table_bbox) for table_bbox in normalized_table_bboxes):
#             filtered_text_blocks.append(block)

#     # Combine the remaining text blocks into a single string
#     remaining_text = "\n".join(block[4] for block in filtered_text_blocks)
    
#     return remaining_text

# # Define Gradio inputs and outputs
# pdf_input = gr.File(label="Upload PDF")
# page_number_input = gr.Number(default=1, label="Page Number")
# output_text = gr.Textbox(label="Filtered Text")

# # Create the Gradio interface
# interface = gr.Interface(fn=process_pdf, inputs=[pdf_input, page_number_input], outputs=output_text)

# # Launch the Gradio app
# interface.launch()







# import gradio as gr
# import camelot
# import fitz  # PyMuPDF

# def process_pdf(pdf_file, page_number):
#     # Extract tables from the PDF using Camelot
#     tables = camelot.read_pdf(pdf_file.name, pages=str(page_number))

#     # Get bounding boxes of tables
#     table_bboxes = []
#     for table in tables:
#         bbox = table._bbox
#         table_bboxes.append(bbox)

#     # Open the PDF using PyMuPDF
#     pdf_document = fitz.open(pdf_file.name)

#     # Extract text blocks and their bounding boxes
#     text_blocks = []
#     page = pdf_document.load_page(page_number - 1)
#     blocks = page.get_text("blocks")
#     for block in blocks:
#         x0, y0, x1, y1, text = block[:5]
#         text_blocks.append((x0, y0, x1, y1, text))

#     # Camelot bounding boxes (bottom-up) to PyMuPDF (top-down) conversion
#     page_height = pdf_document[0].rect.height
#     normalized_table_bboxes = []
#     for bbox in table_bboxes:
#         x0, y0, x1, y1 = bbox
#         normalized_bbox = (x0, page_height - y1, x1, page_height - y0)
#         normalized_table_bboxes.append(normalized_bbox)

#     # Function to check if a text block is within a table bounding box
#     def is_within(bbox1, bbox2):
#         x0, y0, x1, y1 = bbox1
#         X0, Y0, X1, Y1 = bbox2
#         return x0 >= X0 and y0 >= Y0 and x1 <= X1 and y1 <= Y1

#     # Remove text blocks within table bounding boxes
#     filtered_text_blocks = []
#     for block in text_blocks:
#         if not any(is_within(block[:4], table_bbox) for table_bbox in normalized_table_bboxes):
#             filtered_text_blocks.append(block)

#     # Combine the remaining text blocks into a single string
#     remaining_text = "\n".join(block[4] for block in filtered_text_blocks)
    
#     return remaining_text

# # Define Gradio inputs and outputs
# pdf_input = gr.File(label="Upload PDF")
# page_number_input = gr.Number(value=1, label="Page Number")
# output_text = gr.Textbox(label="Filtered Text")

# # Create the Gradio interface
# interface = gr.Interface(fn=process_pdf, inputs=[pdf_input, page_number_input], outputs=output_text)

# # Launch the Gradio app
# interface.launch()






# import gradio as gr
# import camelot
# import fitz  # PyMuPDF
# import pandas as pd

# def process_pdf(pdf_file, page_number):
#     # Extract tables from the PDF using Camelot
#     tables = camelot.read_pdf(pdf_file.name, pages=str(page_number))

#     # Get bounding boxes of tables
#     table_bboxes = []
#     for table in tables:
#         bbox = table._bbox
#         table_bboxes.append(bbox)

#     # Generate HTML to display the tables
#     tables_html = ""
#     for i, table in enumerate(tables):
#         table_df = table.df
#         tables_html += f"<h4>Table {i + 1}</h4>"
#         tables_html += table_df.to_html(index=False)
    
#     # Open the PDF using PyMuPDF
#     pdf_document = fitz.open(pdf_file.name)

#     # Extract text blocks and their bounding boxes
#     text_blocks = []
#     page = pdf_document.load_page(page_number - 1)
#     blocks = page.get_text("blocks")
#     for block in blocks:
#         x0, y0, x1, y1, text = block[:5]
#         text_blocks.append((x0, y0, x1, y1, text))

#     # Camelot bounding boxes (bottom-up) to PyMuPDF (top-down) conversion
#     page_height = pdf_document[0].rect.height
#     normalized_table_bboxes = []
#     for bbox in table_bboxes:
#         x0, y0, x1, y1 = bbox
#         normalized_bbox = (x0, page_height - y1, x1, page_height - y0)
#         normalized_table_bboxes.append(normalized_bbox)

#     # Function to check if a text block is within a table bounding box
#     def is_within(bbox1, bbox2):
#         x0, y0, x1, y1 = bbox1
#         X0, Y0, X1, Y1 = bbox2
#         return x0 >= X0 and y0 >= Y0 and x1 <= X1 and y1 <= Y1

#     # Remove text blocks within table bounding boxes
#     filtered_text_blocks = []
#     for block in text_blocks:
#         if not any(is_within(block[:4], table_bbox) for table_bbox in normalized_table_bboxes):
#             filtered_text_blocks.append(block)

#     # Combine the remaining text blocks into a single string
#     remaining_text = "\n".join(block[4] for block in filtered_text_blocks)
    
#     return remaining_text, tables_html

# # Define Gradio inputs and outputs
# pdf_input = gr.File(label="Upload PDF")
# page_number_input = gr.Number(value=1, label="Page Number")
# output_text = gr.Textbox(label="Filtered Text")
# tables_output = gr.HTML(label="Detected Tables")

# # Create the Gradio interface
# interface = gr.Interface(fn=process_pdf, inputs=[pdf_input, page_number_input], outputs=[output_text, tables_output])

# # Launch the Gradio app
# interface.launch()






import gradio as gr
import camelot
import fitz  # PyMuPDF
import pandas as pd

def process_pdf(pdf_file, page_number):
    # Extract tables from the PDF using Camelot
    tables = camelot.read_pdf(pdf_file.name, pages=str(page_number))

    # Get bounding boxes of tables
    table_bboxes = []
    for table in tables:
        bbox = table._bbox
        table_bboxes.append(bbox)

    # Generate HTML to display the tables with custom CSS for better visibility
    tables_html = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
    """
    for i, table in enumerate(tables):
        table_df = table.df
        tables_html += f"<h4>Table {i + 1}</h4>"
        tables_html += table_df.to_html(index=False, escape=False)
    
    # Open the PDF using PyMuPDF
    pdf_document = fitz.open(pdf_file.name)

    # Extract text blocks and their bounding boxes
    text_blocks = []
    page = pdf_document.load_page(page_number - 1)
    blocks = page.get_text("blocks")
    for block in blocks:
        x0, y0, x1, y1, text = block[:5]
        text_blocks.append((x0, y0, x1, y1, text))

    # Camelot bounding boxes (bottom-up) to PyMuPDF (top-down) conversion
    page_height = pdf_document[0].rect.height
    normalized_table_bboxes = []
    for bbox in table_bboxes:
        x0, y0, x1, y1 = bbox
        normalized_bbox = (x0, page_height - y1, x1, page_height - y0)
        normalized_table_bboxes.append(normalized_bbox)

    # Function to check if a text block is within a table bounding box
    def is_within(bbox1, bbox2):
        x0, y0, x1, y1 = bbox1
        X0, Y0, X1, Y1 = bbox2
        return x0 >= X0 and y0 >= Y0 and x1 <= X1 and y1 <= Y1

    # Remove text blocks within table bounding boxes
    filtered_text_blocks = []
    for block in text_blocks:
        if not any(is_within(block[:4], table_bbox) for table_bbox in normalized_table_bboxes):
            filtered_text_blocks.append(block)

    # Combine the remaining text blocks into a single string
    remaining_text = "\n".join(block[4] for block in filtered_text_blocks)
    
    return remaining_text, tables_html

# Define Gradio inputs and outputs
pdf_input = gr.File(label="Upload PDF")
page_number_input = gr.Number(value=1, label="Page Number")
output_text = gr.Textbox(label="Filtered Text")
tables_output = gr.HTML(label="Detected Tables")

# Create the Gradio interface
interface = gr.Interface(fn=process_pdf, inputs=[pdf_input, page_number_input], outputs=[output_text, tables_output])

# Launch the Gradio app
interface.launch()
