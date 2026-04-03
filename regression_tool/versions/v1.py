def process(data):
    return data.upper()

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    print(process(input_data))
