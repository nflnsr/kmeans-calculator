echo " Build Start"
python3.8 -m pip install -r requirements.txt

python3.8 manage.py collectstatic --noinput --clear
echo " Build End" 