# OTF_Part2
This is the part 2 of the test 'On The Fuze'

What is your usual IDE? 
  -Spyder
What are the advantages of this IDE over the others?
  -I don't have an specific reason to use spyder, I know that spyder is an IDE specially for python and it can manage big programs in python.
Which of the items resulted in the most computational time for you? Add time in seconds.
  -The longest time in program is in the load function because I didn't find a way to load all the properties in one time I used a FOR to load all the data
   so for that reason take a lot of time. Another point is that I'm printing each response with the server to certify that I'm sending all the data and this part it could take a big amount of time.

    Time_extraction= 29.52s
    Time_transform=25.52s
    Time_load=1350s-22min aprox


   
If you have any public portfolio (e.g., IA, computer visión, data processing...),please share the link with us.
  -I have 3 projects on python if you want to see it:
   The first one was my thesis, I did an IoT system to measure the quality of the drivers in Transmilenio (The program takes the data of an accelerometer, do some calculations and send it to a cloud system (firebase), and then show the data in a web page)
   (https://github.com/danizu001/TdG_DanielGonzalez_CarlosMedina)
   The second and third one were 2 project on my actual job with a partner to automate all the manual tasks in our work, saving more than 1 day of time.  
   (https://github.com/danizu001/Csg_programs)



About the 5 point I'm not sure if it is possible but we could save the deleted duplicates in another json with the deleted propertes but without the email because is theonly one who has a a unique ID.
For example:
We have this data
  |  Name    |      Email         |    street      |     date      |
  | :---:    |       :---:        |     :---:      |      :---:    | 
  |Daniel G  |   dany@gmail.com   |   Autopista    |   2023/07/03  |
  | :---:    |       :---:        |     :---:      |      :---:    |
  |Daniel G  |   dany@hotmail.com |    Boyaca      |   2021/07/03  |

so we know the program is going to save the first row because is the recent date, the second row is going to delete it.
The possibility is save the second row but without the email so we  are going to save the second row like that.
   |  Name    |      Email         |    street      |     date      |
   | :---:    |       :---:        |     :---:      |      :---:    |
   |Daniel G  |   dany@hotmail.com |    Boyaca      |   2021/07/03  |
And when we want to retrieve this data we will search the firstname and lastname
