## ✅&nbsp; Installation Requirements -

STEP 1: **Environment**

- Once the project has been cloned we need to create an environment with the following commands:
  `conda create --name skeleton python=3.7`
  `source activate-env`
  Note:The yml configuration file has already been included in the project
- Update conda with `make update-conda`
- Create a new enviroment with `make create-env`
- Activate the prolomeister environment in the kernel running `make activate-env`

STEP 2: **Skeleton!!!**

- Run `pip install -e .[dev]` to convert our code into a formal python package
- Run `pip install -r requirements-no-deps.txt --no-deps` to install additional requirements
- if you run `pip list` prolomeister should appear in the list

STEP 3: **Install Jupyter lab**

- Run `pip install jupyterlab` to install pip and its dependencies
- Run `make install-kernel` to include the prolopricer environment in the kernel

STEP 4: **Pre-commit install**

- Install pre-commit in case you are going to do modifications to the code with the following command `pre-commit install`
- Run `pre-commit run --all-files` to ensure any changes adhere to the specified guidelines

Setup/Activate environment
python3 -m venv venv
source venv/bin/activate

Install Jupyter lab
pip install jupyterlab

Install main libraries (editable)
and cli package
pip install -e .

Call from cli
skeleton greet ismael

Call from cli with options
skeleton greet ismael -lan 'es'

### Create requirements txt

pip install pip-tools #pip tools to create requirements.txt
pip-compile > requirements.txt

docker
docker build . -t skeletonapp
docker run -p 8000:8000 skeletonapp

### Call the api

uvicorn asgi:app --reload
