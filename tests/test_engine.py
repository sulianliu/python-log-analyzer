from analyzer.engine import AnalyzerEngine
from analyzer.model import LogEntry, AnalysisResult


class DummyRule:
    name = "dummy"

    def analyze(self, entries):
        return [
            AnalysisResult(rule=self.name, detail="ok", line=None)
        ]


def test_engine_runs_all_rules():
    engine = AnalyzerEngine([DummyRule()])

    entries = [LogEntry("t", "INFO", "msg")]
    results = engine.run(entries)

    assert len(results) == 1
    assert results[0].rule == "dummy"
