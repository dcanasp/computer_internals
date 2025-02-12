import json

def read_json_file(filename):
    """Read and return JSON data from a file."""
    with open(filename, "r") as file:
        return json.load(file)

def main():
    filename = "iterPc.json"
    data = read_json_file(filename)

    print("Press Enter to step through the JSON data (Ctrl+C to exit)...")
    for item in data:
        input()  # Lo mismo que el boton de seguir
        # print(json.dumps(item, indent=2))  # por si quieres ver todo
        print("iter:", item.get("iter"))
        print("PC:", item.get("PC"))
        print("registros:", item.get("registros"))
        x = item.get("registros")
        print("R0:", x[0])
        # print("memoria:", item.get("memoria"))

if __name__ == "__main__":
    main()
