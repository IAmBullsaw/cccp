echo "creating virtual environment in .venv ->" &&
python3 -m venv .venv &&
echo "                                 done <-" &&
source .venv/bin/activate &&
echo "installing requirements ->" &&
pip3 install --upgrade pip 1> /dev/null &&
pip3 install -r requirements.txt 1> /dev/null &&
deactivate &&
echo "                   done <-"
echo -e "activate on linux with \nsource .venv/bin/activate"
