from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/product')
def product_page():
    return render_template("product.html")

@app.route('/shop')
def shop_page():
	products=["icecream", "chocolate", "candy"]
	return render_template("shop.html", products=products)

if __name__ == '__main__':
   app.run(debug = True)