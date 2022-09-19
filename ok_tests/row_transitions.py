test = {
    "name": "row_transitions",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> row_transitions(board)\n20",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]]);\n>>> row_transitions(board)\n32",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 0, 1, 0, 0],\n...                [1, 1, 1, 1, 1, 0],\n...                [1, 0, 0, 1, 1, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 0]]);\n>>> row_transitions(board)\n24",
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