import locale

def format_currency(value):
            locale.setlocale(locale.LC_ALL,'')

            formatted_value = locale.currency(value, grouping=True)

            return formatted_value


with open("blast",'r') as orig_blast_file, open("final_blast_file","w") as refined_file:
 
    for figure in orig_blast_file:
        cleaned_figure = figure.strip()
        if cleaned_figure:
            numeric_value = float(cleaned_figure)
            
            refined_file.write(format_currency(numeric_value))
            refined_file.write('\n')
    

print(format_currency(225434))