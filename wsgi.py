"""Driver for Web server"""
import json
from views import app
with open('config.json') as file:
    config = json.load(file)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.secret_key = 'heyheyhey'
    app.run(debug=True, host='127.0.0.1', port='5000')
