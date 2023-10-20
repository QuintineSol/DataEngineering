gsutil cp ../data/* gs://data_de2023_qjsol

git config --global user.email "quintine@example.com"
git config --global user.name "Quintine Sol"
echo "data uploaded" >> data_upload.txt
git commit -am "data uploaded"
git push https://$1:$2@github.com/QuintineSol/DataEngineering.git --all