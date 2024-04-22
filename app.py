from Website.__init__ import create_app
from flask import Flask, render_template, jsonify, request,redirect
import os
import cv2

# Create Flask app instance
app = create_app()

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

