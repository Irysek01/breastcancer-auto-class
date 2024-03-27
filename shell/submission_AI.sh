echo "Id,Predicted" > proposed_models/clip-vit-finetuned-breastcancer/submission.csv

for f in complete_set/testing_setwm/*.png
do
    python3 proposed_models/clip-vit-finetuned-breastcancer/predict.py -i $f >> proposed_models/clip-vit-finetuned-breastcancer/submission.csv
done

