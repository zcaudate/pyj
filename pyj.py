from pathlib import Path

def slurp(path):
  return Path(path).read_text()
