from analyzer.model import LogEntry, AnalysisResult

class ErrorCountRule:
    name = "error-count"

    def __init__(self, threshold: int):
        if threshold <= 0:
            raise ValueError("threshold must be positive")
        self._threshold = threshold

    def analyze(self, entries):
        errors = [
            (i, e) for i, e in enumerate(entries)
            if e.level == "ERROR"
        ]

        if len(errors) >= self._threshold:
            return [
                AnalysisResult(
                    rule=self.name,
                    detail=f"{len(errors)} errors detected (threshold={self._threshold})",
                    line=None,
                )
            ]

        return []
