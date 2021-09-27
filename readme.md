## ✅&nbsp; Installation Requirements

STEP 1: **Clone the skeleton repo**
`git clone git@github.com:ismaelcv/skeleton.git`

STEP 2: **Set up a virtual environment**

a) Install vitualenv: `sudo pip3 install virtualenv`
b) create a virtual environment: `virtualenv venv`
c) Activate the virtual environment: `source venv/bin/activate`

STEP 3: **Skeleton!!!**
- Run `pip install -e .'[dev]'` to convert our code into a formal python package
- Run `pip install -r requirements.txt` to install additional requirements
- Install pre-commit `pre-commit install`
- if you run `pip list` prolomeister should appear in the list
- Run `pre-commit run --a` to ensure any changes adhere to the specified guidelines





docker
docker build . -t skeletonapp
docker run -p 8000:8000 skeletonapp

### Call the api

uvicorn asgi:app --reload
