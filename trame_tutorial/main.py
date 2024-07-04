from app import App
import sys

def main(**kwargs):
    app = App()
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split("=")
            kwargs[key] = int(value)
        except:
            pass
    app.server.start(**kwargs)


if __name__ == '__main__':
    main()