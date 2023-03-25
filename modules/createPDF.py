from fpdf import FPDF, HTMLMixin
import os, tempfile
from modules.txt_logic import *
from modules import main_config


def create_pdf(text_lines, order_number):
    pdf = FPDF(orientation='L', format=(75, 120))
    pdf.add_page()
    pdf.add_font("DejaVu", "", main_config.bot.main_front, uni="utf-8")
    pdf.set_font("DejaVu", "", 20)

    order_number_formatted = f"{order_number // 1000000:03} {order_number // 1000 % 1000:03} {order_number % 1000:03}"

    #################################
    pdf.image(main_config.bot.path_logo, x=5, y=3, w=main_config.bot.size_logo)
    pdf.set_xy(5, 3)

#################################################################
    if main_config.bot.title != "Заголовок":
        title = main_config.bot.title
        pdf.set_xy(35, 3)
        pdf.set_font("DejaVu", "", 15)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 7, title, align='C', border=0)

        pdf.set_xy(30, 3)
        pdf.set_text_color(0)
        width = pdf.get_string_width(title) + 60
        pdf.cell(width, 6, '', align='L', border=1)

    pdf.set_xy(1, 1)
    pdf.cell(118, 53, '', border=1)


    pdf.set_font("DejaVu", "", 25)
    pdf.set_text_color(0)  # Устанавливаем цвет текста в чёрный

    max_chars_per_line = 30
    min_font_size = 5
    max_font_size = 35


    y_position = 15
    pdf.add_font(family="DejaVu", style="", fname=main_config.bot.main_front, uni="utf-8")
    pdf.set_font("DejaVu", size=18, style="")

    y_position = 15
    for number, line in enumerate(text_lines, 0):
        if line != '':
            pdf.set_xy(1, y_position)
            pdf.cell(0,  pdf.font_size, f"{main_config.bot.dict_paragraph[number]}:{line}")
            y_position += pdf.font_size

    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, f'{order_number_formatted}.pdf') # Изменено имя файла на order_number_formatted

    pdf.output(pdf_path)

    return pdf_path