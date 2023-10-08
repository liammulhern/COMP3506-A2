all: zip

zip: clean
	zip -r submission.zip structures/*.py tests/*.py algorithms/*.py ./*.py statement.txt

clean: 
	rm -rf submission.zip