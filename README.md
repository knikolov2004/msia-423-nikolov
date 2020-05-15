# MSiA423 Playlist Predictor
#### Project by Kristian Nikolov (knikolov2004)  
#### QA by Joshua Khazanov (joshuakhazanov) 

___

## Project Charter
### Background Scenario

I am part of the data science team at Spotify, currently working with the 
marketing team before the launch of our new ML curated playlists, which are 
themed for certain occasions (dinner, parties, workouts, etc.). 

Our goal for this Q is to figure out a way to increase user engagement 
with the new product. Because of the team's successful and unorthodox methods 
in the past, we have been given full creative freedom to design whatever we see 
fit, but have a very tight deadline - the end product has to be up and running in 9 weeks.

### Vision
Create an interesting and fun to use interactive tool, 
which would ultimately showcase Spotify's in house playlists, 
which will increase day-to-day user engagement. 

The app can also lead to new customers
and higher customer retention for Spotify.
 
### Mission

To showcase how great our models are at curating the playlists, we have 
decided to let the user pick his own music, and let our model decide what 
occasion it is best suited for.

To do so, we will pick the 4 most commonly used themes for playlists (TBD), 
find the top used songs for those themed playlists (based on publicly 
accessible Spotify playlists), and build a model which classifies songs based
on their audio features into one of the 4 themes.

After the model has been built, we will deploy it in an easy to use webapp, 
where users can input their favorite songs, which will then be classified to 
one of the 4 predefined themes. 

### Success Criteria
1. ML Metrics
* Our CV misclass rate when training the model is <10%
* Our CV SSE standard deviation isn't wildly varying (signifying that our model 
is very sensitive to the sample it is trained on). Ballpark estimate is less 
than 10% variation between SSE's.
* Model doesn't take more than 5 seconds to run (which would render the 
app user unfriendly and lead to high churn rates)

2. Business Metrics

    The initiative can be considered a success if we observe: 
* 0.5% increase in newly acquired users for the subsequent 3 months 
after the app is launched (the baseline will be the monthly increase for 
the previous year, to account for seasonal trends)
* 2% decrease in churn for the subsequent 3 months (baseline will again be 
the previous year's churn rates for the relevant months)
* 5% increase in daily user engagement with Spotify's curated playlists (daily
engagement defined as opening the curated playlist tab in the app at least 
once per day)

For all of these metrics we will do A/B testing on customers who have access 
to the web app vs customers who don't. Since the percentage differences we 
are looking for are relatively small, we will need a pretty large sample size,
but we work for Spotify, so that is a non-issue.

## Project Backlog
### Planning
Initiative 1 - Verify that the overall idea and business metrics
are both achievable and good enough for our stakeholders (Chloe and Fauste)
* Epic 1 - Produce charter and backlog
* Epic 2 - Find the required data for the model
    + Story 1 - sourcing the SpotiPy API - https://spotipy.readthedocs.io/en/2.11.1/ - 
    can serve both as source of playlists and audio features for the model
    + Story 2 - LibROSA - https://librosa.github.io/librosa/index.html - can 
    be used for audio features for offline .mp3 files
    + Story 3 - The Playlist Miner - https://github.com/plamere/playlistminer OR
    http://playlistminer.playlistmachinery.com/index.html - can provide either 
    static playlists or if time permits the ability to generate playlists 
    based on user input
* Epic 3 - Agree on proposed ML/business metrics
* Epic 4 - Replicate the playlist miner to generate playlists on the fly 
and allow users to input their own search themes

Initiative 2 - Building the playlist theme classification model 
* Epic 1 - Data gathering and cleaning
    + Story 1 - Getting SpotiPy authenticated
    + Story 2 - Collecting the top 100 songs from all public playlists which
    contain a thematic keyword in their names (i.e. finding all playlists 
    which have "workout" in them and creating a list of the top 100 most 
    commonly found songs) 
    + Story 3 - Using SpotiPy to get the audio features for each song
    + Story 4 - Reshaping the data into dataframe/matrix form, which
    would easily allow me to run scikitlearn models 
    + Story 5 - Saving data for predefined themes to .csv files (later to be
    uploaded to S3 buckets)
* Epic 2 - EDA and Feature Engineering
    + Story 1 - Going over all audio features, standardizing the data (because
    of different variable scales), fixing skewed data (logging), checking for 
    outliers and missings (unlikely since data is from API)
    + Story 2 - Creating new features (i.e., checking if features vary 
    between song segments, max variation could be new feature)
    + Story 3 - Bringing granularity back to song level (to ensure our model 
    is modelling the correct thing)
* Epic 3 - Testing various classification models 
    + Story 1 - Testing logistic regression using CV
    + Story 2 - Testing classification trees using CV 
    + Story 3 - Testing boosted trees using CV
    + Story 4 - Testing additional models    

Initiative 3 - Building the "Playlist Predictor" webapp
* Epic 1 - Create app frontend
    + Story 1 - Create default site aesthetic using html/CSS
    + Story 2 - Create search box prompting for song/artist combination
    + Story 3 - Create output box, which shows which theme the song belongs to
* Epic 2 - Uploading static data to S3 bucket
* Epic 3 - Combining the frontend with the model 
* Epic 4 - Adding additional input window, allowing the user to input custom 
themes, which could later be the basis for the classification algorithm

