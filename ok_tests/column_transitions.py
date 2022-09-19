test = {
    "name": "column_transitions",
    "points": 2,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> column_transitions(board)\n22",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 0, 1, 0, 0],\n...                [1, 1, 1, 1, 1, 0],\n...                [1, 0, 0, 1, 1, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 0]]);\n>>> column_transitions(board)\n30",
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