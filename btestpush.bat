
pushd Sources\BPackage

git pull

echo namespace{} >> b.h
git commit . -m"dummy edit"
echo namespace{} >> b.h
git commit . -m"dummy edit"
echo namespace{} >> b.h
git commit . -m"dummy edit"

git push

popd
