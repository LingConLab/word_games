import markdown
import re

with open("test.md", 'r', encoding="utf-8") as f, open("test.html", 'w', encoding="utf-8") as h:
    md_text = f.read()
    html_text = markdown.markdown(md_text)
    with open("games/CombinerGame.html", 'r', encoding="utf-8") as c:
        html_text = re.sub(r'<p><code>.*<\/code><\/p>', c.read(), html_text)
        h.write(html_text)
