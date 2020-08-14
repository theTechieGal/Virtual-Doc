# Make file to run the DocBot project

run: jsonify.py train.py app.py chat.py autoopen.py
	python3 jsonify.py
	python3 train.py
	python3 app.py
	
clean:
	rm chatbot_model.h5 classes.pkl words.pkl geckodriver.log
	rm -r __pycache__
