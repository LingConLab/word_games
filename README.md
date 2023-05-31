# word_games
Python package for creating language games from your own data

Пример использования:

```python
import word_games

proj = word_games.Project("test.md", "russian_nouns.txt")
proj.compile_to_web("test_project")
```

По пути ```test_project``` появится папка, содержащая `app.py`, `Games.py` и папку `templates`, в которой хранятся html страницы. Сайт может быть запущен локально с помощью запуска `app.py`