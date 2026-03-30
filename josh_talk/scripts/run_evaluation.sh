

echo " Starting Evaluation..."

python src/model/evaluate.py

if [ $? -ne 0 ]; then
  echo " Evaluation failed"
  exit 1
fi

echo " Evaluation completed!"