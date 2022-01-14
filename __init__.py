from flask import Flask
from views.views import MainView, ProductView, CustomerView, ShoppingView


app = Flask(__name__)

def init_views():
    CustomerView.register(app)
    ProductView.register(app)
    ShoppingView.register(app)
    MainView.register(app)


if __name__ == '__main__':
    init_views()
    app.run(debug=True)
