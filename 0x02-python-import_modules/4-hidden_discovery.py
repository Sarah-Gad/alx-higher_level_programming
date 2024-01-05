#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for idx in dir(hidden_4):
        if not idx.startswith("__"):
            print(f"{idx}")
