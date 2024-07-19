import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def generate_and_show_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter a URL or text to generate QR code.")
        return

    global qr_img
    qr_img = generate_qr_code(data)

    img = qr_img.resize((300, 300), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)

    qr_label.configure(image=img, text="")
    qr_label.image = img

    save_button.configure(state=NORMAL)

def save_qr_code():
    if qr_img is None:
        messagebox.showwarning("No QR Code", "Please generate a QR code first.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_img.save(file_path)
        messagebox.showinfo("Saved", f"QR code saved to {file_path}")

# Create the main application window
root = ttk.Window(themename="darkly")
root.title("Apple Themed QR Code Generator")
root.geometry("600x700")
root.resizable(False, False)

# Create and place the input field
entry_frame = ttk.Frame(root, padding=(20, 20), bootstyle=DARK)
entry_frame.pack(pady=20, padx=20, fill="both", expand=True)

entry_label = ttk.Label(entry_frame, text="Enter URL or Text:", font=("Helvetica", 16), bootstyle=LIGHT)
entry_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

entry = ttk.Entry(entry_frame, width=40, font=("Helvetica", 16), bootstyle=SUCCESS)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the generate button
generate_button = ttk.Button(entry_frame, text="Generate QR Code", command=generate_and_show_qr, bootstyle=SUCCESS, width=20)
generate_button.grid(row=1, column=0, columnspan=2, pady=20)

# Create and place the label to display the QR code
qr_label_frame = ttk.Frame(root, padding=(20, 20), bootstyle=DARK)
qr_label_frame.pack(pady=20, padx=20, fill="both", expand=True)

qr_label = ttk.Label(qr_label_frame, text="Your QR Code will appear here", font=("Helvetica", 18), bootstyle=LIGHT)
qr_label.pack(pady=20)

# Create and place the save button
save_button = ttk.Button(root, text="Save QR Code", command=save_qr_code, state=DISABLED, bootstyle=SUCCESS, width=20)
save_button.pack(pady=20)

qr_img = None  # To hold the QR code image

# Adding tooltips
ToolTip(generate_button, text="Click to generate the QR Code from the entered URL or text", bootstyle=INFO)
ToolTip(save_button, text="Click to save the generated QR Code", bootstyle=INFO)

# Adding icons to buttons (ensure you have the icons in the same directory)
try:
    generate_icon = ImageTk.PhotoImage(Image.open("generate_icon.png").resize((20, 20)))
    generate_button.configure(image=generate_icon, compound=LEFT)

    save_icon = ImageTk.PhotoImage(Image.open("save_icon.png").resize((20, 20)))
    save_button.configure(image=save_icon, compound=LEFT)
except FileNotFoundError:
    print("Icons not found. Make sure 'generate_icon.png' and 'save_icon.png' are in the same directory.")

# Run the application
root.mainloop()
