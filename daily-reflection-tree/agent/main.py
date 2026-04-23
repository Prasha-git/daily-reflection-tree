import json

with open("../tree/reflection-tree.json", "r") as file:
    data = json.load(file)

nodes = {}
for node in data["nodes"]:
    nodes[node["id"]] = node

current = "START"

while True:
    node = nodes[current]

    print("\n" + node["text"])

    if node["type"] == "question":
        options = node["options"]

        for i, option in enumerate(options, start=1):
            print(str(i) + ". " + option)

        input("Choose option number: ")
        current = node["next"]

    elif node["type"] == "start":
        current = node["next"]

    elif node["type"] == "reflection":
        input("Press Enter to continue...")
        current = node["next"]

    elif node["type"] == "end":
        break

print("Session completed.")