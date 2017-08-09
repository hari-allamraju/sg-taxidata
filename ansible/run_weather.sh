source ~/taxidata/bin/activate
cd ~/taxidata/sg-taxidata
ORIGINAL_PYTHONPATH=$PYTHONPATH
export PYTHONPATH="$PWD:$ORIGINAL_PYTHONPATH"
echo $PYTHONPATH
python sgtaxidata/fetch_weather_to_file.py
