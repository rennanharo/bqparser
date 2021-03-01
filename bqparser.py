import re
import json

f = open("example_inputs/example_input3.txt", "r")

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
    {"name": row[0], "description": "", "mode": row[1], "type": corresp[row[2]]}
    for row in result
]

with open("output.json", "w") as file1:
    json.dump(schema, file1)
print("Conversao feita com sucesso!")
