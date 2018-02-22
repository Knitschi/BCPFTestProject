
pushd Sources\BPackage

echo namespace{} >> b.cpp
git commit . -m"dummy edit"
echo namespace{} >> b.cpp
git commit . -m"dummy edit"
echo namespace{} >> b.cpp
git commit . -m"dummy edit"

git push

popd
