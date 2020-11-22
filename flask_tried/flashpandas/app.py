from flask import Flask, render_template


def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/user/<name>')
    def name(name):
        return f'Hello {name}!'


    @app.route('/learn')
    def learn():
        return 'Here to learn huh? <br>I suggest you try harder.'


    @app.route('/test')
    def test():
        return 'This is a test.'

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
