:: Activate Virtual Enviroment
@ECHO Step #1 - Generate Python Enviroment ...
@python3 -m venv env
@ECHO Step #1 - Done

@ECHO Step #2 - Activating Virtual Environment ...
@CD /D env/Scripts && activate && CD ../../simplemooc && ECHO Step #2 - Done && ECHO Step #3 - Isntalling Requirements ... && pip3 install -r requirements.txt && ECHO Step #3 - Done