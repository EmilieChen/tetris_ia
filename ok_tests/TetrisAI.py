test = {
    "name": "TetrisAI",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]);\n>>> piece = Tetromino.create('T').place_at(1,2);\n>>> state = (board, piece);\n>>> \n>>> policy = TetrisAI();\n>>> params = [0.17, 0.55, 0.16, 0.12];\n>>> action = policy(state, params);\n>>> \n>>> action\n3",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]);\n>>> piece = Tetromino.create('O').place_at(2,2);\n>>> state = (board, piece);\n>>> \n>>> policy = TetrisAI();\n>>> params = [0.1, 0.1, 1, 0.1];\n>>> action = policy(state, params);\n>>> \n>>> action\n2",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]);\n>>> piece = Tetromino.create('S').place_at(1,2);\n>>> state = (board, piece);\n>>> \n>>> policy = TetrisAI();\n>>> params = [0.17, 0.55, 0.16, 0.12];\n>>> action = policy(state, params);\n>>> \n>>> action\n4",
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