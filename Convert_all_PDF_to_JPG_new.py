import pdf2image
from pathlib import Path

def convert_pdf_to_jpg(pdf_path, output_folder, quality=95, dpi=300, output_format='JPEG'):
    print(f"Converting {pdf_path} with dpi={dpi} and quality={quality}...")
    output_folder.mkdir(parents=True, exist_ok=True)
    
    try:
        images = pdf2image.convert_from_path(str(pdf_path), dpi=dpi)
    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        return
    
    for i, image in enumerate(images, start=1):
        output_file = output_folder / f"{pdf_path.stem}_{i}_high_quality.{output_format.lower()}"
        try:
            image.save(output_file, output_format, quality=quality)
            print(f"Saved {output_file}")
        except Exception as e:
            print(f"Error saving {output_file}: {e}")

def convert_all_pdfs_to_jpg(directory, output_folder_name="pdf_images_high_dpi", quality=95, dpi=300, output_format='JPEG'):
    directory = Path(directory)
    output_folder = directory / output_folder_name
    pdf_files = list(directory.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found.")
        return
    
    for pdf_file in pdf_files:
        convert_pdf_to_jpg(pdf_file, output_folder, quality=quality, dpi=dpi, output_format=output_format)

if __name__ == "__main__":
    current_directory = Path(__file__).resolve().parent
    print(f"Converting PDFs in {current_directory} to {current_directory / 'pdf_images_high_dpi'}...")
    # Adjust quality, dpi, and output_format as needed.
    convert_all_pdfs_to_jpg(current_directory, quality=95, dpi=300, output_format='JPEG')
