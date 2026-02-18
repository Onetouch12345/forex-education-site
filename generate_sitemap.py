import os
from datetime import datetime

# ========== CONFIGURATION ==========
site_url = "https://rainhunterforex.com"  # Your website base URL
output_file = "sitemap.xml"              # Output file
html_folder = "."                         # Folder to scan for HTML pages
# ===================================

def get_html_files(folder):
    html_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.relpath(os.path.join(root, file), folder)
                html_files.append(filepath.replace("\\", "/"))
    return html_files

def generate_sitemap(url_list, output):
    now = datetime.now().strftime("%Y-%m-%d")
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    for url in url_list:
        sitemap.append("  <url>")
        sitemap.append(f"    <loc>{site_url}/{url}</loc>")
        sitemap.append(f"    <lastmod>{now}</lastmod>")
        sitemap.append("    <changefreq>weekly</changefreq>")
        sitemap.append("    <priority>0.8</priority>")
        sitemap.append("  </url>")

    sitemap.append("</urlset>")

    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))
    print(f"Sitemap generated: {output}")

if __name__ == "__main__":
    html_pages = get_html_files(html_folder)
    # Exclude hidden files or irrelevant HTML files if needed
    html_pages = [p for p in html_pages if not p.startswith(".")]
    
    generate_sitemap(html_pages, output_file)
