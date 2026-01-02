# python-log-analyzer

A production-style Python 3 CLI tool for deterministic log analysis, designed with clean architecture and long-term evolvability in mind.

---

## Overview

`python-log-analyzer` is a command-line tool for analyzing application logs in a **deterministic, explainable, and streaming-friendly** way.

The project is intentionally designed as a **clean, framework-free Python 3 codebase**, emphasizing:

- Clear separation of concerns
- Predictable behavior over heuristic inference
- Readability and maintainability
- Incremental evolution toward more advanced analysis (including optional AI-assisted interpretation)

This repository is not a demo or proof-of-concept.  
It is structured as a **long-lived engineering project**.

---

## Key Design Principles

- **Deterministic first**  
  Core analysis logic is rule-based and repeatable. Results should not depend on probabilistic models.

- **Streaming-friendly**  
  Logs are processed line by line to support large files without excessive memory usage.

- **Clean architecture**  
  Parsing, domain models, statistics, and CLI concerns are kept separate.

- **Minimal dependencies**  
  Uses Python standard library wherever possible to reduce complexity.

- **Evolvable by design**  
  The architecture allows future extensions such as structured output formats, time-window analysis, or AI-assisted explanation layers without rewriting the core.

---

## Features (Current)

- Parse structured text logs
- Filter by log level (e.g. ERROR, WARN, INFO)
- Aggregate events by service/component
- Report top-N occurrences
- Robust handling of malformed log lines

---

## Example Usage

```bash
python main.py sample.log --level ERROR --top 5
