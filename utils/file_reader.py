import json
from pathlib import Path

BASE_PATH = "C:\\Users\\HP\\PycharmProjects\\alpha\\tests\\data\\"


def read_file(file_name: str) -> dict:
    file_path = get_file_with_json_ext(file_name)
    print("file_path", file_path)
    with open(file_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def get_file_with_json_ext(file_name: str) -> Path:
    if not file_name.endswith(".json"):
        file_name += ".json"
    return  "C:\\Users\\HP\\PycharmProjects\\alpha\\tests\\data\\payload.json"
