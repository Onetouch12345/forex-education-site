import os

base_url = "https://rainhunterforex.com/"

pages = [f for f in os.listdir() if f.endswith(".html")]

with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for page in pages:
        f.write(f"<url><loc>{base_url}{page}</loc></url>\n")
    f.write("</urlset>")