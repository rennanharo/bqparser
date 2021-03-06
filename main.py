import os
import re
import json
import argparse

# CLI args settings
parser = argparse.ArgumentParser(
    description="Bqparser will convert plain txt files with schemas from various RDBMS to BigQuery json schema."
)
parser.add_argument(
    "path_to_source", type=str, help="Add the path to source e.g.: ~/schema.txt"
)
parser.add_argument(
    "source_db",
    type=str,
    help="Database which schema you want to convert to BigQuery e.g.: Oracle",
)
parser.add_argument(
    "-d", action="store_true", help="Pass the path to source files as dir"
)

# Initializing arguments
args = parser.parse_args()

if args.source_db.lower() == "oracle":
    if args.d == True:
        files: list[str] = os.listdir(args.path_to_source)
    else:
        files: list[str] = [args.path_to_source]
    lrange: int = len(files)

    for file in files:
        if args.d == True:
            filename = os.fsdecode(file).split(".")[0]
            print(filename)
            f = open(f"{args.path_to_source}/{file}", "r")
        else:
            filename = args.path_to_source.split("/")[-1]
            filename = filename.split(".")[0]
            f = open(args.path_to_source, "r")
        print(filename)

        objects = []
        for line in f:
            strpline = line.strip()
            line_list = strpline.split()
            objects.append(line_list)

        f.close()

        result = []
        for row in objects:
            if row[1] == "NOT":
                row[1] = "REQUIRED"
                row.pop(2)
                try:
                    row[2] = re.sub(r"\([^()]*\)", "", row[2])
                except:
                    "No parentheses found."

                result.append(row)

            elif row[0] != "Nome" and not re.search("--.+", row[0]) and row[1] != "NOT":
                row.insert(1, "NULLABLE")
                try:
                    row[2] = re.sub(r"\([^()]*\)", "", row[2])
                except:
                    "No parentheses found."
                result.append(row)

        corresp = {
            "BINARY_DOUBLE": "NUMERIC",
            "BINARY_FLOAT": "FLOAT64",
            "BLOB": "BYTES",
            "CHAR": "STRING",
            "CLOB": "STRING",
            "DATE": "DATE",
            "FLOAT": "FLOAT64",
            "INTERVALDAYTOSECOND": "STRING",
            "INTERVALYEARTOMONTH": "STRING",
            "NCHAR": "STRING",
            "NCLOB": "STRING",
            "NUMBER": "NUMERIC",
            "NVARCHAR2": "STRING",
            "RAW": "BYTES",
            "TIMESTAMP": "DATETIME",
            "TIMESTAMP WITHLOCALTIMEZONE": "TIMESTAMP",
            "TIMESTAMP WITHTIMEZONE": "TIMESTAMP",
            "VARCHAR2": "STRING",
        }

        schema = [
            {
                "name": row[0],
                "description": "",
                "mode": row[1],
                "type": corresp[row[2]],
            }
            for row in result
        ]
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open(f"outputs/{filename}.json", "w+") as file1:
            json.dump(schema, file1)
        print("Conversao feita com sucesso!")

# TODO Treat decimals with numeric (7,4)