test = {
    "name": "cumulative_wells",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> board = Board([[0, 0, 0, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 1, 1, 1, 1, 1]]);\n>>> cumulative_wells(board)\n6",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0],\n...                [0, 1, 1, 0, 1, 1],\n...                [0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 0, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [1, 0, 0, 0, 0, 1],\n...                [0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 1, 1, 1],\n...                [1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 1, 1]]);\n>>> cumulative_wells(board)\n24",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> board = Board([[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],\n...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]]);\n>>> cumulative_wells(board)\n3",
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