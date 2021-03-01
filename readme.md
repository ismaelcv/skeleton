Change to main folder
cd skeleton


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
pip install pip-tools          #pip tools to create requirements.txt
pip-compile > requirements.txt 

docker
docker build . -t skeletonapp
docker run -p 8000:8000 skeletonapp


### Call the api
uvicorn asgi:app --reload