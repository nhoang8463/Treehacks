from treehacks import filter_app


app = filter_app()

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
