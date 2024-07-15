# import camelot
# tables = camelot.read_pdf(r"C:\Users\mohit\Desktop\Infineon-XC167_16-DS-v01_03-en.pdf",pages="25",flavor='lattice')
 
# type(tables) 
# tables[0].df
# a=str(tables[0].df)
# a

#######################################################################
# concept(dimention)

# from camelot import utils
# layout, dim = utils.get_page_layout(file_name)

import camelot
import gradio as gr
import pandas as pd

def extract_table_from_pdf(pdf_path, page_num):
    # Read tables from the PDF using Camelot
    tables = camelot.read_pdf(pdf_path, pages=str(page_num), flavor='lattice')
    
    # Assuming there's only one table on the page
    table = tables[0]
    
    # Convert the table to a pandas dataframe
    table_df = table.df
    
    return table_df

# Gradio interface function
def gradio_app(pdf_file, page_number):
    pdf_path = pdf_file.name
    table_df = extract_table_from_pdf(pdf_path, page_number)
    
    # Ensure the dataframe columns and data are strings to avoid display issues in Gradio
    table_df.columns = table_df.columns.astype(str)
    table_df = table_df.astype(str)
    
    return table_df

# Interface setup
inputs = [
    gr.File(label="Upload PDF"),
    gr.Number(label="Page Number", value=1, precision=0)
]

outputs = gr.Dataframe(label="Extracted Table Data")

# Launch the Gradio interface
gr.Interface(fn=gradio_app, inputs=inputs, outputs=outputs, 
             title="PDF Table Extraction",
             description="Upload a PDF and specify the page number to extract tables using Camelot.").launch()























# tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite

# tables[0]

# tables[0].parsing_report
# {
#     'accuracy': 99.02,
#     'whitespace': 12.24,
#     'order': 1,
#     'page': 1
# }

# tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite

# tables[0].df # get a pandas DataFrame!