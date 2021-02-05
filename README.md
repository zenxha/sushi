![Sushi](https://cdn.discordapp.com/attachments/783082777020203061/799906807388307496/unknown.png)
# Sushi
Group Project for tri2!
### Links
- [Project Board](https://github.com/zenxha/sushi/projects/4)
- [Runtime Link](http://rubinfamily.dyndns.org:5000/)
- [Easter Egg Link (Use mort as username)](http://rubinfamily.dyndns.org:5000/update)

### Collaborators
- Allen Xu ID: #72947445
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: 51984972

### Tickets this week
- Allen
  - [Worked on creating the IAM page and displaying each person's IAM statements](https://github.com/zenxha/sushi/projects/4#card-54281293)
- Chris
  - [Work on the user sessions as well as user authentication](https://github.com/zenxha/sushi/projects/4#card-53785877)
- Devam
  - [Work on user login and authentication (still incomplete due to technical issues. We have it running, but not storing in database)](https://github.com/zenxha/sushi/projects/4#card-53785877)
- Komay
  - [Create Login and Email registration form for the front end and link the user input to the backend code](https://github.com/zenxha/sushi/projects/4#card-54354857)
  - [Created method to access easter egg which only allows access with specific username](https://github.com/zenxha/sushi/projects/4#card-53782464)

### College Board Requirements
- Instructions for input from one of the following:
  - the user (including user actions that trigger events)
  - a device
  - an online data stream
  - a file
- Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
- At least one procedure that contributes to the program’s intended purpose,
where you have defined:
  - the procedure’s name
  - the return type (if necessary)
  - one or more parameters
- An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
- Calls to your student-developed procedure
- Instructions for output (tactile, audible, visual, or textual) based on input and
program functionality
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
