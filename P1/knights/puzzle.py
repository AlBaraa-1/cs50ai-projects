from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # A said: "I am both a knight and a knave."
    # If A is a knight, the statement must be true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, the statement must be false
    Implication(AKnave, Not(And(AKnight, AKnave))),
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A can't be both
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Not(And(BKnight, BKnave)),  # B can't be both
    # A's statement: "We are both knaves."
    Implication(
        AKnight, And(AKnave, BKnave)
    ),  # If A is a knight, the statement must be true
    Implication(
        AKnave, Not(And(AKnave, BKnave))
    ),  # If A is a knave, the statement must be false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Base identity rules
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A's statement: "We are the same kind"
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # B's statement: "We are of different kinds"
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

AsaidKnight = Symbol("A said 'I am a knight'")
AsaidKnave = Symbol("A said 'I am a knave'")

knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Or(AsaidKnight, AsaidKnave),
    Not(And(AsaidKnight, AsaidKnave)),
    Implication(And(AKnight, AsaidKnight), AKnight),
    Implication(And(AKnave, AsaidKnight), Not(AKnight)),
    Implication(And(AKnight, AsaidKnave), AKnave),
    Implication(And(AKnave, AsaidKnave), Not(AKnave)),
    Implication(BKnight, AsaidKnave),
    Implication(BKnave, Not(AsaidKnave)),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
