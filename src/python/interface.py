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
