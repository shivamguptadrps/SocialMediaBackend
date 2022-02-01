ToDoBackend is Python API written in django rest framework for social media app like Twitter .
Api is installed on azure server with IP http://40.121.193.12:8001



PROJECT INSTALLATION INSTRUCTION:
python3 -m venv env     //create virtual environment
source env/bin/activate //actiavte virtual environment
pip3 install -r requirements.txt  //install all requirements

python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py runserver



API DETAILS

 url(r'^signin/$', views.signin),
    url(r'^signup/$', views.signup),
    url(r'^home/$', views.home),
    url(r'^tweet/$', views.dotweet),
    url(r'^follow/$', views.dofollow),


To create your account
Method : POST
URL : http://40.121.193.12:8001/listtodo/signup           or    http://127.0.0.1:8001/listtodo/signup/
Allow: POST -   {username: "shivam", password: "1234", email: "shivam@contaque.com", cnfpassword: "1234", userfullname: "1111",usern_mobile_no: "07007504187",profile_pic: picture }



To sign in your account
Method : POST
URL : http://40.121.193.12:8001/listtodo/signin/        or   http://127.0.0.1:8001/listtodo/signin/
{userid: "Reena", password: "1234"}




To do Tweet with your account
Method : POST
URL : http://40.121.193.12:8001/listtodo/tweet/      or   http://127.0.0.1:8001/listtodo/tweet/
{desc: "Tweet details", authtoken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTY0M…5hIn0.E4ipq_DetxaED_9TY7NpRkarbWWyVbBQ_IzpkM8QerU", tweeting: File}





To Follow other user with his user id
Method : POST
URL : http://40.121.193.12:8001/listtodo/follow/    or   http://127.0.0.1:8001/listtodo/follow/
{id: "112345678902", authtoken: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTY0M…5hIn0.E4ipq_DetxaED_9TY7NpRkarbWWyVbBQ_IzpkM8QerU"}









