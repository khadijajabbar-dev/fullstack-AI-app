import os

def main():
    env = os.getenv("APP_ENV", "development")
    print(f"Hello, World! 👋 api is running in {env} mode.")

if __name__ == "__main__":
    main()
