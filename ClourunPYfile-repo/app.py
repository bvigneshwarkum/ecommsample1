from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>E-Commerce App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .header {
                background-color: #333;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
            .container {
                margin: 20px auto;
                max-width: 1200px;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .column {
                float: left;
                width: 30%;
                margin: 1.66%;
                box-sizing: border-box;
                padding: 10px;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                text-align: center;
            }
            .column h2 {
                margin-top: 0;
                color: #333;
            }
            .clearfix::after {
                content: "";
                clear: both;
                display: table;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Welcome to Our BalkiS E-Commerce Store</h1>
        </div>
        <div class="container">
            <div class="clearfix">
                <div class="column">
                    <h2>Electronics</h2>
                    <p>Explore our latest gadgets and accessories.</p>
                </div>
                <div class="column">
                    <h2>Fashion</h2>
                    <p>Discover the newest trends in clothing.</p>
                </div>
                <div class="column">
                    <h2>Home & Garden</h2>
                    <p>Find the best deals for your home and garden.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
