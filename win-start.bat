:: Activate Virtual Enviroment
@ECHO Step #1 - Generate Python Enviroment ...
@python -m venv env
@ECHO Step #1 - Done

@ECHO Step #2 - Activating Virtual Environment ...
@CD /D env/Scripts && activate && CD ../../simplemooc && ECHO Step #2 - Done && ECHO Step #3 - Isntalling Requirements ... && pip install -r requirements.txt && ECHO Step #3 - Done