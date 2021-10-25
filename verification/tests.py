"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["571", 2],
            "answer": "71",
        },
        {
            "input": ["12", 1],
            "answer": "2",
        },
        {
            "input": ["763832", 3],
            "answer": "832",
        },
        {
            "input": ["4368534743453", 5],
            "answer": "87453",
        },
        {
            "input": ["111121", 3],
            "answer": "121",
        },
        {
            "input": ["54", 2],
            "answer": "54",
        }
    ],
    "Extra": [
        {
            "input": ["45", 1],
            "answer": "5",
        },
        {
            "input": ["54997", 2],
            "answer": "99",
        },
        {
            "input": [
                '16383285933376488107769716335121387836084524687971486076526036589610245072878793773409679774783341023289100622985565634155435110412023751504758366716974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850', 
                137
            ],
            "answer": '99999999988974179230108295707946257428929060971704475252304168467635339386587930249331616481009829964427704428337722526713972938626223850'
        }
    ]
}
