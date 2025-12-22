'''
Handles export to Excel, PDF, or Markdown.
'''

def export_to_excel(data: dict, filename: str):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_excel(filename,index=False)