import yaml
from pathlib import Path


def load_config():
    base_path = Path(__file__).parent.parent
    full_path = base_path / "resources" / "application.yml"

    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_config()
