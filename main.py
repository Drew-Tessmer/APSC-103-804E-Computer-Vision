from Website.__init__ import create_app
from flask import Flask, render_template, jsonify, request

# Create Flask app instance
app = create_app()


# def detect_obstacle(image):
#     # Your YOLOv8 detection code goes here
#     # This is just a placeholder
#     if "obstacle" in image:
#         return True
#     else:
#         return False
#
#
# @app.route('/detect', methods=['POST'])
# def detect():
#     if request.method == 'POST':
#         # Assuming the image data is sent in the request
#         image_data = request.files['images'].read()
#
#         # Process the image using YOLOv8 (replace this with your actual detection code)
#         obstacle_detected = detect_obstacle(image_data)
#
#         if obstacle_detected:
#             # If obstacle detected, return a warning message
#             return jsonify({'message': 'Warning: Obstacle detected!'})
#         else:
#             # If no obstacle detected, return a success message
#             return jsonify({'message': 'No obstacles detected.'})


# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
