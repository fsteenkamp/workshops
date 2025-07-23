def fetch_data():
    raise Exception("data fetching failed")

# -------------------------------------------------

def sum_data(x):
    return x["a"]+ x["b"]


def main():
    x = None
    try:
        x = fetch_data()
    except Exception as e:
        print(f"Error: {e}")

    sum_data(x)

main()
