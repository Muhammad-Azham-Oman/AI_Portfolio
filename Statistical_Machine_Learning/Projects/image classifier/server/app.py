from flask import Flask, request, render_template
from util import classify_image, load_saved_artifacts

app = Flask(__name__)
load_saved_artifacts()

@app.route("/", methods=["GET", "POST"])
def index():
    unknown = None
    result = None
    error = None

    if request.method == "POST":
        image = request.files["image"]
        image.save("uploaded.jpg")

        classified = classify_image(None, "uploaded.jpg")

        if not classified or len(classified) == 0:
            error = "Image is invalid or could not be classified."

        else:
            if classified['class_probability']<80:
                unknown = 'Unknown person.'
            else:
                result = classified

    return render_template("index.html", result=result, error=error , unknown = unknown)

if __name__ == "__main__":
    app.run(debug=True)