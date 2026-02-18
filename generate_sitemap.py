import os
from datetime import datetime

# ---------------------------
# CONFIGURATION
# ---------------------------
BASE_URL = "https://rainhunterforex.com"  # Your website
ROOT_DIR = "."  # Root directory of HTML files
DEFAULT_PRIORITY = "0.8"
INDEX_PRIORITY = "1.0"
CHANGEFREQ = "weekly"

# ---------------------------
# FUNCTION TO SCAN HTML FILES
# ---------------------------
def get_html_files(root_dir):
    html_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.relpath(os.path.join(subdir, file), root_dir)
                html_files.append(path.replace("\\", "/"))
    return html_files

# ---------------------------
# GENERATE SITEMAP.XML
# ---------------------------
def generate_sitemap(html_files, base_url):
    today = datetime.today().strftime("%Y-%m-%d")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n'

    for file in html_files:
        priority = INDEX_PRIORITY if file.lower() in ["index.html", "./index.html"] else DEFAULT_PRIORITY
        sitemap += "  <url>\n"
        sitemap += f"    <loc>{base_url}/{file}</loc>\n"
        sitemap += f"    <lastmod>{today}</lastmod>\n"
        sitemap += f"    <changefreq>{CHANGEFREQ}</changefreq>\n"
        sitemap += f"    <priority>{priority}</priority>\n"
        sitemap += "  </url>\n\n"

    sitemap += "</urlset>"
    return sitemap

# ---------------------------
# SAVE SITEMAP.XML
# ---------------------------
def save_sitemap(content, filename="sitemap.xml"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{filename} generated successfully!")

# ---------------------------
# MAIN SCRIPT
# ---------------------------
if __name__ == "__main__":
    html_files = get_html_files(ROOT_DIR)
    sitemap_content = generate_sitemap(html_files, BASE_URL)
    save_sitemap(sitemap_content)
