#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thelen = len(sys.argv) - 1
    if thelen == 0:
        print(f"{thelen} arguments.")
    elif thelen == 1:
        print(f"{thelen} argument:")
        print(f"{thelen}: {(sys.argv[1])}")
    else:
        idx = 1
        print(f"{thelen} arguments:")
        while idx < 7:
            print(f"{idx}: {(sys.argv[idx])}")
            idx = idx + 1
