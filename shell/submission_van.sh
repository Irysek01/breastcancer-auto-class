echo "Id,Predicted" > proposed_models/CARPE-VAN/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 proposed_models/CARPE-VAN/predict.py -i $f >> proposed_models/CARPE-VAN/submission.csv
    python3 scripts/remove_unwanted_lines.py -i proposed_models/CARPE-VAN/submission.csv 
done
