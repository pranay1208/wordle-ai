class LetterResult :
    def __init__(self) -> None:
        self.status : str = ''
        self.correctPositions : list[int] = []
        self.incorrectPositions: list[int] = []

    def newCorrectResult(i: int):
        newResult = LetterResult()
        newResult.status = "CORRECT"
        newResult.correctPositions = [i]
        return newResult

    def newPartialResult(i: int):
        newResult = LetterResult()
        newResult.status = "PARTIAL"
        newResult.incorrectPositions = [i]
        return newResult

    def newIncorrectResult():
        newResult = LetterResult()
        newResult.status = "INCORRECT"
        newResult.incorrectPositions = [j for j in range(5)]
        return newResult

class ConstraintHeuristic:
    def __init__(self) -> None:
        self.numOccurrences : int = 0
        self.posOccurrences : list[int] = [0] * 5

    def addOccurrence(self, position: int) -> None:
        self.numOccurrences += 1
        self.posOccurrences[position] += 1

    def getEliminationScore(self) -> None:
        return self.numOccurrences

    def getPositionScore(self, position: int) -> None:
        if self.numOccurrences == 0:
            return 0
        probabilityCoefficient = 1 - (self.posOccurrences[position] / self.numOccurrences)
        return self.posOccurrences[position] * probabilityCoefficient