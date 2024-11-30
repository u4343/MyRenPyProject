import json
import os

class DataHandler:
    def __init__(self, base_path):
        """
        :param base_path: JSON 파일의 기본 경로
        """
        self.data_folder = os.path.join(base_path, "data")

    def load_json(self, filename):
        """
        JSON 데이터를 로드하는 메서드
        :param filename: 로드할 JSON 파일 이름
        :return: 로드된 JSON 데이터 또는 None
        """
        file_path = os.path.join(self.data_folder, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {filename} not found in {self.data_folder}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error in {filename}: {e}")
            return None

    def save_json(self, filename, data):
        """
        JSON 데이터를 저장하는 메서드
        :param filename: 저장할 JSON 파일 이름
        :param data: 저장할 데이터 (dict 형식)
        """
        file_path = os.path.join(self.data_folder, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving {filename}: {e}")
