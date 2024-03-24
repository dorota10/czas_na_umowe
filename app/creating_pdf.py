from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from flask import make_response

def create_pdf(data):

    response = make_response()
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=umowa_najmu.pdf'


    c = canvas.Canvas(response.stream, pagesize=letter)

    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    c.setFont("Verdana", 8)


    text = c.beginText(40, 750)
    text.textLine(f"{data['miejsce_zawarcia']}, {data['data_zawarcia'].strftime('%d-%m-%Y')}")
    text.textLine("Umowa Najmu")
    text.textLine("Umowa zostaje zawarta między:")
    text.textLine(f"{data['imie_wynajmujacego']} {data['nazwisko_wynajmujacego']}, PESEL: {data['pesel_wynajmujacego']}, zwanym dalej Wynajmującym")
    text.textLine("a")
    text.textLine(f"{data['imie_najemcy']} {data['nazwisko_najemcy']}, PESEL: {data['pesel_najemcy']}, zwanym dalej Najemcą.")
    text.textLine(f"Umowa tyczy się nieruchomości znajdującej się na {data['adres_lokalu']}, o powierzchni {data['wielkosc_lokalu']}.")
    text.textLine(f"Czynsz za wynajem wynosi miesięcznie {data['kwota_czynszu']}. Kaucja za lokal wynosi {data['kwota_kaucji']}.")
    text.textLine(f"Kaucja musi zostać uiszczona {data['dni_kaucji']} dni po zawarciu umowy.")
    text.textLine(f"Czynsz należy uiszczać do {data['data_zaplaty_czynszu']} każdego miesiąca.")
    text.textLine(f"Umowa obowiązuje do {data['data_zakonczenia_umowy'].strftime('%d-%m-%Y')}.")

    c.drawText(text)
    c.showPage()
    c.save()

    return response