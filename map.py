from flask import Flask, request, jsonify, render_template

# Create a Flask app
app = Flask(__name__)

# Global list to store markers
markers = []

# Route to render the map
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html', map_data=markers)

# Route to add a marker
@app.route("/add_marker", methods=["POST"])
def add_marker():
    try:
        # Get coordinates from the form
        lat = float(request.form["latitude"])
        lng = float(request.form["longitude"])
        # Add the marker to the list
        markers.append({"lat": lat, "lng": lng, "popup": f"Marker at ({lat}, {lng})"})
        return jsonify(markers)
    except ValueError:
        return jsonify({"success": False, "message": "Invalid coordinates."}), 400

if __name__ == "__main__":
    app.run(debug=True)
