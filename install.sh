echo "creating virtual environment in .venv ->" &&
python3 -m venv .venv &&
echo "                                 done ->" &&
source .venv/bin/activate &&
echo "installing requirements ->" &&
pip3 install -r src/requirements.txt &&
deactivate &&
echo "                   done <-"
