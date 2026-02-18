import os
from datetime import datetime

# =========================
# Configuration
# =========================
BASE_URL = "https://rainhunterforex.com"  # Your website URL
SITE_DIR = "./"  # Directory where HTML files are stored
OUTPUT_FILE = "sitemap.xml"

# =========================
# Function to find HTML pages
# =========================
def get_html_pages(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                # Get relative path from SITE_DIR
                rel_dir = os.path.relpath(root, directory)
                rel_file = os.path.join(rel_dir, file) if rel_dir != "." else file
                html_files.append(rel_file.replace("\\", "/"))
    return html_files

# =========================
# Generate sitemap.xml
# =========================
def generate_sitemap():
    pages = get_html_pages(SITE_DIR)
    now = datetime.now().strftime("%Y-%m-%d")
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n'
    
    for page in pages:
        priority = "0.8"
        if page == "index.html":
            priority = "1.0"
        sitemap_content += f"  <url>\n"
        sitemap_content += f"    <loc>{BASE_URL}/{page}</loc>\n"
        sitemap_content += f"    <lastmod>{now}</lastmod>\n"
        sitemap_content += f"    <priority>{priority}</priority>\n"
        sitemap_content += f"  </url>\n\n"
    
    sitemap_content += "</urlset>"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    
    print(f"[✔] Sitemap generated with {len(pages)} pages -> {OUTPUT_FILE}")

# =========================
# Run
# =========================
if __name__ == "__main__":
    generate_sitemap()
