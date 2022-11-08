FROM python
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /tests_project/tests/

# docker build -t pytest_runner .
# docker run --rm --mount type=bind,src=/Users/ek.chudi/PycharmProjects/learnqaPythonApi,target=/tests_project/ pytest_runner