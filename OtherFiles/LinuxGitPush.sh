time=$(date "+%y.%m.%d-%H.%M.%S")
nowpath=$(gwd)

cd /mnt/d/Codes
git add -A
git commit -m $time
git push
cd nowpath

