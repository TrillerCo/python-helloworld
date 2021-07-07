# Python helloworld for pybuilder

Test code for pybuilder stage in any Python CICD pipeline.

## Steps

1. Install requirements `pip install -r requirements.txt`
2. Build project with `pyb` command
3. Upload artifact with [twine]() `twine upload --repository-url ${PYPI_SERVER} -r hello target/dist/hello-*/dist/hello*.whl`
