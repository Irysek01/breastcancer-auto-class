echo "Id,Predicted" > proposed_models/beit-base-finetuned-BreastCancer/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 proposed_models/beit-base-finetuned-BreastCancer/predict.py -i $f >> proposed_models/beit-base-finetuned-BreastCancer/submission.csv
    python3 scripts/remove_unwanted_lines.py -i proposed_models/beit-base-finetuned-BreastCancer/submission.csv
done

