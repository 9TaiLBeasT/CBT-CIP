#CREATING PAYMENT RECEIPT 

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def draw_header(c, width, height, store_name, store_address):
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.darkblue)
    text_width = c.stringWidth(store_name, "Helvetica-Bold", 24)
    c.drawString((width - text_width) / 2, height - 1 * inch, store_name)

    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    text_width = c.stringWidth(store_address, "Helvetica", 12)
    c.drawString((width - text_width) / 2, height - 1.5 * inch, store_address)

def draw_receipt_details(c, details, y_start, width):
    x_start = 1 * inch
    line_height = 18
    
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(x_start, y_start, f"Date: {details['Date']}")
    c.drawString(width - 2.5 * inch, y_start, f"Receipt No: {details['Receipt No']}")
    y_start -= line_height

    c.drawString(x_start, y_start, f"Customer Name: {details['Customer Name']}")
    c.drawString(width - 2.5 * inch, y_start, f"Mobile No: {details['Mobile No']}")
    y_start -= line_height

    return y_start

def draw_items_table(c, items, y_start, width):
    x_start = 1 * inch
    table_start_y = y_start - 20
    line_height = 14
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(x_start, table_start_y, "Item")
    c.drawString(x_start + 3.5 * inch, table_start_y, "Price (Rs.)")
    
    table_start_y -= line_height + 4

    c.setFont("Helvetica", 12)
    total_amount = 0
    for item, price in items.items():
        c.drawString(x_start, table_start_y, item)
        c.drawString(x_start + 3.5 * inch, table_start_y, f"Rs. {price:.2f}")
        table_start_y -= line_height
        total_amount += price
    
    table_start_y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_start, table_start_y, "Total Amount")
    c.drawString(x_start + 3.5 * inch, table_start_y, f"Rs. {total_amount:.2f}")

    return table_start_y

def draw_borders(c, width, height):
    c.setLineWidth(0.5)
    c.setStrokeColor(colors.black)
    
    c.rect(0.5 * inch, 0.5 * inch, width - 1 * inch, height - 1 * inch)
    
    c.line(0.5 * inch, height - 1.75 * inch, width - 0.5 * inch, height - 1.75 * inch)

def create_receipt(store_name, store_address, receipt_details, items):
    c = canvas.Canvas("payment_receipt.pdf", pagesize=letter)
    width, height = letter

    draw_header(c, width, height, store_name, store_address)
    details_start_y = height - 2 * inch
    details_end_y = draw_receipt_details(c, receipt_details, details_start_y, width)

    c.line(0.5 * inch, details_end_y, width - 0.5 * inch, details_end_y)
    
    draw_items_table(c, items, details_end_y - 20, width)
    draw_borders(c, width, height)

    c.save()

#Main Function
store_name = "ANIME MERCHANDISE"
store_address = "4-164/4, Uppal X Road, Hyderabad, Telangana, 500039. "

receipt_details = {
    "Date": input("Enter the date (YYYY-MM-DD): "),
    "Receipt No": input("Enter the receipt number: "),
    "Customer Name": input("Enter the customer name: "),
    "Mobile No": input("Enter the mobile number: "),
}

num_items = int(input("Enter the number of items purchased: "))
items = {input(f"Enter item {i+1} name: "): float(input(f"Enter item {i+1} price: ")) for i in range(num_items)}
create_receipt(store_name, store_address, receipt_details, items)
print("Receipt generated and saved as payment_receipt.pdf")
