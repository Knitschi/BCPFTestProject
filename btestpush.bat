
pushd Sources\APackage

echo namespace{} >> b.cpp
git commit . -m"dummy edit"
echo namespace{} >> b.cpp
git commit . -m"dummy edit"
echo namespace{} >> b.cpp
git commit . -m"dummy edit"

git push

popd

::git commit . -m"update APackage"
::git push origin refs/notes/* refs/heads/master refs/tags/*

::git notes append -m "dontTr1gger"
