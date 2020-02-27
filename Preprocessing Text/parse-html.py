from bs4 import BeautifulSoup


# Create some HTML code
html = "<div class='full_name'><span style='font-weight:bold'>Masego</span> Azra</div>"

# Parse html
soup = BeautifulSoup(html, "html.parser")

# Find the div with the class "full_name", show text
soup.find("div", { "class" : "full_name" }).text
