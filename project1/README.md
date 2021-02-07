# Project 1- Music Discovery Web App

<!--## To fork and clone this repository, follow the steps below:-->
<!--1. On <https://github.com/NJIT-CS490-SP21/project1-vs597>, click __Fork__ on the top right corner. This will create a copy of the repository in your GitHub account.-->
<!--2. Go to your github reposotories and you should find a repository named __project1-vs597__.-->
<!--3. Click the drop down arrow on the green button named __Code__ and copy the Https URL.-->
<!--4. In terminal, clone the repo:`git clone https://github.com/NJIT-CS490-SP21/project1-vs597.git`-->
<!--5. `cd` into the repository to begin working on it!-->
<!--6. Run `git init` command to setup a git folder on your local machine for this repository.-->

## Milestone 1:

All technologies, frameworks, libraries, and APIs used:
*[x] Spotify Web API
*[x] Flask
*[x] Python _random_
*[x] Python _requests_
*[x] Python _os_
*[x] Python _dotenv_

#### To get set up on Milestone 1, please note the following:
+ Contains Spotify API to receive information about an artist's top tracks. Artist can be changing by changing `artist_id`
+ Uses Flask to display the song name, song preview, and a song-related image
+ `index.html` file contains if statements that identify tracks with no song preview URL. This is so that no link is displayed.
+ `style.css` file formats the HTML. All classes are outlined but some may not be filled
+ 

#### Questions
1. 3 technical difficulties I experienced and how I fixed them:

One of the techincal issues I encountered was indexing the top tracks information to identify song name, song artist, song-related image, and the preview URL. I was able to overcome this issue by practicing reading a json response through Google searches and repitition. By learning to read a json response, I was able to correctly index the response to get the information needed.

Another technical difficulty I came accross was formatting with CSS. Since I did not have much expereince with CSS prior to this project, I had to familarize myself quickly. This involved searching Google and looking through online documentation. By becoming familiar with CSS, I was able to implement a button to play the preview.

A third difficulty I experienced was when to displaying a preview URL. This is when I implemented `if-elif-else` statements. By doing this, I was able to specify which songs have a preview URL and which don't; I was able to display a clear message stating there is no preview for songs without a preview URL
2. There are no known problems with my Milestone 1. However, the formatting of images and buttons is not beautified at this point.
3. To improve my project in the future, I would attempt to use the `Spotipy` wrapper API. The wrapper API can simplify some of the code and I would be able to become comfortable with it. 
