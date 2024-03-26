echo "Id,Predicted" > foundation_model/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 scripts/process.py -i $f >> foundation_model/submission.csv
done

