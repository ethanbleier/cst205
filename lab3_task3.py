# Ethan Bleier Lab 3 Task 3
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}
print("Red channel of Clay Creek is", tineye_sample["result"][0].get("color")[0], "\b.")
print("Blue channel of Seal Brown is", tineye_sample["result"][1].get("color")[2], "\b.")