import fitz


def parse_pdf(file_path):
    """
    Extract text from each page of a PDF.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        list: List of dictionaries containing page number and text.
    """

    pages_data = []

    try:
        pdf_document = fitz.open(file_path)

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            text = page.get_text()

            pages_data.append({
                "page": page_number + 1,
                "text": text
            })

        pdf_document.close()

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return pages_data