import word_games

proj = word_games.Project("test.md", "russian_nouns.txt")
proj.compile_to_web("test_project")