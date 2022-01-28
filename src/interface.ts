export interface LetterResult {
  status: "CORRECT" | "PARTIAL" | "INCORRECT" | "MULTI_INSTANCE";
  correctPositions: number[];
  incorrectPositions: number[];
}
