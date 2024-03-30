echo "Id,Predicted" > proposed_models/mit-b0-finetuned-BreastCancer/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 proposed_models/mit-b0-finetuned-BreastCancer/predict.py -i $f >> proposed_models/mit-b0-finetuned-BreastCancer/submission.csv
    python3 scripts/remove_unwanted_lines.py -i proposed_models/mit-b0-finetuned-BreastCancer/submission.csv
done
