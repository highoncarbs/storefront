from app import app 
from app import db

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True , port=8585 , host='0.0.0.0')