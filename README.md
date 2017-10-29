# Analytics Vidhya's DataHack2017 Hack Session

Code, Documents and Slides for Hack Session: ML Models in Production using Flask and Docker.

### Contents:

- __Folder: [`hello-world-flask`](https://github.com/pratos/datahack2017-workshop-av/tree/master/hello-world-flask)__, contains the hello-world examples for starting with `flask`
- __Folder: [`slides`](https://github.com/pratos/datahack2017-workshop-av/tree/master/slides)__, for the Hack session (__NOTE:__ The [`README.md`](https://github.com/pratos/datahack2017-workshop-av/blob/master/slides/README.md) in [`/slides`](https://github.com/pratos/datahack2017-workshop-av/tree/master/slides) contains info on how to run it locally) 
- __Folder: [`working_api`](https://github.com/pratos/datahack2017-workshop-av/tree/master/working_api)__, contains the working code and notebooks for the hack session.
- __File: [`docker-machine-hello-world.md`](https://github.com/pratos/datahack2017-workshop-av/blob/master/docker-machine-hello-world.md)__, contains basic info about `docker-machine` and how to start off.

### How to setup the Anaconda environment:

- Make sure you have __Anaconda distribution__, if not then visit: [Miniconda Installation](https://conda.io/miniconda.html) to install it.
- For any queries regarding conda environment, visit: [Managing Conda Environments](https://conda.io/docs/user-guide/tasks/manage-environments.html)
- __Anaconda environment file__ is in the root directory: `datahack.yml`
- In the terminal run command: `conda env create -f datahack.yml`
- Once done, run: `source activate datahack`. Your virutal environment is setup successfully!