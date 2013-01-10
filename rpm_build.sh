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
rpmbuild --define '_topdir '`pwd` -ba SPECS/helloworld.spec
