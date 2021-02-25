"""Driver for Web server"""

from views import app



port = 5000
if __name__ == "__main__":
    # runs the application on the repl development server
    app.secret_key = 'heyheyhey'
    app.run(debug=True,host='localhost',port=port)

