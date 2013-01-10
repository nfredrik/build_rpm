#!/usr/bin/env sh
# TODO:
# binary files should go under SRPMS
# check afterwards in this script with rpmlint?
# one or several rpms?
# Dependencies?  framework?
# md5?
# installera köra i rpm:en?

set -x 

export WORKSPACE=$1
export TAGNAME=$2
export BUILD_NUMBER =$3

cd $WORKSPACE

[[ -d rpmbuild ]] && rm -fr rpmbuild
    mkdir rpmbuild
    
cd rpmbuild

# Clean up and create directories
for dir in BUILD RPMS SOURCES SPECS SRPMS
do
 [[ -d $dir ]] && rm -Rf $dir
  mkdir $dir
done

# Put our files in the right place
mv helloworld.sh SOURCES/.
mv helloworld.spec SPECS/.

# Create rpm in RPMS/noarch/
rpmbuild  --define 'TAGNAME '$TAGNAME  --define 'BUILD_NUMBER '$BUILD_NUMBER --define '_topdir '`pwd` -ba SPECS/helloworld.spec
