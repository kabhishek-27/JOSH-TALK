

echo "🚀 Starting Training Pipeline..."


echo " Preprocessing dataset..."
python src/data/preprocess.py

if [ $? -ne 0 ]; then
  echo " Preprocessing failed"
  exit 1
fi


echo " Training Whisper model..."
python src/model/train.py

if [ $? -ne 0 ]; then
  echo " Training failed"
  exit 1
fi

echo " Training completed successfully!"