ASR Pipeline using Whisper for Hindi Speech Recognition
📌 Overview

This project implements an end-to-end Automatic Speech Recognition (ASR) pipeline using the Whisper model. The objective is to preprocess audio-text data, fine-tune a speech recognition model, evaluate performance using Word Error Rate (WER), and perform detailed error analysis.

The project also includes text cleanup operations such as number normalization and English word detection, along with linguistic analysis for spelling correction and lattice-based evaluation.

📁 Project Structure
josh_talk/
│
├── src/
│   ├── data/
│   │   ├── download_data.py
│   │   ├── preprocess.py
│   │
│   ├── model/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   ├── evaluate_fleurs.py
│   │   ├── error_analysis.py
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── models/
│   ├── fine_tuned/
│
├── report.pdf
├── README.md
⚙️ Environment Setup

This project uses two virtual environments:

🧠 Python 3.14 for training and preprocessing
📊 Python 3.10 for dataset compatibility (FLEURS)
🧠 Python 3.14 Environment (Main)

Used for preprocessing, training, and local evaluation.

Create environment
python3 -m venv .venv
Activate environment
source .venv/bin/activate
Install dependencies
pip install torch torchaudio
pip install transformers datasets jiwer librosa soundfile accelerate pandas tqdm
Verify version
python --version

Expected:

Python 3.14.x

📊 Python 3.10 Environment (Required for FLEURS)

Used only for loading and evaluating the Hugging Face dataset.

Install Python 3.10
brew install pyenv
pyenv install 3.10.14
Set Python version
pyenv local 3.10.14
Create environment
python -m venv .venv310
Activate environment
source .venv310/bin/activate
Install dependencies
pip install torch torchaudio
pip install transformers datasets jiwer librosa soundfile accelerate pandas tqdm
Verify version
python --version

Expected:

Python 3.10.x

🔄 Switching Between Environments

Activate Python 3.14:

source .venv/bin/activate

Activate Python 3.10:

source .venv310/bin/activate

Deactivate:

deactivate

🧑‍💻 VS Code Setup
Open Command Palette
Cmd + Shift + P
Select
Python: Select Interpreter
Choose:
.venv/bin/python → Python 3.14
.venv310/bin/python → Python 3.10

📥 Data Preparation
Step 1: Download Data
python src/data/download_data.py

Note: Some URLs may be restricted. Fallback strategies were used where needed.

Step 2: Preprocess Data
python src/data/preprocess.py

Output:

data/processed/dataset.csv

Format:

audio_path,text

🤖 Model Training
python src/model/train.py

Details:

Whisper-tiny model
Custom training loop
librosa for audio loading

📊 Evaluation
Local Dataset
python src/model/evaluate.py
FLEURS Dataset
source .venv310/bin/activate
python src/model/evaluate_fleurs.py

🔍 Error Analysis
python src/model/error_analysis.py

🧹 Cleanup Pipeline

Includes:

🔢 Number normalization
🌐 English word detection
🧠 Spell Correction

Dictionary-based validation
Edit distance
Confidence scoring

🧩 Lattice-Based Evaluation
Handles multiple valid transcriptions
Reduces unfair WER penalties
Uses word-level alignment

📈 Results
Model	WER
Whisper Tiny (Base)	1.00
Fine-tuned Model	1.00

⚠️ Limitations
Restricted dataset URLs
Synthetic audio used
Limited dataset size
Python compatibility issues

🚀 Future Improvements
Use real speech datasets
Improve multilingual handling
Expand dataset size
Enhance code-switch support

▶️ Run Complete Pipeline
python src/data/download_data.py
python src/data/preprocess.py
python src/model/train.py
python src/model/evaluate.py

👤 Author

Abhishek Kumar
