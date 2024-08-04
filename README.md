# Personal Game Stats
<!-- PROJECT SHIELDS -->
[![Latest release][github-release-version]][github-release-url]
[![Build Status][github-build]][github-build-url]
[![License][github-license]][github-license-url]



<!-- PROJECT LOGO -->



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project lets you run a local website that can query apis for the most common games given a api key for the specific games. Games that you can query given api keys and username are,

Leage of Legends (Not workig),
Valorant (Not working),
Overwatch (Not working),
Chess.com (Not working).



## Overview

## Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)
- Git (for version control)



<!-- SETUP -->
## Setup

1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone https://github.com/ollav12/LeageOfLegendsTracker
cd your-repository
```

### 2. Create and Activate a Virtual Environment

#### On Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
#### On MacOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a .env file in the root directory of the project and add your environment variables.
Look at .env.example for what to include.

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

### 6. Access the Application
```bash
http://127.0.0.1:8000
```
You should now see the homepage of the application.

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROJECT STRUCTURE -->
## Project Structure

```bash 
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   └── templates/
│       └── index.html
│
├── .env     # Your .env file created for environment variables
├── .gitignore
├── requirements.txt
└── venv/    # Virtual environment directory
```



<!-- LICENSE -->
## License
Not decided on license yet.



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Resources i have found helpful when creating this project:

* [Img Shields](https://shields.io)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[github-release-version]:https://img.shields.io/github/v/release/ollav12/LeageOfLegendsTracker
[github-release-url]:https://github.com/ollav12/LeageOfLegendsTracker/releases
[github-build]:https://img.shields.io/github/actions/workflow/status/ollav12/LeageOfLegendsTracker/main.yml
[github-build-url]:https://github.com/ollav12/LeageOfLegendsTracker/actions
[github-license]:https://img.shields.io/github/license/ollav12/LeageOfLegendsTracker
[github-license-url]:#license