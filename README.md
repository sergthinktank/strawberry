# strawberry
Demo
1. Clone the repository.
2. Create and activate virtual env: `python -m venv virtualenv`, `source virtualenv/bin/activate`.
3. Install all the modules: `pip install -r requirements.txt`.
4. Run `uvicorn main:app --reload`.
5. Using Chrome go to `http://127.0.0.1:8000/graphql`, input `subscription{ showContent }` to see the result. 
