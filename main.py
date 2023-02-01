# import os
# import docx
#
#
# def create_word_files_from_template(directory, file_names, template_file):
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     template = docx.Document(template_file)
#
#     for file_name in file_names:
#         file_path = os.path.join(directory, file_name + ".docx")
#         doc = template.clone()
#         doc.save(file_path)
#
#
# # Example usage
# directory = "word_files"
# file_names = ["file1", "file2", "file3"]
# template_file = "template.docx"
#
# create_word_files_from_template(directory, file_names, template_file)
from flask import Flask, request
import os
import docx

app = Flask(__name__)


@app.route("/create_word_files", methods=["POST"])
def create_word_files():
    directory = request.form.get("directory")
    file_names = request.form.getlist("file_names")
    template_file = request.form.get("template_file")

    if not os.path.exists(directory):
        os.makedirs(directory)

    template = docx.Document(template_file)

    for file_name in file_names:
        file_path = os.path.join(directory, file_name + ".docx")
        doc = template.clone()
        doc.save(file_path)

    return "Word files created successfully!"


if __name__ == "__main__":
    app.run()
