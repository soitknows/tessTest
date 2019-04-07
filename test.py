import os
import shutil
import pytesseract as ts
import img2pdf

# LEFT TOP WIDTH HEIGHT
#-------------------------------------------------------------------------------
# 465 40 140 15 --> Invoice
# 485 65 140 15 --> Invoice Date
# 505 80 140 15 --> Invoice Amount
# 489 95 140 15 --> Customer ID
#-------------------------------------------------------------------------------

def get_invoice_text(filename, vendor):
  name = filename.split(".")[0]
  # Copy and rename vendor template UZN file
  shutil.copy(os.path.join(vendor, vendor + ".uzn"), os.path.join(vendor, name + ".uzn"))

  # Extract invoice, date, amount, customer ID using UZN zone file (psm 4)
  text = ts.image_to_string(os.path.join(vendor, filename), config='--psm 4')
  array = text.split('\n')
  # Remove blank lines
  array[:] = [x for x in array if x != ""]
  # Build pip delimeted line
  line = ("|".join(array))
  # Write output
  delim = open(os.path.join(vendor, "out.txt"), "w")
  delim.write(line)

  # Create PDF of image
  with open(os.path.join(name, ".pdf","wb")) as f:
    f.write(img2pdf.convert(filename))


get_invoice_text("invoice2.jpg", "chargebee")
