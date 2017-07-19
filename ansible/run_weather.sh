source ~/taxidata/bin/activate
cd ~/taxidata/sg-taxidata
ORIGINAL_PYTHONPATH=$PYTHONPATH
export PYTHONPATH="$PWD/api/:$ORIGINAL_PYTHONPATH"
echo $PYTHONPATH
python api/fetch_weather_to_file.py
