echo "Id,Predicted" > proposed_models/breastcanc_class_RNN/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 scripts/process.py -i $f >> proposed_models/breastcanc_class_RNN/submission.csv
    python3 scripts/remove_unwanted_lines.py -i proposed_models/breastcanc_class_RNN/submission.csv
done

