from flask_pymongo import ObjectId

class Resume:
    def __init__(self, filename, text, parsed_data):
        self.filename = filename
        self.text = text
        self.parsed_data = parsed_data

    def to_dict(self):
        return {
            "filename": self.filename,
            "text": self.text,
            "parsed_data": self.parsed_data
        }
