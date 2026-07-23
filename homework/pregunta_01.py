# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import glob
import os
import zipfile
import pandas as pd


def pregunta_01():
    zip_path = "files/input.zip"
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(".")

    os.makedirs("files/output", exist_ok=True)

    def generate_dataset(split_name):
        data = []
        sentiments = ["negative", "positive", "neutral"]

        for sentiment in sentiments:
            path_pattern = os.path.join("input", split_name, sentiment, "*.txt")
            file_paths = glob.glob(path_pattern)

            for file_path in file_paths:
                with open(file_path, "r", encoding="utf-8") as file:
                    phrase = file.read().strip()
                    data.append({"phrase": phrase, "target": sentiment})

        return pd.DataFrame(data)

    train_df = generate_dataset("train")
    test_df = generate_dataset("test")

    train_df.to_csv("files/output/train_dataset.csv", index=True, index_label="")
    test_df.to_csv("files/output/test_dataset.csv", index=True, index_label="")