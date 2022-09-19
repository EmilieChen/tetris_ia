test = {
    "name": "landing_height",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 0, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 0, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> tetro = Tetromino.create('T', (1, 2)).rotate_left();\n>>> board = board.add(tetro);\n>>> landing_height(board, tetro)\n4",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]);\n>>> tetro = Tetromino.create('T', (1, 7)).rotate_left();\n>>> board = board.add(tetro);\n>>> landing_height(board, tetro)\n5",
                    "hidden": False,
                    "locked": False
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}