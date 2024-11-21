from flask import Flask, request, jsonify, make_response
import os
import hashlib

app = Flask(__name__)

# Directory to store content on disk
CONTENT_DIR = "content_store"

# Ensure the directory exists
os.makedirs(CONTENT_DIR, exist_ok=True)


def generate_etag(data):
    """Generate an ETag for the given data using SHA256."""
    return hashlib.sha256(data.encode()).hexdigest()


def save_content_to_disk(key, content):
    """Save content to a file on disk."""
    file_path = os.path.join(CONTENT_DIR, key)
    try:
        with open(file_path, "w", encoding="utf-8") as file:  # Explicitly specify UTF-8 encoding
            file.write(content)
        print(f"Content saved to {file_path}")  # Debugging log
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")


def read_content_from_disk(key):
    """Read content from a file on disk."""
    file_path = os.path.join(CONTENT_DIR, key)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:  # Explicitly specify UTF-8 encoding
                return file.read()
        except Exception as e:
            print(f"Error reading content from {file_path}: {e}")
    return None


@app.route('/content/<key>', methods=['GET', 'HEAD', 'POST'])
def handle_content(key):
    sanitized_key = key.replace("/", "_")  # Sanitize the key to avoid invalid paths

    if request.method == 'GET':
        content = read_content_from_disk(sanitized_key)
        if content is not None:
            etag = generate_etag(content)
            response = make_response(content)
            response.headers['ETag'] = etag
            return response
        else:
            return "Content not found", 404

    elif request.method == 'HEAD':
        content = read_content_from_disk(sanitized_key)
        if content is not None:
            etag = generate_etag(content)
            response = make_response()
            response.headers['ETag'] = etag
            return response
        else:
            return "Content not found", 404

    elif request.method == 'POST':
        new_content = request.data.decode('utf-8')  # Decode incoming binary data to UTF-8 string
        # print(f"Received content to save: {new_content}")  # Debugging log
        save_content_to_disk(sanitized_key, new_content)
        etag = generate_etag(new_content)
        return jsonify({"message": "Content stored", "ETag": etag}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
