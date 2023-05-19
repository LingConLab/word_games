import markdown
import re
from web_template.games.Games import *
import os
import shutil


class Project:
    def __init__(self, md_path, dict_path) -> None:
        self.md_path = md_path
        self.dict_path = dict_path

    def compile_to_web(self, web_path):
        os.mkdir(web_path)
        _ = os.path.join(web_path, "templates")
        os.mkdir(_)
        _ = os.path.join(web_path, "games")
        os.mkdir(_)

        with open(self.md_path, 'r', encoding="utf-8") as f, open(f"{web_path}/templates/base.html", 'w', encoding="utf-8") as h:
            md_text = f.read()
            html_text = markdown.markdown(md_text)
            game = self.__parse_games(html_text)
            with open(f"web_template/games/{game[0]}.html", 'r', encoding="utf-8") as c:
                html_text = re.sub(
                    r'<p><code>.*<\/code><\/p>', c.read(), html_text)
                h.write("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                
                                <!-- Заголовок страницы -->
                                <title>{% block title %}{% endblock %}</title>
                                
                                <link rel="icon" type="image/png" href="{{ url_for('static', filename='img/favic.png') }}">
                                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
                                <link href="https://fonts.googleapis.com/css?family=Lora:400,700&display=swap" rel="stylesheet" type="text/css" />

                            </head>
                            <body>""")
                h.write(html_text)
                h.write("""</body>
                            </html>
                            """)

        with open("web_template/app.py", 'r', encoding="utf-8") as temp, open(f"{web_path}/app.py", 'w', encoding="utf-8") as new:
            code = temp.read()
            print("hi")
            code = re.sub('\"GAME_MASK\"',
                          game[1]+f'("{self.dict_path}")', code)
            new.write(code)

        shutil.copy("web_template/games/Games.py",
                    f"{web_path}/games/Games.py")

    def __parse_games(self, text):
        games_dict = {
            "HangmanGame": None,
            "CombinerGame": "Combiner"
        }

        game = re.search(r'<p><code>(.*)<\/code><\/p>', text).group(1)
        return game, games_dict[game]