Initiative 4 - Deploying the webapp and testing performance
* Epic 1 - Sampling users for both control and experiment groups
* Epic 2 - Setting up the experiment to accurately measure our performance 
metrics before deploying the webapp
* Epic 3 - Deploying the webapp to the experiment group for 3 months
* Epic 4 - Measuring success

### Backlog
* Initiative1.Epic1 *planned (1)*
* Initiative1.Epic2 *planned (2)*
* Initiative1.Epic3 *planned (2)*
* Initiative2.Epic1.Story1 *planned(1)*
* Initiative2.Epic1.Story2 *planned(2)*
* Initiative2.Epic1.Story3 *planned(2)*
* Initiative2.Epic1.Story4 *planned(1)*
* Initiative2.Epic1.Story5 *(1)*
* Initiative2.Epic2.Story1 *(1)*
* Initiative2.Epic2.Story2 *(2)*
* Initiative2.Epic2.Story2 *(1)*




### Icebox
* Initiative1.Epic4 
* Initiative2.Epic3 (8)
* Initiative3.Epic1 (8)
* Initiative3.Epic2 (8)
* Initiative3.Epic3 (8)
* Initiative3.Epic4
* Initiative4

<!-- toc -->


## Directory structure 

```
├── README.md                         <- You are here
│
├── api
│   ├── static/                       <- CSS, JS files that remain static
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── boot.sh                       <- Start up script for launching app in Docker container.

├── config                            <- Directory for configuration files 
│   ├── local/                        <- Directory for keeping environment variables and other local configurations that *do not sync** to Github 
│   ├── logging/                      <- Configuration of python loggers
│   ├── flaskconfig.py                <- Configurations for Flask API 
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── external/                     <- External data sources, usually reference data,  will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── deliverables/                     <- Any white papers, presentations, final work products that are presented or delivered to a stakeholder 
│
├── docs/                             <- Sphinx documentation based on Python docstrings. Optional for this project. 
│
├── figures/                          <- Generated graphics and figures to be used in reporting, documentation, etc
│
├── models/                           <- Trained model objects (TMOs), model predictions, and/or model summaries
│
├── notebooks/
│   ├── archive/                      <- Develop notebooks no longer being used.
│   ├── deliver/                      <- Notebooks shared with others / in final state
│   ├── develop/                      <- Current notebooks being used in development.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports, helper functions, and SQLAlchemy setup. 
│
├── reference/                        <- Any reference material relevant to the project
│
├── src/                              <- Source data for the project 
│
├── test/                             <- Files necessary for running model tests (see documentation below) 
│
├── app.py                            <- Flask wrapper for running the model 
├── run.py                            <- Simplifies the execution of one or more of the src scripts  
├── Dockerfile                        <- Dockerfile for building image to run app  
├── run_docker.sh                     <- Shell file which runs docker app (simplifies importing env varabiles)
├── requirements.txt                  <- Python package dependencies 
```

## Running the app
### 1. Set up SpotiPy credentials
Go to https://developer.spotify.com/dashboard/applications and log in with your Spotify
account (needed for Spotify integrations). When in, create an app (whatever name you want)
and set the Client ID and Client Secret as environment variables.



### 2. Set up remaining env variables
In `config/config.py`, all environment variables which are called with `os.getenv` need to be 
set on the user's machine. These include:
1. RDS variables - user, password, host, port, database; these need to be set up
in the user's AWS console - for instructions visit https://github.com/MSIA/2020-msia423/blob/master/aws-rds/README.md

    In order to check my RDS table, the port is `3306`, and the host is `nu-msia423-kris.cdeg4vxlquwj.us-east-2.rds.amazonaws.com`
    For instructor purposes, the user is msia423instructors and the password is my netid.
    For QA purposes, the user is msia423qa, and the password is my netid.

2. S3 variables - AWS key ID, AWS secret key, S3 bucket; these are also set up in 
the user's AWS console - go to "My Security Credentials" under your username in the top right corner.
Press Create Access Key . Save your AWS Access Key ID and AWS Secret Access Key as env variables, and 
change the S3 bucket name with your own bucket.

### 3. Setting up the Docker image
The Dockerfile for running the API call and ingestion scripts is in the home (current) folder. 
To build the image, run from this directory (the root of the repo): 

```bash
 docker build -t spotify_classifier .
```

This command builds the Docker image, with the tag `spotify_classifier`, based on the instructions in `Dockerfile` 
and the files existing in this directory.

### 4. Running the API calls and RDS/S3 ingestion scripts
*Note:* for this part of the setup to work, the user needs to be connected to
NU's VPN via the GlobalProtect app, otherwise the connection to RDS cannot be made! 
#### 1. Running outside of Docker
To run the files without building the Docker image (this might break due to 
missing packages which can be found in the `requirements.txt` file or other OS
specific differences) just run from this directory:

`python run.py`

This creates 4 raw data files in the `data` folder, uploads the raw data files to
S3 and creates and populates and RDS database with the 4 files.

#### 2. Running in Docker
To run the docker container from this directory, just run:

`sh run_docker.sh` (you may need to add `winpty` in front if running from Git Bash 
on Windows)

This shell file contains the full command needed to import the system's environment
variables and run the docker container. 

This also creates 4 raw data files in the `data` folder, uploads the raw data files to
S3 and creates and populates and RDS database with the 4 files.
