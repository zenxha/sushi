![Sushi](https://cdn.discordapp.com/attachments/784178874303905792/812833268171800596/unknown.png)
# Sushi
Group Project for tri2!
### Links
- [Project Board](https://github.com/zenxha/sushi/projects/4)
- [Runtime Link](http://rubinfamily.dyndns.org:5000/)
- [Easter Egg Link (Use mort as username)](http://rubinfamily.dyndns.org:5000/upload)

### Collaborators
- Allen Xu ID: #72947445
- Komay Sugiyama ID: #30739783
- Chris Rubin ID: #72892271
- Devam Shrivastava ID: 51984972


### Progress Summary
- **College Board rubric is displayed on readme for easy access**
- **To access crossover report, navigate to /easteregg/crossover, or click on the crossover button in the easter egg navbar. [Or use link](http://rubinfamily.dyndns.org:5000/easteregg/crossover)**

- Front End Aspect
  - Visuals: 
    - For the last couple of weeks, we mainly worked on visuals in our home page, such as [displaying quotes from an api,](https://github.com/zenxha/sushi/blob/cd2b15bcf0891ea65179d5313b9b589c463e3676/views.py#L31-L38) and creating a [nice looking home page with CSS.](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/base2.html#L38-L163)
    - We are currently working on our table to display user uploaded info from the upload page onto our browse page
  - HTML:
    - We primarily focused on implementing a scoreboard/table like Trish demonstrated, which can be seen in our [browse.html](https://github.com/zenxha/sushi/blob/main/templates/homesite/browse.html) file.
  - CSS: 
    - We used CSS in designing our pages on the website, such as our [home page,](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/base2.html#L38-L163) [login page,](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/login.html#L7-L135) and [upload page.](https://github.com/zenxha/sushi/blob/d7b689743ea916ab470de41c06ed3d0e4fa7c28f/templates/homesite/loginv2.html#L11-L135)

- Back End Aspect
  - Routes: 
    - The recently updated routes on our project are our [easteregg path where you need mort as the username](https://github.com/zenxha/sushi/blob/358412ff2e6057e202f4d1b2e697487fca2fd6a9/views.py#L63-L71) and [browse page](https://github.com/zenxha/sushi/blob/358412ff2e6057e202f4d1b2e697487fca2fd6a9/views.py#L47-L60) that takes info from upload and displays it on the browse page.
  - Database:
    - We mainly use the information stored on [this database](https://github.com/zenxha/sushi/blob/fa37260ea37930cff19fd023076c2a3ee56d5a4f/model.py#L5-L11), and the information gets [stored from the upload page](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/views.py#L62-L82) and is [displayed on our browse page](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/views.py#L47-L60) [here](https://github.com/zenxha/sushi/blob/36fed625125b4679d7682e593dbc592bade06ace/templates/homesite/browse.html#L14-L18)
- Easter Egg 
  - To get to our easter egg, fill out the upload form on the website but put mort as the username to access the easteregg
- Project WOW
  - [Our upload page](http://rubinfamily.dyndns.org:5000/upload). Once you upload an image, type in http://rubinfamily.dyndns.org:5000/images/1 to view the image you just uploaded. Each image uploaded is assigned an id, starting with 1, so if you upload another image, you can replace 1 with 2 to view that uploaded image, and so on.


### Tickets Progress
- Allen
  - [Worked on creating the IAM page and displaying each person's IAM statements](https://github.com/zenxha/sushi/projects/4#card-54281293)
  - [Worked with Chris on creating the front end for our browse page that displays the user's review (2nd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)
  - [Embed the crossover report into the easter egg navbar](https://github.com/zenxha/sushi/projects/4#card-55314605)
  - [Moved the project section from the main site navbar to the easter egg navbar](https://github.com/zenxha/sushi/projects/4#card-55314635)
- Chris
  - [Work on the user sessions as well as user authentication](https://github.com/zenxha/sushi/projects/4#card-53703118)
  - [Worked on creating the front end for the browse page that displays user info and implementing CSS on the page(2nd and 3rd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)
- Devam
  - [Work on user login and authentication (still incomplete due to technical issues. We have it running, but not storing in database)](https://github.com/zenxha/sushi/projects/4#card-53785877)
  - [Helped secure the route to easter egg so it is only accessible by entering mort as the username, and can't be viewed by just typing in the url (checkbox 2 and 3)](https://github.com/zenxha/sushi/projects/4#card-53782464)
- Komay
  - [Worked on integrating the backend login/auth system with the frontend html form](https://github.com/zenxha/sushi/projects/4#card-54354857)
  - [Finished 3rd checkbox of the ticket which only allows the correct account to access easteregg](https://github.com/zenxha/sushi/projects/4#card-53782464)
  - [Worked on the backend aspect of taking the informatoin from upload.html and displaying it on browse.html(1st and 3rd checkbox)](https://github.com/zenxha/sushi/projects/4#card-55146571)

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

