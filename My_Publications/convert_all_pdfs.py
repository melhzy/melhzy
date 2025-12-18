import PyPDF2
import os
import glob

def pdf_to_txt(pdf_path):
    """Extract text from PDF and save to TXT file."""
    txt_path = pdf_path.replace('.pdf', '.txt')
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text_content = []
            
            print(f"Processing: {os.path.basename(pdf_path)}")
            print(f"Total pages: {len(pdf_reader.pages)}")
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()
                text_content.append(f"\n{'='*80}\n")
                text_content.append(f"PAGE {page_num}\n")
                text_content.append(f"{'='*80}\n\n")
                text_content.append(text)
            
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(''.join(text_content))
            
            print(f"[SUCCESS] Created: {os.path.basename(txt_path)}\n")
            return True
            
    except Exception as e:
        print(f"[ERROR] Error processing {os.path.basename(pdf_path)}: {str(e)}\n")
        return False

if __name__ == "__main__":
    # Find all PDFs in My_Publications directory recursively
    pdf_files = glob.glob('My_Publications/**/*.pdf', recursive=True)
    
    print(f"Found {len(pdf_files)} PDF files to convert\n")
    print("="*80)
    print()
    
    success_count = 0
    for pdf_path in pdf_files:
        if pdf_to_txt(pdf_path):
            success_count += 1
    
    print("="*80)
    print(f"\nCompleted: {success_count}/{len(pdf_files)} files converted successfully")
