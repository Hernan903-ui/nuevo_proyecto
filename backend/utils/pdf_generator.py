from fpdf import FPDF

class PDFGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Reporte de Inventario', border=0, ln=1, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

def generate_pdf(data, filename='report.pdf'):
    """
    Genera un archivo PDF con los datos proporcionados.
    """
    pdf = PDFGenerator()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    
    for i, row in enumerate(data, start=1):
        pdf.cell(0, 10, f"{i}. Producto: {row['product_id']} | Acción: {row['action']} | Cantidad: {row['quantity']} | Fecha: {row['date']}", ln=1)
    
    pdf.output(filename)
    print(f"PDF generado: {filename}")