import zipfile
import re
import os

pptx_path = r"d:\9. Learn\12. llm wiki\temp\Java_Atomic_Concurrency_Patterns.pptx"
md_path = r"d:\9. Learn\12. llm wiki\raw\papers\java-atomic-concurrency-patterns.md"

def extract_text_from_pptx(pptx_path, md_path):
    with zipfile.ZipFile(pptx_path, 'r') as z:
        # Get slide files
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        
        # Sort slides by number
        slide_files.sort(key=lambda x: int(re.search(r'slide(\d+)\.xml', x).group(1)))
        
        md_content = "---\n"
        md_content += "title: \"Java Atomic Concurrency Patterns\"\n"
        md_content += "source: \"temp/Java_Atomic_Concurrency_Patterns.pptx\"\n"
        md_content += "date_added: 2026-04-24\n"
        md_content += "tags: [concept, java, concurrency, atomic]\n"
        md_content += "aliases: [java-atomic, concurrency-patterns]\n"
        md_content += "status: draft\n"
        md_content += "summary: \"Tài liệu về Java Atomic Concurrency Patterns\"\n"
        md_content += "---\n\n"
        md_content += "# Java Atomic Concurrency Patterns\n\n"
        
        for slide_file in slide_files:
            xml_content = z.read(slide_file).decode('utf-8')
            
            slide_num = re.search(r'slide(\d+)\.xml', slide_file).group(1)
            md_content += f"## Slide {slide_num}\n\n"
            
            # Extract texts grouped by paragraphs <a:p>
            paragraphs = re.findall(r'<a:p\b[^>]*>(.*?)</a:p>', xml_content)
            for p in paragraphs:
                p_texts = re.findall(r'<a:t\b[^>]*>(.*?)</a:t>', p)
                if p_texts:
                    line = "".join(p_texts)
                    md_content += "- " + line + "\n"
            md_content += "\n"
            
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Successfully extracted text to {md_path}")

if __name__ == "__main__":
    extract_text_from_pptx(pptx_path, md_path)
