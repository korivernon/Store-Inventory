from storeinv import app
# Run Server
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
