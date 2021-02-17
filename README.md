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

### Progress Summary

- Idea, Visuals, HTML, CSS, JS 5pts
  - Idea: Our idea, design, and features are located at the end of the README.
  - Visuals: 
    - We mainly worked on visuals in our home page, such as [displaying quotes from an api,](https://github.com/zenxha/sushi/blob/cd2b15bcf0891ea65179d5313b9b589c463e3676/views.py#L31-L38) and creating a [nice looking home page with CSS.](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/base2.html#L38-L163)
  - HTML: You can view these in any of our .html files
  - CSS: 
    - We used CSS in designing our pages on the website, such as our [home page,](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/base2.html#L38-L163) [login page,](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/login.html#L7-L135) and [upload page.](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/loginv2.html#L11-L135)

- Routes, Model Code & CRUD 5pts
  - Routes: 
    - You can see all the routes on your website in our views.py file from [This line and downward](https://github.com/zenxha/sushi/blob/dce184d63e90a32519029a02918c2d3da508221b/views.py#L43)
  - Model Code
  - CRUD: Database setup
- Easter Egg 3 pts
  - To get to our easter egg, fill out the upload form on the website but put mort as the username to access the easteregg
- Project WOW 2 pts
  - [Our upload page](http://rubinfamily.dyndns.org:5000/upload). Once you upload an image, type in http://rubinfamily.dyndns.org:5000/images/1 to view the image you just uploaded. Each image uploaded is assigned an id, starting with 1, so if you upload another image, you can replace 1 with 2 to view that uploaded image, and so on.


### Tickets this week
- Allen
  - [Worked on creating the IAM page and displaying each person's IAM statements](https://github.com/zenxha/sushi/projects/4#card-54281293)
- Chris
  - [Work on the user sessions as well as user authentication](https://github.com/zenxha/sushi/projects/4#card-53703118)
- Devam
  - [Work on user login and authentication (still incomplete due to technical issues. We have it running, but not storing in database)](https://github.com/zenxha/sushi/projects/4#card-53785877)
- Komay
  - [Worked on integrating the backend login/auth system with the frontend html form](https://github.com/zenxha/sushi/projects/4#card-54354857)
  - [Finished 3rd checkbox of the ticket which only allows the correct account to access easteregg](https://github.com/zenxha/sushi/projects/4#card-53782464)

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

## Our Idea
- We aim for a simple and clean site that contains everything about sushi. On the site you’ll be able to search our database of sushi’s and read about each sushi’s description and origin. If you sign up, you’ll be able to save your favorite sushi’s and post

## Things we want to have:
- Database of user uploaded sushi images
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

