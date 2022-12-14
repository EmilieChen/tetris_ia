test = {
    "name": "hole_depths",
    "points": 4,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> hole_depths(board)\n4",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 0, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 0, 0, 0, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 1, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 1, 1]]);\n>>> hole_depths(board)\n7",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]]);\n>>> hole_depths(board)\n16",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 1, 0, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 0, 1],\n...                [1, 0, 1, 1, 0, 1],\n...                [1, 0, 1, 1, 1, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 1, 1],\n...                [0, 0, 1, 0, 0, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> hole_depths(board)\n11",
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