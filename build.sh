.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
reflex init
reflex export --frontend-only
rmdir /s /q public
Expand-Archive -Path frontend.zip -d public   
del frontend.zip
deactivate