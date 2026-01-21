import camelot
def extract_pdf_tables(filepath):
    tables = camelot.read_pdf(filepath, flavor="stream", pages="all")
    dfs = []
    for table in tables:
        dfs.append(table.df)
    return dfs
