"""Driver for Web server"""
from flask import Flask
from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True,host='192.168.1.85',port=5000)
