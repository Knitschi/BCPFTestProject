git pull
git submodule update --remote --rebase
git commit . -m"update submodules"

:: Tags
::pushd Sources\APackage
::    git tag -l | xargs git tag -d
::    git fetch --tags
::popd

::git tag -l | xargs git tag -d
::git fetch --tags