from app.instance import config
from app.main import create_app


if __name__ == '__main__':
    app = create_app(config)
    app.run()



