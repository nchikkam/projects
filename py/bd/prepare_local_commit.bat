git init
pip freeze > requirements.txt
echo "web: gunicorn main:app" > Procfile
git add *
git commit -m "correcting the links"
heroku git:remote -a <heroku-app-name>
git push heroku master
