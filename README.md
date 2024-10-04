# TR-AlgoRit
Part of my Research Work (Treball de Recerca in Catalonia, done in Baccalaureate) about how can non-AI algorithms recommend music based on the user's preferences. The python script is an implementation of such algorithm. It's not really well done, but it was my first programming project as a beginner. 

All the script is written in the same file, in Python language. So to run it, it is a must having: Python interpreter and the libraries shown at the start of the code.

The main script uses the songs that are shown in "Infocançons.txt", which may not be uploaded due to upload size limitations. So to use it properly, with your own songs if you wish, you must follow the format, which is: the songs must be in ".wav" format, the documentation of each song in "Infocançons.txt" must follow its format (that is:         name,genre,name.wav,author,instrumental_to_lyrics_ratio,tempo,tonality,date)

The script stores each user's data in "Music_userdata.txt". It's not the safest implementation of user data storage, specifically it is risky because of passwords, but since this was done for testing for the Research Work, there's a lot of things lacking for actual user's usability and safety. Nonetheless, changing this document by a proper database isn't particularly hard, because the code just calls for the document 2 times: when retrieving data and when storing it.

For the UI, the script requires the images in "Images.zip" to display everything correctly. 

Finally, remember to replace all the <your_relative_path> for the path to the correspondent file.

And that's everything you should know to have no problems using this program.
