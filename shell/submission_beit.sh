echo "Id,Predicted" > proposed_models/bus-deit/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 proposed_models/bus-deit/predict.py -i $f >> proposed_models/bus-deit/submission.csv
    python3 scripts/remove_unwanted_lines.py -i proposed_models/bus-deit/submission.csv
done

