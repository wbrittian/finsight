from website import create_app

def main() -> None:
    print("Hello")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    main()