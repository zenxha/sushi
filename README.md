![Sushi](https://cdn.discordapp.com/attachments/783082777020203061/786710616378572820/unknown.png)
# Sushi
Group Project for tri2!
### Links
- [Project Board](https://github.com/zenxha/sushi/projects/1)
- [Week1/11 Project Board](https://github.com/zenxha/sushi/projects/2)
### Grading
#### Scrum Master Grade: 15
#### Individual
- Allen Xu:5
- Chris Rubin: 5
- Devam Shrivastava:5
- Komay Sugiyama:5

[Project Plan](https://docs.google.com/document/d/1dPvOiqA6RArgcVYMSlQAP0ztnoioO75UUg6ImmFhrQg/edit?usp=sharing)
### Collaborators
- Allen Xu ID: #72947445
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: 51984972

## Summary
- We aim for a simple and clean site that contains everything about sushi. On the site you’ll be able to search our database of sushi’s and read about each sushi’s description and origin. If you sign up, you’ll be able to save your favorite sushi’s and post

## Things we want to have:

- Database of every sushi
- Types of sushi: https://www.tablespoon.com/posts/know-your-sushi-types-and-terms-before-ordering
- Menu example: https://www.toasttab.com/rbsushi-ranchobernardo/v3
- Login system that people can create/save accounts with
- Have users be able to upload their own sushis (picture, desc, reviews)[SQLAlchemy]
- Do this with database that will store sushi name, images, description, user reviews onto database (CB Big Idea #2 and #3)
- Have an option to view the descriptions and reviews of the sushi
- Pull from the database and display that information
- Library of all the tier lists other people have made that the user can browse
- Redirects to social media to draft messages

## Structure/Design:

* Function on flask
* Navbar that lets user navigate the website from info on sushi to posting their favorite sushis
* Data driven UI designs will be storyboarded through google drawings, then implemented into the website once approved. (CB Big Idea #3)
* Login function to save information the user performs in database
* Upload page will allow user to add own sushi images into database
* Database holds information to
  * Sushi types, descriptions, and rating out of 10
  * Login information (this has to be dynamic)
  * Saved tier lists
  * Images to sushis submitted by the users (will include file size limiter, file type selector)


## Planned Features
- Database of every sushi
  - Types of sushi: https://www.tablespoon.com/posts/know-your-sushi-types-and-terms-before-ordering
  - Menu example: https://www.toasttab.com/rbsushi-ranchobernardo/v3
- Login system that people can create/save accounts with
- Library of all the tier lists other people have made that the user can browse
- Redirects to social media to draft messages

## Current Assignments
- Allen Xu: Work on website navbar, edit and upload code video
- Chris Rubin: Help set up navbar and assist Devam in backend
- Devam Shrivastava: Work on backend code which consits of the database
- Komay Sugiyama: Help with website blueprint, brainstorm backend

## Weekly Updates
### Week 4
- Upload page is fully functional, CSS will be incorporated later
- Login working, sessions are saved in cookies, planning on adding a password function later on
- Database working on Devam's individual github, will add to main github soon
### Week 3
- Continued work on upload page, mainly fixing file directory path and adding CSS
- Continued work on log in page
- Began using SQLite for database creation
### Week 2
- Changed backgorund to use an api for many different sushi pictures
- Started work on an upload page that adds images into our database upload via user
- Started work on a log in page for the site
### Week 1
- Added a navbar to the website
- Added a custom moving background
- Added a projects page which displays our project plan
- Started work on the database setup
### Week 0
- Created README layout
- Started storyboarding UI layouts for the website
- Transfered information from google docs onto github readme
