# Churn Scripts

##A Series of Scripts that Test H2O Steam:
- [Import Data](https://github.com/laurendiperna/Churn_Scripts/blob/master/Extraction_Script.py)
- [Transform Data](https://github.com/laurendiperna/Churn_Scripts/blob/master/Transformation_Script.py)
- [Build Model](https://github.com/laurendiperna/Churn_Scripts/blob/master/Modeling_Script.py)

## Using Docker for Mac
- follow the instructions to [Get Started with Docker For Mac](https://docs.docker.com/docker-for-mac/)
- Once installed, double-click Docker.app to start Docker
- clone this repo (in your terminal type `git clone git@github.com:laurendiperna/Churn_Scripts.git`)
- from the command line cd to this repo, then type `docker build -t docker-model .` (don't forget the `.`) and hit enter to build the docker container
- Once built, type `docker run docker-model python Modeling_Script.py` to run the modeling script, which will return the generate model ids using *here documents*
