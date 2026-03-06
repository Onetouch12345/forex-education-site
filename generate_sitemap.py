import os

base_url = "https://onetouch12345.github.io/forex-education-site/"

# Define important pages only
pages = [
    "index.html",
    "learn.html",
    "analysis.html",
    "blog.html",
    "tools.html",
    "brokers.html",
    "contact.html"
]

with open("sitemap.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for page in pages:
        f.write("<url>\n")
        f.write(f"<loc>{base_url}{page}</loc>\n")
        f.write("<changefreq>weekly</changefreq>\n")
        f.write("<priority>0.8</priority>\n")
        f.write("</url>\n")

    f.write("</urlset>")
