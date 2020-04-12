from main import app, os
app.run(port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
