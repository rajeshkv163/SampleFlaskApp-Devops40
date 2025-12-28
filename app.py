from flask import Flask


def create_app():
    x=10
    y=50
    app = Flask(__name__)
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        return 'Hi GFG40 updated'

    @app.route('/test')
    def test():
        x=20
        return "test 1123456789 abcdefg79239279273927393923982938239239"

    @app.route('/test2')
    def test1():
        return "test 20"

    @app.route('/test3')
    def test3():
        return "test 1234"

if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=80, debug=True)
